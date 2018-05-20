__author__ = 'sibirrer'

import numpy as np
from fastell4py import fastell4py

import pytest

class TestFastell4py(object):
    """
    tests the python wrapper
    """
    def setup(self):
        pass

    def test_ellipphi(self):
        x1 = np.array([1,2,3])
        x2 = np.array([3,2,1])
        q = 0.9
        gam = 0.5
        arat = 0.9
        s = 0.01

        phi = fastell4py.ellipphi(x1, x2, q, gam, arat, s)
        assert phi[0] == 4.8517243810676121

        x1 = 1.
        x2 = 3.
        phi_new = fastell4py.ellipphi(x1, x2, q, gam, arat, s)
        assert phi_new == phi[0]

    def test_fastelldefl(self):
        x1 = np.array([1,2,3])
        x2 = np.array([3,2,1])
        q = 0.9
        gam = 0.5
        arat = 0.9
        s = 0.01
        alpha1, alpha2 = fastell4py.fastelldefl(x1, x2, q, gam, arat, s)
        print(alpha1, alpha2, 'alpha1, alpha2')
        assert alpha1[0] == 0.49802187030058409
        assert alpha2[0] == 1.604771432322617

        x1 = 1.
        x2 = 3.
        alpha1_new, alpha2_new = fastell4py.fastelldefl(x1, x2, q, gam, arat, s)
        assert alpha1_new == alpha1[0]
        assert alpha2_new == alpha2[0]

    def test_fastellmag(self):
        x1 = np.array([1,2,3])
        x2 = np.array([3,2,1])
        q = 0.9
        gam = 0.5
        arat = 0.9
        s = 0.01

        alpha1, alpha2, f_xx, f_yy, f_xy = fastell4py.fastellmag(x1, x2, q, gam, arat, s)
        print(alpha1, alpha2, f_xx, f_yy, f_xy, 'alpha1, alpha2, f_xx, f_yy, f_xy')
        assert alpha1[0] == 0.49802187030058409
        assert alpha2[0] == 1.604771432322617
        assert f_xx[0] == 0.45275802445408392
        assert f_xy[0] == -0.14571529551967699
        assert f_yy[0] == 0.064276065829922582
        x1 = 1.
        x2 = 3.
        alpha1_new, alpha2_new, f_xx_new, f_yy_new, f_xy_new = fastell4py.fastellmag(x1, x2, q, gam, arat, s)
        assert alpha1_new == alpha1[0]
        assert alpha2_new == alpha2[0]
        assert f_xx_new == f_xx[0]
        assert f_xy_new == f_xy[0]
        assert f_yy_new == f_yy[0]

if __name__ == '__main__':
   pytest.main()