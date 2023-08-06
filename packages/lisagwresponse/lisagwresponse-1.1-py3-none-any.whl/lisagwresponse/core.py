#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core module.

Implements the base class to compute LISA response to gravitational waves,
plot them and write a gravitational-wave file.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import abc
import logging
import numpy
import matplotlib.pyplot
import h5py
import healpy

from numpy import pi, cos, sin
from scipy.interpolate import InterpolatedUnivariateSpline
from packaging.version import Version
from packaging.specifiers import SpecifierSet
from lisaconstants import c, au

from .utils import dot, norm
from .psd import white_generator

from .meta import __version__
from .meta import __author__


logger = logging.getLogger(__name__)


class GWResponse(abc.ABC):
    """Abstract base class representing a GW source.

    Sampling parameters (``dt``, ``size``, and ``t0``) are used to generate when creating a GW file.
    Note that they are ignored when writing to an existing GW file.

    Args:
        orbits (str): path to orbit file
        orbit_interp_order (int): orbits spline-interpolation order [one of 1, 2, 3, 4, 5]
        dt (float): simulation sampling period [s]
        size (int): simulation size [samples]
        t0 (int): simulation initial time [s]
    """

    SC = [1, 2, 3] #: List of spacecraft indices.
    LINKS = [12, 23, 31, 13, 32, 21] #: List of link indices.

    def __init__(self, orbits, orbit_interp_order=1, dt=0.3, size=259200, t0=0):

        self.git_url = 'https://gitlab.in2p3.fr/lisa-simulation/gw-response'
        self.generator = self.__class__.__name__
        self.version = __version__
        logger.info("Initializing gravitational-wave response (lisagwresponse verion %s)", self.version)

        self.orbits_path = str(orbits) #: str: Path to orbit file.
        self.orbit_interp_order = int(orbit_interp_order) #: int: Orbits spline-interpolation order.

        self.dt = float(dt) #: float: Sampling period [s].
        self.t0 = float(t0) #: float: Initial time [s].
        self.size = int(size) #: int: Simulation size [samples].
        self.fs = 1 / self.dt #: float: Sampling frequency [Hz].
        self.duration = self.size * self.dt #: float: Simulation duration [s].
        self.t = self.t0 + numpy.arange(self.size) * self.dt #: array: Time array [s].

    @abc.abstractmethod
    def compute_gw_response(self, links, t):
        """Compute the response for a list of links.

        If all links share the same time vector, use a 1-dim ``t`` argument of size ``N``.
        If different times must be used for each link, use a 2-dim ``t`` with shape
        ``(len(links), N)``.

        The link esponses are expressed as relative frequency fluctuations.

        This method must be implemented by subclasses.

        Args:
            links (array-like): link indices
            t (array-like): TCB times of shape ``(N)`` or ``(len(links), N)`` [s]

        Returns:
            Array of shape ``(len(links), N)`` containing the response of each link,
            as relative frequency fluctuations (strain units).
        """
        raise NotImplementedError

    def plot(self, t, output=None, gw_name='gravitational wave'):
        """Plot gravitational-wave response.

        Args:
            t (array-like): TCB times [s]
            output (str or None): output file, None to show the plots
            gw_name (str): optional gravitational-wave source name
        """
        logger.info("Plotting gravitational-wave response")
        matplotlib.pyplot.figure(figsize=(12, 4))
        response = self.compute_gw_response(self.LINKS, t)
        for link_index, link in enumerate(self.LINKS):
            matplotlib.pyplot.plot(t, response[link_index], label=link)
        matplotlib.pyplot.grid()
        matplotlib.pyplot.legend()
        matplotlib.pyplot.xlabel("Time [s]")
        matplotlib.pyplot.ylabel("Link response")
        matplotlib.pyplot.title(f"Link response to {gw_name}")
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def _write_metadata(self, hdf5, prefix=''):
        """Set all properties as HDF5 attributes on `object`.

        Try to store all variables as attributes. If it is too large or its type is not
        supported, try to store a string representation; if this fails, log a warning.

        Args:
            hdf5 (h5py.File): an HDF5 file or dataset
        """
        for key, value in self.__dict__.items():
            pkey = f'{prefix}{key}'
            try:
                hdf5.attrs[pkey] = value
            except (TypeError, RuntimeError):
                try:
                    hdf5.attrs[pkey] = str(value)
                except RuntimeError:
                    logger.warning("Cannot write metadata '%s' on '%s'", pkey, hdf5)

    def _interpolate_tps(self, sc, tau):
        r"""Return TCB times corresponding to each TPS times.

        GW responses :math:`H_{ij}^{t}(\tau)` are computed as functions of TCB.

        To compute GW responses as functions of the receiving spacecraft TPS
        :math:`H_{ij}^{\tau_i}(\tau)`, one needs to convert those reception TPSs
        :math:`\tau` to their TCB equivalent :math:`t^{\tau_i}`, such that

        .. code-block :: python

            H_{ij}^{\tau_i}(\tau) = H_{ij}^{t}(t^{\tau_i}(\tau)) \qs

        Orbit files contain a vector of TCB times for a regularly sampled TPS time grid.

        Use this method to interpolate between these values and obtain the TCB equivalent
        times for an arbitrary vector of TPS times (for each spacecraft).

        Args:
            sc (array-like): spacecraft indices
            tau (array-like): TPS times [s]

        Returns:
            Array of shape ``(len(sc), len(tau))`` of equivalent TPS times.

        Raises:
            ValueError: If ``tau`` lies outside of the orbit valid range (no extrapolation).
        """
        logger.info("Computing spline interpolation for TPS times")
        interpolate = lambda t, data: InterpolatedUnivariateSpline(t, data, ext='raise')

        with h5py.File(self.orbits_path, 'r') as orbitf:

            # Warn for orbit file development version
            version = Version(orbitf.attrs['version'])
            logger.debug("Using orbit file version %s", version)
            if version.is_devrelease:
                logger.warning("You are using an orbit file in a development version")

            if version in SpecifierSet('== 1.*', True):
                tps = [
                    interpolate(orbitf['/tps/tau'], orbitf[f'/tps/sc_{sci}'])(tau)
                    for sci in sc
                ]
            elif version in SpecifierSet('== 2.*', True):
                times = orbitf.attrs['t0'] + numpy.arange(orbitf.attrs['size']) * orbitf.attrs['dt']
                tps = [
                    interpolate(times, orbitf['tps/t'][:, sci - 1])(tau)
                    for sci in sc
                ]
            else:
                raise ValueError(f"unsupported orbit file version '{version}'")

        return numpy.stack(tps, axis=0)

    def write(self, path='gw.h5', mode='a', timeframe='both'):
        """Compute and write the response to a GW file.

        If the GW file does not exist, it is created with the source's sampling parameters and the
        6 link responses are computed according to these parameters and written to file. If the GW
        file already exists, the 6 link responses are computed according to the GW file's sampling
        parameters and added to the file.

        When creating the GW file, metadata are saved as attributes.

        When writing a GW response, we add attributes for each local variable, prefixed with ``gw<i>``,
        where i is the index of the GW response in the file.

        Args:
            path (str): path to the GW file
            mode (str): opening mode
            timeframe (str): timetime to compute responses ('tps', 'tcb', or 'both')
        """
        # Open GW file
        logger.info("Opening or creating gravitational-wave file '%s'", path)
        with h5py.File(path, mode) as hdf5:

            # Create time dataset if needed, and write some attributes, and create empty link datasets
            if 't' not in hdf5:
                logger.info("New gravitational-wave file, creating time dataset")
                t = self.t
                hdf5.create_dataset('t', data=t)
                logger.info("Setting global metadata")
                self._write_metadata(hdf5)
                hdf5.attrs['gw_count'] = 0
                for tframe in ['tcb', 'tps']:
                    for link in self.LINKS:
                        dname = f'{tframe}/l_{link}'
                        logger.info("Creating empty link datasets '%s'", dname)
                        hdf5.create_dataset(dname, data=numpy.zeros_like(t))
            else:
                t = hdf5['t'][:]

            # Setting metadata
            logger.info("Setting injection metadata")
            ngw = int(hdf5.attrs['gw_count'])
            hdf5.attrs['gw_count'] = ngw + 1
            self._write_metadata(hdf5, prefix=f'gw{ngw}_')

            # Compute equivalent TCB times for TPSs
            if timeframe == 'both':
                tau = self._interpolate_tps(self.SC, t) # shape (3, t)
                tau_links = tau[[int(str(link)[0]) - 1 for link in self.LINKS]] # shape (6, t)
                t_links = numpy.tile(t, (6, 1)) # shape (6, t)
                times = numpy.concatenate([t_links, tau_links], axis=-1) # shape (6, 2t)
            elif timeframe == 'tcb':
                times = t # shape (t)
            elif timeframe == 'tps':
                tau = self._interpolate_tps(self.SC, t) # shape (3, t)
                tau_links = tau[[int(str(link)[0]) - 1 for link in self.LINKS]] # shape (6, t)
                times = numpy.tile(t, (6, 1)) # shape (6, t)
            else:
                raise ValueError(f"invalid timeframe '{timeframe}'")

            # Compute link response
            response = self.compute_gw_response(self.LINKS, times) # shape (6, 2t) or (6, t)

            # Add response to link datasets
            for link_index, link in enumerate(self.LINKS):
                if timeframe == 'tcb':
                    dname = f'tcb/l_{link}'
                    logger.info("Adding gravitational-wave response to link dataset '%s'", dname)
                    hdf5[dname][:] += response[link_index, :len(t)] # shape (6, t)
                if timeframe == 'tps':
                    dname = f'tps/l_{link}'
                    logger.info("Adding gravitational-wave response to link dataset '%s'", dname)
                    hdf5[dname][:] += response[link_index, :len(t)] # shape (6, t)
                if timeframe == 'both':
                    dname = f'tcb/l_{link}'
                    logger.info("Adding gravitational-wave response to link dataset '%s'", dname)
                    hdf5[dname][:] += response[link_index, :len(t)] # shape (6, t)
                    dname = f'tps/l_{link}'
                    logger.info("Adding gravitational-wave response to link dataset '%s'", dname)
                    hdf5[dname][:] += response[link_index, len(t):] # shape (6, t)

        # Closing file
        logger.info("Closing gravitational-wave file '%s'", path)


