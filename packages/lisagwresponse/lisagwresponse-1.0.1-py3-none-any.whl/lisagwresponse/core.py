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
from packaging.specifiers import SpecifierSet
from lisaconstants import c, au
from .utils import dot, norm
from .psd import white_generator

from .meta import __version__
from .meta import __author__


logger = logging.getLogger(__name__)


class GWResponse(abc.ABC):
    """Abstract base class which computes the response of each link to gravitational-wave signals."""

    SC = ['1', '2', '3']
    LINKS = ['12', '23', '31', '13', '32', '21']

    def __init__(self, dt=0.3, size=259200, t0=0):
        """Initialize a gravitational-wave response object.

        Parameters `dt`, `size`, and `t0` define simulation samling. They are used to generate
        a new gravitational-wave file; they are ignored when writing the glitch to an existing glitch file.

        Args:
            dt: simulation sampling period [s]
            size: simulation size [samples]
            t0: simulation initial time [s]
        """
        self.git_url = 'https://gitlab.in2p3.fr/lisa-simulation/gw-response'
        self.generator = self.__class__.__name__
        self.version = __version__
        logger.info("Initializing gravitational-wave response (lisagwresponse verion %s)", self.version)

        self.dt = float(dt)
        self.t0 = float(t0)
        self.size = int(size)
        self.fs = 1 / self.dt
        self.duration = self.size * self.dt
        self.t = self.t0 + numpy.arange(self.size) * self.dt

    @abc.abstractmethod
    def compute_gw_response(self, links, t):
        """Compute link response to gravitational-wave.

        The response to a gravitational signal must be expressed as a relative frequency fluctuations.

        Args:
            links: link index, or array of links [one of LINKS]
            t: array of TCB times [s]

        Returns:
            Array of shape (len(links), len(t)) containing the response of each link.
        """
        raise NotImplementedError

    def plot(self, output=None, gw_name='gravitational wave'):
        """Plot gravitational-wave response.

        Args:
            output: output file, None to show the plots
            gw_name: optional gravitational-wave source name
        """
        logger.info("Plotting gravitational-wave response")
        matplotlib.pyplot.figure(figsize=(12, 4))
        response = self.compute_gw_response(self.LINKS, self.t)
        for link_index, link in enumerate(self.LINKS):
            matplotlib.pyplot.plot(self.t, response[link_index], label=link)
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

    def write_metadata(self, hdf5, prefix=''):
        """Set all properties as HDF5 attributes on `object`.

        Try to store all variables as attributes. If it is too large or its type is not
        supported, try to store a string representation; if this fails, log a warning.

        Args:
            hdf5: an HDF5 file or dataset
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

    def write(self, path='gw.h5'):
        """Write the gravitational-wave response to a gravitational-wave (GW) file.

        If the GW file does not exist, it is created with the sampling parameters `dt`, `size`, and `t0`.
        If the GW file already exist, the gravitational-wve response is added to the each link dataset.

        The GW HDF5 file contains the following datasets,

            * time dataset `t` given as TCB times, of shape (N),
              with a single column (index 0), in s.

            * link datasets `l_12`, `l_23`, `l_31`, `l_13`, `l_32`, and `l_21`, of shape (N),
              with a single column (index 0), in fractional frequency fluctuations.

        When creating the glitch file, metadata are saved as attributes of the glitch HDF5 file,

            * `version`, git version identifier of lisagwresponse,
            * `git_url`, remote URL of the repository,
            * and any other local variable.

        When adding a GW response, we add attributes for each local variable, prefixed with 'gw<i>',
        where `i` is the index of the GW response in the file.

        Args:
            path: path to the generated gravitational-wave file
        """
        # Open GW file
        logger.info("Opening or creating gravitational-wave file '%s'", path)
        with  h5py.File(path, 'a') as hdf5:

            # Create time dataset if needed, and write some attributes, and create empty link datasets
            if 't' not in hdf5:
                logger.info("New gravitational-wave file, creating time dataset")
                t = self.t
                hdf5.create_dataset('t', data=t)
                logger.info("Setting global metadata")
                self.write_metadata(hdf5)
                hdf5.attrs['gw_count'] = 0
                for link in self.LINKS:
                    dname = f'l_{link}'
                    logger.info("Creating empty link dataset '%s'", dname)
                    hdf5.create_dataset(dname, data=numpy.zeros_like(t))
            else:
                t = hdf5['t'][:]

            # Setting metadata
            logger.info("Setting injection metadata")
            ngw = int(hdf5.attrs['gw_count'])
            hdf5.attrs['gw_count'] = ngw + 1
            self.write_metadata(hdf5, prefix=f'gw{ngw}_')

            # Add gravitational-wave response to link datasets
            response = self.compute_gw_response(self.LINKS, t)
            for link_index, link in enumerate(self.LINKS):
                dname = f'l_{link}'
                logger.info("Adding gravitational-wave response to link dataset '%s'", dname)
                hdf5[dname][:] += response[link_index]

        # Closing file
        logger.info("Closing gravitational-wave file '%s'", path)


class ReadGWResponse(GWResponse):
    """Reads a gravitational-wave response already computed.

    Use this class if the response for each link has already been computed.
    This class resamples the response if needed.
    """
    def __init__(self, t, y_12, y_23, y_31, y_13, y_32, y_21, interp_order=1, **kwargs):
        """Initialize an instance from time-series of pre-computed responses.

        Args:
            t: TCB times associated with read link responses
            y_12: sampled gravitational-wave response of link 12 [ffd]
            y_23: sampled gravitational-wave response of link 23 [ffd]
            y_31: sampled gravitational-wave response of link 31 [ffd]
            y_13: sampled gravitational-wave response of link 13 [ffd]
            y_32: sampled gravitational-wave response of link 32 [ffd]
            y_21: sampled gravitational-wave response of link 21 [ffd]
            interp_order: interpolation order to be used [one of 1, 2, 3, 4, 5]
            **kwargs: all other args from GWResponse
        """
        super().__init__(**kwargs)
        self.interp_order = int(interp_order)

        # Compute spline interpolation
        logger.info("Computing spline interpolation from time series")
        data = {'12': y_12, '23': y_23, '31': y_31, '13': y_13, '32': y_32, '21': y_21}
        self.interpolants = {
            link: InterpolatedUnivariateSpline(t, data[link], k=self.interp_order, ext='zeros')
            for link in self.LINKS
        }

    def compute_gw_response(self, links, t):
        if isinstance(links, str):
            return self.interpolants[links](t)
        responses = [self.compute_gw_response(t, link) for link in links]
        return numpy.stack(responses, axis=0)


class Strain(GWResponse, abc.ABC):
    """Abstract base which computes the link responses from gravitational-wave strains given in the BCRS."""
    def __init__(self,
                 orbits,
                 gw_beta,
                 gw_lambda,
                 orbit_interp_order=1,
                 x=None,
                 y=None,
                 z=None,
                 tt=None,
                 t0='orbits',
                 **kwargs):
        """Initialize an instance from a file orbit, and the source sky localization.

        Args:
            orbits: path to orbit file
            gw_beta: ecliptic latitude of gravitational-wave source [rad]
            gw_lambda: ecliptic longitude of gravitational-wave source [rad]
            orbit_interp_order: interpolation order to be used for orbits [one of 1, 2, 3, 4, 5]
            x: dictionary of spacecraft x-position functions, overrides orbits [m]
            y: dictionary of spacecraft y-position functions, overrides orbits [m]
            z: dictionary of spacecraft z-position functions, overrides orbits [m]
            tt: dictionary of functions for light travel times along each link, overrides orbits [s]
            t0: initial time [s], or 'orbits' to match that of the orbits
            **kwargs: all other args from GWResponse
        """
        # Forward numerical values of t0 to superclass
        if t0 != 'orbits':
            kwargs['t0'] = t0

        super().__init__(**kwargs)
        self.gw_beta = float(gw_beta)
        self.gw_lambda = float(gw_lambda)
        self.orbit_interp_order = int(orbit_interp_order)

        # Handle orbits
        if x is not None or y is not None or z is not None or tt is not None:
            logger.info("Using provided functions for orbits")
            self.set_orbits(x, y, z, tt)
        else:
            self.orbits_path = str(orbits)
            logger.info("Reading orbits from file '%s'", self.orbits_path)
            self.interpolate_orbits()
            if t0 == 'orbits':
                logger.debug("Reading initial time from orbit file '%s'", self.orbits_path)
                with h5py.File(self.orbits_path, 'r') as orbitf:
                    self.t0 = float(orbitf.attrs['tau0'])

        # Compute source-localization vector basis
        self.k = numpy.array([
            -cos(self.gw_beta) * cos(self.gw_lambda),
            -cos(self.gw_beta) * sin(self.gw_lambda),
            -sin(self.gw_beta),
        ])
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

    def interpolate_orbits(self):
        """Interpolate orbit data (spacecraft positions and light travel times).

        Also check that orbit file is valid and supported.

        Raises:
            ValueError if orbit file is not supported.
        """
        logger.info("Computing spline interpolation for orbits")
        with h5py.File(self.orbits_path, 'r') as orbitf:
            version = orbitf.attrs['version']
            logger.debug("Using orbit file version %s", version)
            if version in SpecifierSet('~= 1.0'):
                interpolate = lambda t, data: InterpolatedUnivariateSpline(
                    t, data, k=self.orbit_interp_order, ext='raise')

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
                self.tt = {
                    link: interpolate(orbitf['tcb/t'], orbitf[f'tcb/l_{link}']['tt'])
                    for link in self.LINKS
                }
            else:
                raise ValueError(f"unsupported orbit file version '{version}'")

    def set_orbits(self, x, y, z, tt):
        """Set orbit data from dictionaries (spacecraft positions and light travel times).

        Args:
            x: dictionary of spacecraft x-position functions, overrides orbits [m]
            y: dictionary of spacecraft y-position functions, overrides orbits [m]
            z: dictionary of spacecraft z-position functions, overrides orbits [m]
            tt: dictionary of functions for light travel times along each link, overrides orbits [s]
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
        self.tt = {
            link: tt[link] if callable(tt[link]) else lambda t, val=tt[link]: float(val)
            for link in self.LINKS
        }

    @abc.abstractmethod
    def compute_hplus(self, t):
        """Compute +-polarized gravitational-wave strain in the BCRS.

        Args:
            t: array of TCB times [s]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def compute_hcross(self, t):
        """Compute x-polarized gravitational-wave strain in the BCRS.

        Args:
            t: array of TCB times [s]
        """
        raise NotImplementedError

    def plot(self, output=None, gw_name='gravitational wave'):
        """Plot gravitational-wave strain and response.

        Args:
            output: output file, None to show the plots
            gw_name: optional gravitational-wave source name
        """
        # Initialize the plot
        _, axes = matplotlib.pyplot.subplots(2, 1, figsize=(12, 8))
        axes[1].set_xlabel("Time [s]")
        axes[0].set_title(f"Strain and link response to {gw_name}")
        # Computing and plotting response
        logger.info("Plotting gravitational-wave response")
        axes[0].set_ylabel("Link response")
        response = self.compute_gw_response(self.LINKS, self.t)
        for link_index, link in enumerate(self.LINKS):
            axes[0].plot(self.t, response[link_index], label=link)
        # Computing and plotting strain
        logger.info("Plotting gravitational-wave strain")
        axes[1].set_ylabel("Gravitational-wave strain")
        hplus = self.compute_hplus(self.t)
        hcross = self.compute_hcross(self.t)
        axes[1].plot(self.t, hplus, label=r'$h_+$')
        axes[1].plot(self.t, hcross, label=r'$h_\times$')
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

    def compute_gw_response(self, links, t):
        # pylint: disable=too-many-locals
        if isinstance(links, str):
            links = [links]
        logger.info("Computing gravitational-wave response for links %s", links)

        # Compute emission and reception time at spacecraft
        logger.debug("Computing emission time at spacecraft")
        trec = t # (t)
        temi = numpy.repeat(trec[numpy.newaxis], len(links), axis=0) # (link, t)
        for link_index, link in enumerate(links):
            temi[link_index] -= self.tt[link](t)

        # Compute spacecraft positions at emission and reception
        try:
            logger.debug("Computing receiver position at reception time")
            xrec = numpy.empty((len(links), len(t), 3)) # (link, t, coord)
            for link_index, link in enumerate(links):
                receiver = link[0]
                xrec[link_index, :, 0] = self.x[receiver](trec)
                xrec[link_index, :, 1] = self.y[receiver](trec)
                xrec[link_index, :, 2] = self.z[receiver](trec)
            logger.debug("Computing emitter position at emission time")
            xemi = numpy.empty((len(links), len(t), 3)) # (link, t, coord)
            for link_index, link in enumerate(links):
                emitter = link[1]
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
        trec_sun = trec[numpy.newaxis] - dot(xrec, self.k) / c # (link, t)
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


class ReadStrain(Strain):
    """Read gravitational-wave strain time series, and compute link response."""
    def __init__(self, t, hplus, hcross, strain_interp_order=1, **kwargs):
        """Initialize an instance from time series of gravitational strains in the BCRS.

        Args:
            t: TCB times associated with gravitational strain [s]
            hplus: sampled +-polarized strain in the BCRS
            hcross: sampled x-polarized strain in the BCRS
            strain_interp_order: interpolation order to be used for strain [one of 1, 2, 3, 4, 5]
            **kwargs: all other args from GWResponse
        """
        super().__init__(**kwargs)
        self.strain_interp_order = int(strain_interp_order)

        # Interpolate strain
        logger.info("Computing spline interpolation for gravitational-wave strain")
        self.hplus = self.interpolate_strain(t, hplus)
        self.hcross = self.interpolate_strain(t, hcross)

    def interpolate_strain(self, t, data):
        """Interpolate strain data.

        Args:
            data: array of data to interpolate

        Returns:
            Interpolated spline.
        """
        return InterpolatedUnivariateSpline(t, data, k=self.strain_interp_order, ext='zeros')

    def compute_hplus(self, t):
        return self.hplus(t)

    def compute_hcross(self, t):
        return self.hcross(t)


class GalacticBinary(Strain):
    """Generate gravitational-wave response from a chirping galactic binary.

    The gravitational-wave strain of a galactic binary is given, in the source frame, by

        h+_source = -A [1 + cos^2(iota)] * cos(π df t^2 + 2πf t - phi0)
        hx_source = -2 A cos(iota) * sin(π df t^2 + 2πf t - phi0)

    and in the BCRS, at the Sun,

        h+ = h+_source cos(2 psi) - hx_source sin(2 psi)
        hx = h+_source sin(2 psi) + hx_source cos(2 psi)

    """
    def __init__(self, A, f, df=0, phi0=0, iota=0, psi=0, **kwargs):
        """Initialize an gravitational-wave from a chirping binary.

        Args:
            A: gravitational-wave strain amplitude
            f: signal frequency [Hz]
            df: signal frequency time derivative [Hz/s]
            phi0: initial phase [rad]
            iota: inclination angle [rad]
            psi: polarization angle [rad]
            **kwargs: all other args from Strain
        """
        super().__init__(**kwargs)
        self.A = float(A)
        self.f = float(f)
        self.df = float(df)
        self.phi0 = float(phi0)
        self.iota = float(iota)
        self.psi = float(psi)

    def compute_strain_in_source_frame(self, t):
        """Compute gravitational-wave strain in the source frame.

        Args:
            t: array of TCB times [s]

        Returns:
            Couple (hplus, hcross).
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
    """Generate response for a point-like gravitational-wave stochastic source.

    The +/x-polarized strains are white Gaussian noise.
    """
    def __init__(self, generator, **kwargs):
        """Initialize a point-like gravitational-wave stochastic source.

        Args:
            generator: either the strain power spectral density [/Hz], or a function of (fs, size)
                the sampling frequency `fs` [Hz] and the number of samples `size` to generate the
                stochastic strain
            **kwargs: all other args from Strain
        """
        super().__init__(**kwargs)

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
            t, self.generator(self.fs, size_margin), k=5, ext='raise')
        self.hcross = InterpolatedUnivariateSpline(
            t, self.generator(self.fs, size_margin), k=5, ext='raise')

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
    """Generate response for a whole-sky gravitational-wave stochastic background.

    The background is generated from a Healpix-generated [1] sky map of power spectral density,
    using one stochastic point source per pixel.

        [1] https://healpix.jpl.nasa.gov/
    """
    def __init__(self, skymap, generator, orbits, orbit_interp_order=1, optim=False, **kwargs):
        """Initialize a gravitational-wave stochastic background source.

        Args:
            skymap: sky map of power spectral densities (from healpix) [/Hz]
            generator: either the strain power spectral density [/Hz], or a function of (fs, size)
                the sampling frequency `fs` [Hz] and the number of samples `size` to generate the
                stochastic strain
            orbits: path to orbit file
            orbit_interp_order: interpolation order to be used for orbits [one of 1, 2, 3, 4, 5]
            optim: optimize for memory usage (release pixel point sources computing response).
                Warning: do not call `compute_gw_response()` multiple times when memory optimization
                is enabled, at the risk of loosing sky correlation between calls. Defaults to False.
            **kwargs: all other args from GWResponse
        """
        super().__init__(**kwargs)

        self.orbits_path = str(orbits)
        self.orbit_interp_order = int(orbit_interp_order)

        self.skymap = numpy.array(skymap)
        self.generator = generator
        self.npix = len(skymap)
        self.nside = healpy.npix2nside(self.npix)
        logger.info("Using a resolution of %s pixels (nside=%s)", self.npix, self.nside)

        self.optim = bool(optim)
        if not self.optim:
            logger.info("Memory optimization disabled, building point sources")
            self.sources = []
            x, y, z, tt = None, None, None, None
            for pixel in range(self.npix):
                source = self.point_source(pixel, x, y, z, tt)
                if source is not None:
                    x, y, z, tt = source.x, source.y, source.z, source.tt
                    self.sources.append(source)
        else:
            logger.info("Memory optimization enabled, will generate point source on the fly")
            self.sources = None
            # Track if we call `compute_gw_response()` multiple times to issue a warning
            self.called_once = False

    def compute_gw_response(self, links, t):
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

            x, y, z, tt = None, None, None, None
            # Loop over pixels and add contributions
            for pixel in range(self.npix):
                source = self.point_source(pixel, x, y, z, tt)
                if source is not None:
                    gw_response += source.compute_gw_response(links, t)
                    # We rely on the first pixel to interpolate the orbits,
                    # and reuse this interpolation for all remaining pixels
                    x, y, z, tt = source.x, source.y, source.z, source.tt
                    del source
        # Return sum of pixel's response
        return gw_response

    def point_source(self, pixel, x=None, y=None, z=None, tt=None):
        """Return stochastic point source corresponding to the desired pixel.

        The spectrum of the pixel is computed as the product of the sky modulation `skymap` at
        this pixel, and the stochastic background spectrum `generator`.

        Args:
            pixel: pixel index
            x: dictionary of spacecraft x-position functions, overrides orbits [m]
            y: dictionary of spacecraft y-position functions, overrides orbits [m]
            z: dictionary of spacecraft z-position functions, overrides orbits [m]
            tt: dictionary of functions for light travel times along each link, overrides orbits [s]
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
            x=x, y=y, z=z, tt=tt,
            dt=self.dt, size=self.size, t0=self.t0)

    def plot(self, output=None, gw_name='stochastic gravitational-wave background'):
        """Plot gravitational-wave response and sky map of power spectral density.

        Args:
            output: output file, None to show the plots
            gw_name: optional gravitational-wave source name
        """
        # Initialize the plot
        t = self.t0 + numpy.arange(self.size, dtype=numpy.float64) * self.dt
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
