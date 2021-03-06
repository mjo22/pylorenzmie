#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pylorenzmie.theory import LorenzMie
from pylorenzmie.theory import GeneralizedLorenzMie
import numpy as np
try:
    import cupy as cp
    cp.cuda.Device()
    if 'Cuda' not in str(GeneralizedLorenzMie):
        raise Exception()
    from pylorenzmie.theory import cuholo as cuh
except Exception:
    cp = None
try:
    import numba as nb
    from pylorenzmie.theory import fastholo as fh
except Exception:
    nb = None


class LMHologram(LorenzMie):

    '''
    A class that computes in-line holograms of spheres

    ...

    Attributes
    ----------
    alpha : float, optional
        weight of scattered field in superposition

    Methods
    -------
    hologram() : numpy.ndarray
        Computed hologram of sphere
    '''

    def __init__(self,
                 alpha=1.,
                 *args, **kwargs):
        super(LMHologram, self).__init__(*args, **kwargs)
        self.alpha = alpha

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        self._alpha = float(alpha)

    @property
    def properties(self):
        p = {}
        p.update(self.particle.properties)
        p.update(self.instrument.properties)
        p.update({'alpha': self.alpha})
        return p

    @properties.setter
    def properties(self, properties):
        if type(properties) is dict:
            for prop in properties.keys():
                if hasattr(self.particle, prop):
                    setattr(self.particle, prop, properties[prop])
                elif hasattr(self.instrument, prop):
                    setattr(self.instrument, prop, properties[prop])
                elif hasattr(self, prop):
                    setattr(self, prop, properties[prop])
                else:
                    msg = "{} is not a property of LMHologram"
                    raise ValueError(msg.format(prop))

    def hologram(self, return_gpu=False):
        '''Return hologram of sphere

        Returns
        -------
        hologram : numpy.ndarray
            Computed hologram.
        '''
        if self.using_cuda:
            field = self.field()
            hologram = self.holo
            alpha = self._flt(self.alpha)
            Ex, Ey, Ez = field
            kernel = cuh.cuhologram if self.double_precision else cuh.cuhologramf
            kernel((self.blockspergrid,), (self.threadsperblock,),
                   (Ex, Ey, Ez, alpha, hologram.size, hologram))
            if return_gpu is False:
                hologram = hologram.get()
        elif self.using_numba:
            field = self.field()
            hologram = self.holo
            fh.fasthologram(field, self.alpha, hologram.size, hologram)
        else:
            field = self.alpha * self.field()
            field[0, :] += 1.
            hologram = np.sum(np.real(field * np.conj(field)), axis=0)
        return hologram


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from Instrument import coordinates
    from time import time

    shape = [201, 201]
    h = LMHologram(coordinates=coordinates(shape))
    h.particle.r_p = [125, 75, 100]
    h.particle.a_p = 0.9
    h.particle.n_p = 1.45
    h.instrument.wavelength = 0.447
    h.hologram()
    start = time()
    hol = h.hologram()
    print("Time to calculate {}".format(time() - start))
    plt.imshow(hol.reshape(shape), cmap='gray')
    plt.show()