class ReadGWResponse(GWResponse):
    """Reads already-computed link responses.

    Use this class if the link responses are available as Numpy arrays,
    and you want to use GW files or the interface offered by this package.

    To honor the source's sampling parameters, the input data may be resampled using
    spline interpolation. If you do not wish to interpolate, make sure to instantiate
    the source with sampling parameters matching your data.

    Args:
        t (array-like): TCB times associated with link responses [s]
        y_12 (array-like): response of link 12
        y_23 (array-like): response of link 23
        y_31 (array-like): response of link 31
        y_13 (array-like): response of link 13
        y_32 (array-like): response of link 32
        y_21 (array-like): response of link 21
        interp_order (int): response spline-interpolation order [one of 1, 2, 3, 4, 5]
        **kwargs: all other args from :class:`lisagwresponse.GWResponse`
    """

    def __init__(self, t, y_12, y_23, y_31, y_13, y_32, y_21, interp_order=1, **kwargs):
        super().__init__(**kwargs)
        self.interp_order = int(interp_order) #: int: Response spline-interpolation order.

        # Compute spline interpolation
        logger.info("Computing spline interpolation from time series")
        data = {'12': y_12, '23': y_23, '31': y_31, '13': y_13, '32': y_32, '21': y_21}
        self.interpolants = {
            link: InterpolatedUnivariateSpline(t, data[link], k=self.interp_order, ext='zeros')
            for link in self.LINKS
        } #: Dictionary of interpolating spline functions (link indices as keys).

    def compute_gw_response(self, links, t):
        # Broadcast times if needed
        if t.ndim == 1:
            t = numpy.tile(t, (len(links), 1))
        # Interpolate strain
        responses = [self.interpolants[link](t_link) for link, t_link in zip(links, t)]
        return numpy.stack(responses, axis=0)


