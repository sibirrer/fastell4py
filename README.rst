=============================
Wrapper for fastell
=============================

Wrapper for the fastell fortran code

for use, have a look at the testing routines in test.test_fastell4py.py


Features
--------

single value and numpy array handling for evaluation deflection angle, grandients and potentials


From the original code of Rennan Barkana:

c     Code for a family of elliptical density gravitational lens models.
c     Developed by Rennan Barkana (barkana@wise.tau.ac.il), Fall 1997-1998.
c     Available at http://wise-obs.tau.ac.il/~barkana/codes.html. Comments 
c     are welcome.
c
c     FASTELL is a code to calculate quickly and accurately the lensing 
c     deflection and magnification matrix for the SPEMD lens galaxy model.
c     The SPEMD consists of a softened power law radial distribution with 
c     elliptical isodensity contours. FASTELL is NOT restricted to 
c     small ellipticity.
c
c     The method is described in a paper, also available at the above Web
c     page. The paper builds on the work of T. Schramm, Astron. Astrophys.
c     231, 19 (1990), who expressed the x and y components of the 
c     deflection angle due to an elliptical mass distribution as integrals.
c     We simplify these integrals and then approximate the integrands in 
c     order to be able to integrate analytically. We also take derivatives 
c     in order to calculate the magnification matrix.
c
c     In addition to the FASTELL routines we include here the numerically
c     integrated 'slow' version, as well as the calculation of the 
c     potential phi (needed for the gravitational time delay), which
c     must be integrated numerically and cannot be speeded up with 
c     our methods. 
c     
c     The slow, numerically integrated version consists of the
c     subroutines ellipmag (deflections and magnification matrix)
c     and ellipdefl (deflections only). Note: these routines may not
c     be robust, i.e. their accuracy may be low for some parameter
c     values. The fast routines below, however, have been verified to be
c     extremely accurate over a wide range of parameter values.
c
c     The numerically integrated calculation of the gravitational
c     potential is ellipphi. It should be accurate over a wide
c     range of parameter values, thanks to a fix to an accuracy problem 
c     pointed out by David Rusin. [Feb. 2000]
c
c     The fast routines are fastellmag (deflections and magnification 
c     matrix) and fastelldefl (deflections only). They run fastest
c     with aggressive optimization, e.g. f77 -O5 fastell.f 
c
c     In the routines below, we denote the projected mass density in 
c     units of the critical density as kappa(x1,x2)=q [u2+s2]^(-gam), 
c     where u2=[x1^2+x2^2/(arat^2)] and arat is the axis ratio. Note
c     that in section 2 of the paper this same kappa is denoted
c     [(u2+s^2)/E^2]^(eta/2-1) in terms of the same quantity u2.
c
c     The routines do not really calculate the magnification matrix, 
c     they calculate the Jacobian matrix J_{ij}=d a_i/d x_j, where 
c     a_i is the deflection. The magnification matrix can then be 
c     obtained as the inverse matrix of delta_{ij}-J_{ij}. 
c
c     A simple example program is included.


Installation
--------
c     The installation requires a fortran compiler installed.
c     >>> cd projectrepo
c     >>> python setup.py install --user