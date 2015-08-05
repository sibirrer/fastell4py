#! /usr/bin/env python

# Copyright (C) 2015 ETH Zurich, Institute for Astronomy

# System imports
from __future__ import print_function, division, absolute_import, unicode_literals


# External modules
import numpy as np

# fastell4py imports

from fastell4py import _fastell

#axis ratio (<=1; <0 means: end)
#arat = 0.2
#q,gam,s2 = 0.2, 1, 0.001

#x1,x2, = 0.9, 0.9

#defl = np.empty((2))
#defl3 = np.empty((2))
#phi = 0
#magmx = np.empty((2,2))

#fastell.fastelldefl(x1,x2,q,gam,arat,s2,defl3)
#print('fastell Defl.= ', defl3)

#fastell.fastellmag(x1,x2,q,gam,arat,s2,defl, magmx)
#print('fastell mag routine: Defl.= ',defl)
#print('and Magmx(11,22,12) = ',magmx[0,0])
#print(magmx[0,1],magmx[1,0], magmx[1,1])

#fastell.ellipphi(x1,x2,q,gam,arat,s2,phi)
#print('slow Phi= ',phi)


def fastelldefl(x1,x2,q,gam,arat,s2):
    """

    :param x1:
    :param x2:
    :param q:
    :param gam:
    :param arat:
    :param s2:
    :return:
    """
    if isinstance(x1, int) or isinstance(x1, float):
        defl = np.empty((2))
        _fastell.fastelldefl(x1, x2, q, gam, arat, s2, defl)
        return defl[0], defl[1]
    else:
        n = len(x1)
        defl1 = np.empty(n)
        defl2 = np.empty(n)
        _fastell.fastelldefl_array(x1, x2, q, gam, arat, s2, defl1, defl2, n)
        alpha1 = defl1
        alpha2 = defl2
        return alpha1, alpha2


def fastellmag(x1, x2, q, gam, arat, s2):
    """

    :param x1:
    :param x2:
    :param q:
    :param gam:
    :param arat:
    :param s2:
    :return:
    """
    if isinstance(x1, int) or isinstance(x1, float):
        n = 1
    else:
        n = len(x1)
    defl1 = np.empty(n)
    defl2 = np.empty(n)
    magmx_xx = np.empty(n)
    magmx_xy = np.empty(n)
    magmx_yy = np.empty(n)
    _fastell.fastellmag_array(x1, x2, q, gam, arat, s2, defl1, defl2, magmx_xx, magmx_xy, magmx_yy, n)
    alpha1 = defl1
    alpha2 = defl2
    f_xx = magmx_xx
    f_xy = magmx_xy
    f_yy = magmx_yy
    return alpha1, alpha2, f_xx, f_yy, f_xy


def ellipphi(x1,x2,q,gam,arat,s2):
    """

    :param x1:
    :param x2:
    :param q:
    :param gam:
    :param arat:
    :param s2:
    :return:
    """
    if isinstance(x1, int) or isinstance(x1, float):
        n = 1
    else:
        n = len(x1)
    phi = np.empty(n)
    _fastell.ellipphi_array(x1, x2, q, gam, arat, s2, phi, n)
    return phi