class Strain(GWResponse, abc.ABC):
    """Abstract base that computes link responses from GW strain time series.

    Args:
        gw_beta (float): ecliptic latitude [rad]
        gw_lambda (float): ecliptic longitude [rad]
        x (callable): spacecraft x-position interpolating functions, overrides orbits [m]
        y (callable): spacecraft y-position interpolating functions, overrides orbits [m]
        z (callable): spacecraft z-position interpolating functions, overrides orbits [m]
        ltt (callable): light travel time interpolating functions, overrides orbits [s]
        t0 (float or str): initial time [s], or ``'orbits'`` to match orbit file's initial time
        **kwargs: all other args from :class:`lisagwresponse.GWResponse`
    """

    def __init__(self,
                 gw_beta,
                 gw_lambda,
                 x=None,
                 y=None,
                 z=None,
                 ltt=None,
                 t0='orbits',
                 **kwargs):

        # Forward numerical values of t0 to superclass
        if t0 != 'orbits':
            kwargs['t0'] = t0

        super().__init__(**kwargs)
        self.gw_beta = float(gw_beta)
        self.gw_lambda = float(gw_lambda)

        # Handle orbits
        if x is not None or y is not None or z is not None or ltt is not None:
            logger.info("Using provided functions for orbits")
            self._set_orbits(x, y, z, ltt)
        else:
            logger.info("Reading orbits from file '%s'", self.orbits_path)
            self._interpolate_orbits()
            if t0 == 'orbits':
                logger.debug("Reading initial time from orbit file '%s'", self.orbits_path)
                with h5py.File(self.orbits_path, 'r') as orbitf:
                    # Warn for orbit file development version
                    version = Version(orbitf.attrs['version'])
                    logger.debug("Using orbit file version %s", version)
                    if version.is_devrelease:
                        logger.warning("You are using an orbit file in a development version")
                    # Switch between versions
                    if version in SpecifierSet('== 1.*', True):
                        self.t0 = float(orbitf.attrs['tau0'])
                    elif version in SpecifierSet('== 2.*', True):
                        self.t0 = float(orbitf.attrs['t0'])
                    else:
                        raise ValueError(f"unsupported orbit file version '{version}'")

        # Compute source-localization vector basis
        self.k = numpy.array([
            -cos(self.gw_beta) * cos(self.gw_lambda),
            -cos(self.gw_beta) * sin(self.gw_lambda),
            -sin(self.gw_beta),
        ]) #: Wave propagation unit vector.
        self.u = numpy.array([
            sin(self.gw_lambda),
            -cos(self.gw_lambda),
            0
        ])
        self.v = numpy.array([
            -sin(self.gw_beta) * cos(self.gw_lambda),
            -sin(self.gw_beta) * sin(self.gw_lambda),
            cos(self.gw_beta),
        ])

    def _interpolate_orbits(self):
        """Interpolate orbit data (spacecraft positions and light travel times).

        Also check that orbit file is valid and supported.

        Raises:
            ValueError if orbit file is not supported.
        """
        logger.info("Computing spline interpolation for orbits")
        interpolate = lambda t, data: InterpolatedUnivariateSpline(
                t, data, k=self.orbit_interp_order, ext='raise')

        with h5py.File(self.orbits_path, 'r') as orbitf:

            # Warn for orbit file development version
            version = Version(orbitf.attrs['version'])
            logger.debug("Using orbit file version %s", version)
            if version.is_devrelease:
                logger.warning("You are using an orbit file in a development version")

            if version in SpecifierSet('== 1.*', True):
                self.x = {
                    sc: interpolate(orbitf['tcb/t'], orbitf[f'tcb/sc_{sc}']['x'])
                    for sc in self.SC
                }
                self.y = {
                    sc: interpolate(orbitf['tcb/t'], orbitf[f'tcb/sc_{sc}']['y'])
                    for sc in self.SC
                }
                self.z = {
                    sc: interpolate(orbitf['tcb/t'], orbitf[f'tcb/sc_{sc}']['z'])
                    for sc in self.SC
                }
                self.ltt = {
                    link: interpolate(orbitf['tcb/t'], orbitf[f'tcb/l_{link}']['tt'])
                    for link in self.LINKS
                }
            elif version in SpecifierSet('== 2.*', True):
                times = orbitf.attrs['t0'] + numpy.arange(orbitf.attrs['size']) * orbitf.attrs['dt']
                self.x = {
                    sc: interpolate(times, orbitf['tcb/x'][:, i, 0])
                    for i, sc in enumerate(self.SC)
                }
                self.y = {
                    sc: interpolate(times, orbitf['tcb/x'][:, i, 1])
                    for i, sc in enumerate(self.SC)
                }
                self.z = {
                    sc: interpolate(times, orbitf['tcb/x'][:, i, 2])
                    for i, sc in enumerate(self.SC)
                }
                self.ltt = {
                    link: interpolate(times, orbitf['tcb/ltt'][:, i])
                    for i, link in enumerate(self.LINKS)
                }
            else:
                raise ValueError(f"unsupported orbit file version '{version}'")

    def _set_orbits(self, x, y, z, ltt):
        """Set orbit data from dictionaries (spacecraft positions and light travel times).

        Args:
            x (callable): spacecraft x-position interpolating functions, overrides orbits [m]
            y (callable): spacecraft y-position interpolating functions, overrides orbits [m]
            z (callable): spacecraft z-position interpolating functions, overrides orbits [m]
            ltt (callable): light travel time interpolating functions, overrides orbits [s]
        """
        # pylint: disable=cell-var-from-loop
        # We use default values for `val` in lambdas to capture the values
        self.x = {
            sc: x[sc] if callable(x[sc]) else lambda t, val=x[sc]: float(val)
            for sc in self.SC
        }
        self.y = {
            sc: y[sc] if callable(y[sc]) else lambda t, val=y[sc]: float(val)
            for sc in self.SC
        }
        self.z = {
            sc: z[sc] if callable(z[sc]) else lambda t, val=z[sc]: float(val)
            for sc in self.SC
        }
        self.ltt = {
            link: ltt[link] if callable(ltt[link]) else lambda t, val=ltt[link]: float(val)
            for link in self.LINKS
        }

    @abc.abstractmethod
    def compute_hplus(self, t):
        """Compute +-polarized gravitational-wave strain :math:`h_+(t)` in the BCRS.

        Args:
            t (array-like): TCB times [s]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_hcross(self, t):
        """Compute x-polarized gravitational-wave strain :math:`h_\\times(t)` in the BCRS.

        Args:
            t (array-like): TCB times [s]
        """
        raise NotImplementedError

    def compute_gw_response(self, links, t):
        """Compute the response for a list of links according :doc:`model`.

        If all links share the same time vector, use a 1-dim ``t`` argument of size ``N``.
        If different times must be used for each link, use a 2-dim ``t`` with shape
        ``(len(links), N)``.

        The link esponses are expressed as relative frequency fluctuations.

        Args:
            links (array-like): link indices
            t (array-like): TCB times of shape ``(N)`` or ``(len(links), N)`` [s]

        Returns:
            Array of shape ``(len(links), N)`` containing the response of each link,
            as relative frequency fluctuations (strain units).
        """
        # pylint: disable=too-many-locals
        logger.info("Computing gravitational-wave response for links %s", links)

        # Broadcast times if needed
        if t.ndim == 1:
            t = numpy.tile(t, (len(links), 1)) # (link, t)

        # Compute emission and reception time at spacecraft
        logger.debug("Computing emission time at spacecraft")
        trec = t # (link, t)
        temi = numpy.copy(t) # (link, t)
        for link_index, link in enumerate(links):
            temi[link_index] -= self.ltt[link](t[link_index])

        # Compute spacecraft positions at emission and reception
        try:
            logger.debug("Computing receiver position at reception time")
            xrec = numpy.empty((*t.shape, 3)) # (link, t, coord)
            for link_index, link in enumerate(links):
                receiver = int(str(link)[0])
                xrec[link_index, :, 0] = self.x[receiver](trec[link_index])
                xrec[link_index, :, 1] = self.y[receiver](trec[link_index])
                xrec[link_index, :, 2] = self.z[receiver](trec[link_index])
            logger.debug("Computing emitter position at emission time")
            xemi = numpy.empty((*t.shape, 3)) # (link, t, coord)
            for link_index, link in enumerate(links):
                emitter = int(str(link)[1])
                xemi[link_index, :, 0] = self.x[emitter](temi[link_index])
                xemi[link_index, :, 1] = self.y[emitter](temi[link_index])
                xemi[link_index, :, 2] = self.z[emitter](temi[link_index])
        except ValueError as error:
            logger.error("Missing orbit information")
            raise ValueError("missing orbit information, use longer orbit file or adjust sampling") from error

        # Compute link unit vector
        logger.debug("Computing link unit vector")
        n = (xrec - xemi) # (link, t, coord)
        n /= norm(n)[..., numpy.newaxis]

        # Compute equivalent emission and reception time at the Sun
        logger.debug("Computing equivalent reception time at the Sun")
        trec_sun = trec - dot(xrec, self.k) / c # (link, t)
        logger.debug("Computing equivalent emission time at the Sun")
        temi_sun = temi - dot(xemi, self.k) / c # (link, t)

        # Compute antenna pattern functions
        logger.debug("Computing antenna pattern functions")
        xiplus = dot(n, self.u)**2 - dot(n, self.v)**2 # (link, t)
        xicross = 2 * dot(n, self.u) * dot(n, self.v) # (link, t)

        # Compute hplus and hcross contributions
        logger.debug("Computing gravitational-wave response")
        termplus = numpy.empty_like(temi_sun) # (link, t)
        termcross = numpy.empty_like(trec_sun) # (link, t)
        for link_index in range(len(links)):
            termplus[link_index] = \
                self.compute_hplus(temi_sun[link_index]) - self.compute_hplus(trec_sun[link_index])
            termcross[link_index] = \
                self.compute_hcross(temi_sun[link_index]) - self.compute_hcross(trec_sun[link_index])
        return (termplus * xiplus + termcross * xicross) / (2 * (1 - dot(n, self.k)))

    def plot(self, t, output=None, gw_name='gravitational wave'):
        """Plot gravitational-wave response and strain.

        Args:
            t (array-like): TCB times [s]
            output (str or None): output file, None to show the plots
            gw_name (str): optional gravitational-wave source name
        """
        # Initialize the plot
        _, axes = matplotlib.pyplot.subplots(2, 1, figsize=(12, 8))
        axes[1].set_xlabel("Time [s]")
        axes[0].set_title(f"Strain and link response to {gw_name}")
        # Computing and plotting response
        logger.info("Plotting gravitational-wave response")
        axes[0].set_ylabel("Link response")
        response = self.compute_gw_response(self.LINKS, t)
        for link_index, link in enumerate(self.LINKS):
            axes[0].plot(t, response[link_index], label=link)
        # Computing and plotting strain
        logger.info("Plotting gravitational-wave strain")
        axes[1].set_ylabel("Gravitational-wave strain")
        hplus = self.compute_hplus(t)
        hcross = self.compute_hcross(t)
        axes[1].plot(t, hplus, label=r'$h_+$')
        axes[1].plot(t, hcross, label=r'$h_\times$')
        # Add legend and grid
        for axis in axes:
            axis.legend()
            axis.grid()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()


class ReadStrain(Strain):
    """Reads already-computed strain.

    Use this class if you wish to use your own waveform generator code but want to compute
    the link responses and and use the interface offered by this package.

    To honor the source's sampling parameters, the input data may be resampled using
    spline interpolation. If you do not wish to interpolate, make sure to instantiate
    the source with sampling parameters matching your data.

    Args:
        t (array-like): TCB times [s]
        hplus (array-like): +-polarized strain :math:`h_+` in the BCRS
        hcross (array-like): x-polarized strain :math:`h_\\times` in the BCRS
        strain_interp_order (int): strain spline-interpolation order [one of 1, 2, 3, 4, 5]
        **kwargs: all other args from :class:`lisagwresponse.GWResponse`
    """

    def __init__(self, t, hplus, hcross, strain_interp_order=5, **kwargs):
        super().__init__(**kwargs)
        self.strain_interp_order = int(strain_interp_order) #: int: Strain interpolation order.

        # Interpolate strain
        logger.info("Computing spline interpolation for gravitational-wave strain")
        self.hplus = self._interpolate_strain(t, hplus)
        """+-polarized strain :math:`h_+` interpolating function."""
        self.hcross = self._interpolate_strain(t, hcross)
        """x-polarized strain :math:`h_\\times` interpolating function."""

    def _interpolate_strain(self, t, data):
        """Interpolate strain data.

        Args:
            t (array-like): timestamps
            data (array-like): data to interpolate

        Returns:
            Interpolating spline function.
        """
        return InterpolatedUnivariateSpline(t, data, k=self.strain_interp_order, ext='zeros')

    def compute_hplus(self, t):
        return self.hplus(t)

    def compute_hcross(self, t):
        return self.hcross(t)


class GalacticBinary(Strain):
    """Represent a chirping galactic binary.

    Args:
        A (float): strain amplitude
        f (float): frequency [Hz]
        df (float): frequency derivative [Hz/s]
        phi0 (float): initial phase [rad]
        iota (float): inclination angle [rad]
        psi (float): polarization angle [rad]
        **kwargs: all other args from :class:`lisagwrespons.Strain`
    """

    def __init__(self, A, f, df=0, phi0=0, iota=0, psi=0, **kwargs):
        super().__init__(**kwargs)
        self.A = float(A)
        self.f = float(f)
        self.df = float(df)
        self.phi0 = float(phi0)
        self.iota = float(iota)
        self.psi = float(psi)

    def compute_strain_in_source_frame(self, t):
        """Compute strain in the source frame.

        Args:
            t (array-like): TCB times [s]

        Returns:
            Couple of arrays ``(hplus, hcross)``, each of shape ``(len(t))``.
        """
        logger.info("Compute gravitational-wave strain in the source frame")
        phase = pi * self.df * t**2 + 2 * pi * self.f * t - self.phi0
        hplus = -self.A * (1 + cos(self.iota)**2) * cos(phase)
        hcross = -2 * self.A * cos(self.iota) * sin(phase)
        return (hplus, hcross)

    def compute_hplus(self, t):
        logger.info("Compute +-polarized gravitational-wave strain in the BCRS")
        hplus_source, hcross_source = self.compute_strain_in_source_frame(t)
        return hplus_source * cos(2 * self.psi) - hcross_source * sin(2 * self.psi)

    def compute_hcross(self, t):
        logger.info("Compute x-polarized gravitational-wave strain in the BCRS")
        hplus_source, hcross_source = self.compute_strain_in_source_frame(t)
        return hplus_source * sin(2 * self.psi) + hcross_source * cos(2 * self.psi)


class StochasticPointSource(Strain):
    """Represent a point-like gravitational-wave stochastic source.

    This class generates random strain time series, following a given power spectral density.

    This class is used to represent independant pixels in a whole-sky
    :class:`lisagwresponse.StochasticBackground` instance.

    Args:
        generator (float or callable):
            strain power spectral density [/Hz], or a function ``(float, int) -> float`` of
            the sampling frequency [Hz] and size [samples] to generate strain time series
        strain_interp_order (int): strain spline-interpolation order [one of 1, 2, 3, 4, 5]
        **kwargs: all other args from :class:`lisagwresponse.Strain`
    """

    def __init__(self, generator, strain_interp_order=5, **kwargs):
        super().__init__(**kwargs)
        self.strain_interp_order = int(strain_interp_order) #: int: Strain interpolation order.

        if isinstance(generator, (int, float)):
            logger.info("Using a constant power spectral density of %s", generator)
            self.psd = float(generator)
            self.generator = white_generator(self.psd)
        elif callable(generator):
            logger.info("Using user-provided stochastic generator")
            self.psd = None
            self.generator = generator
        else:
            raise TypeError(f"invalid generator '{generator}', must be a scalar or a callable")

        # Strain needs to be interpolated at most 1 au / c before
        # and after; we take 120% left and right margins
        duration_margin = 1.2 * au / c
        t0_margin = self.t0 - duration_margin
        size_margin = self.size + 2 * int(duration_margin // self.dt)
        t = t0_margin + numpy.arange(size_margin) * self.dt

        # Interpolate stochastic strain
        logger.debug("Interpolating stochastic strain time series")
        self.hplus = InterpolatedUnivariateSpline(
            t, self.generator(self.fs, size_margin), k=self.strain_interp_order, ext='raise')
        """+-polarized strain :math:`h_+` interpolating function."""
        self.hcross = InterpolatedUnivariateSpline(
            t, self.generator(self.fs, size_margin), k=self.strain_interp_order, ext='raise')
        """x-polarized strain :math:`h_\times` interpolating function."""

    def compute_hplus(self, t):
        try:
            return self.hplus(t)
        except ValueError as error:
            logger.error("Missing stochastic strain (hplus) to interpolate at\n%s", t)
            raise ValueError("missing stochastic strain data (hplus) to interpolate") from error

    def compute_hcross(self, t):
        try:
            return self.hcross(t)
        except ValueError as error:
            logger.error("Missing stochastic strain (hcross) to interpolate at\n%s", t)
            raise ValueError("missing stochastic strain data (hcross) to interpolate") from error


class StochasticBackground(GWResponse):
    """Represent a whole-sky gravitational-wave stochastic background.

    The background is generated from a healpix-generated intensity sky map and a
    power spectral density. Each pixel in the sky is represented by a
    :class:`lisagwresponse.StochasticPointSource` instance, whose power is the product of
    the background PSD and the pixel intensity on the map.

    The response of each link is the superposition of the responses to each of the pixels
    (i.e., the stochastic point sources) making up the sky. Note that using a greater number
    of pixels increases the precision of the response but also the computational cost.

    .. admonition:: Memory usage

        Stochastic point sources for each pixel are created when initializating a stochastic
        background object, which triggers the generation of the random strain time series for
        the entire sky. For long simulations, we recommend you use ``optim=True`` to keep the
        memory usage to a minimum; point sources will not be created until you call
        :meth:`lisagwresponse.StochasticBackground.point_source`.

        Note that you will be limited to a single call to
        :meth:`lisagwresponse.StochasticBackground.compute_gw_response` in this case.

    Args:
        skymap: intensity sky map (from healpix)
        generator (float or callable):
            strain power spectral density [/Hz], or a function ``(float, int) -> float`` of
            the sampling frequency [Hz] and size [samples] to generate strain time series
        optim (bool):
            optimize for memory usage (release pixel point sources computing response).
        **kwargs: all other args from :class:`lisagwresponse.GWResponse`
    """

    def __init__(self, skymap, generator, optim=False, **kwargs):
        super().__init__(**kwargs)

        self.skymap = numpy.asarray(skymap)
        self.generator = generator
        self.npix = len(skymap) #: Number of sky pixels. Equivalently number of point sources.
        self.nside = healpy.npix2nside(self.npix) #: Healpix ``nside``.
        logger.info("Using a resolution of %s pixels (nside=%s)", self.npix, self.nside)

        self.optim = bool(optim) #: Whether memory optimization is enabled.
        if not self.optim:
            logger.info("Memory optimization disabled, building point sources")
            self.sources = []
            x, y, z, ltt = None, None, None, None
            for pixel in range(self.npix):
                source = self.point_source(pixel, x, y, z, ltt)
                if source is not None:
                    x, y, z, ltt = source.x, source.y, source.z, source.ltt
                    self.sources.append(source)
        else:
            logger.info("Memory optimization enabled, will generate point source on the fly")
            self.sources = None
            # Track if we call `compute_gw_response()` multiple times to issue a warning
            self.called_once = False

    def compute_gw_response(self, links, t):
        """Compute the response for a list of links.

        The response is computed as the sum of each pixel's response.

        If all links share the same time vector, use a 1-dim ``t`` argument of size ``N``.
        If different times must be used for each link, use a 2-dim ``t`` with shape
        ``(len(links), N)``.

        The link esponses are expressed as relative frequency fluctuations.

        .. warning:: Memory optimization

            If memory optimization is enabled (see :attr:`lisagwresponse.StochasticBackground.optim`),
            each call to this function will return a new stochastic point source with new
            strain time series, even for the same pixel.

            You will get inconsistent results (simulate a different sky) if you call this method
            multiple times.

        Args:
            links (array-like): link indices
            t (array-like): TCB times of shape ``(N)`` or ``(len(links), N)`` [s]

        Returns:
            Array of shape ``(len(links), N)`` containing the response of each link,
            as relative frequency fluctuations (strain units).
        """
        gw_response = 0
        if not self.optim:
            # Simply iterate over sources, and sum responses
            for source in self.sources:
                gw_response += source.compute_gw_response(links, t)
        else:
            # We use memory optimization, i.e., will destroy each source after it's been used
            # Check that we haven't called `compute_gw_response()` before
            if self.called_once:
                logger.warning("Multiple calls to `compute_gw_response()` when memory optimization "
                               "is enabled may lead to inconsistent results")
            else:
                self.called_once = True

            x, y, z, ltt = None, None, None, None
            # Loop over pixels and add contributions
            for pixel in range(self.npix):
                source = self.point_source(pixel, x, y, z, ltt)
                if source is not None:
                    gw_response += source.compute_gw_response(links, t)
                    # We rely on the first pixel to interpolate the orbits,
                    # and reuse this interpolation for all remaining pixels
                    x, y, z, ltt = source.x, source.y, source.z, source.ltt
                    del source
        # Return sum of pixel's response
        return gw_response

    def point_source(self, pixel, x=None, y=None, z=None, ltt=None):
        """Return stochastic point source corresponding to the desired pixel.

        The spectrum of the pixel is computed as the product of the sky modulation `skymap` at
        this pixel, and the stochastic background spectrum `generator`.

        .. warning:: Memory optimization

            If memory optimization is enabled (see :attr:`lisagwresponse.StochasticBackground.optim`),
            each call to this function will return a new stochastic point source with new
            strain time series, even for the same pixel.

            You will get inconsistent results (simulate a different sky) if you call this method
            multiple times.

        Args:
            pixel (int): pixel index
            x (callable): spacecraft x-position interpolating functions, overrides orbits [m]
            y (callable): spacecraft y-position interpolating functions, overrides orbits [m]
            z (callable): spacecraft z-position interpolating functions, overrides orbits [m]
            ltt (callable): light travel times interpolating functions, overrides orbits [s]
        """
        if pixel not in range(self.npix):
            raise ValueError(f"pixel '{pixel}' out of range")

        # Bypass black pixel
        if not self.skymap[pixel]:
            logger.info("Bypassing black pixel %s", pixel)
            return None

        logger.info("Initializing stochastic point source for pixel %s", pixel)

        # Theta and phi are colatitude and longitude, respectively (healpy conventions)
        # They are converted to beta and lambda, latitude and longitude (LDC conventions)
        gw_theta, gw_phi= healpy.pix2ang(self.nside, pixel)
        gw_beta, gw_lambda = pi / 2 - gw_theta, gw_phi

        # Compute the generator for the pixel
        if callable(self.generator):
            pixel_generator = lambda fs, size: self.skymap[pixel] * self.generator(fs, size)
        else:
            pixel_generator = self.skymap[pixel] * self.generator

        return StochasticPointSource(
            pixel_generator,
            gw_lambda=gw_lambda, gw_beta=gw_beta,
            orbits=self.orbits_path, orbit_interp_order=self.orbit_interp_order,
            x=x, y=y, z=z, ltt=ltt,
            dt=self.dt, size=self.size, t0=self.t0)

    def plot(self, t, output=None, gw_name='stochastic gravitational-wave background'):
        """Plot gravitational-wave response and intensity sky map.

        Args:
            t (array-like): TCB times [s]
            output (str or None): output file, None to show the plots
            gw_name (str): optional gravitational-wave source name
        """
        # Initialize the plot
        _, axes = matplotlib.pyplot.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [1, 1.5]})
        axes[0].set_xlabel("Time [s]")
        axes[0].set_title(f"Power sky map and link response to {gw_name}")
        # Computing and plotting response
        logger.info("Plotting gravitational-wave response")
        axes[0].set_ylabel("Link response")
        response = self.compute_gw_response(self.LINKS, t)
        for link_index, link in enumerate(self.LINKS):
            axes[0].plot(t, response[link_index], label=link)
        axes[0].legend()
        axes[0].grid()
        # Plotting sky map
        matplotlib.pyplot.axes(axes[1])
        logger.info("Plotting sky map of power spectral density")
        healpy.mollview(self.skymap, hold=True, title=None, unit='Power spectral density at 1 Hz')
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()
