=============================
Wrapper for fastell
=============================

Wrapper for the fastell fortran code

for use, have a look at the testing routines in test.test_fastell4py.py


Features
--------

single value and numpy array handling for evaluation deflection angle, grandients and potentials


From the original code of Rennan Barkana:

Code for a family of elliptical density gravitational lens models.
Developed by Rennan Barkana (barkana@wise.tau.ac.il), Fall 1997-1998.
Available at http://wise-obs.tau.ac.il/~barkana/codes.html. Comments
are welcome.

FASTELL is a code to calculate quickly and accurately the lensing
deflection and magnification matrix for the SPEMD lens galaxy model.
The SPEMD consists of a softened power law radial distribution with
elliptical isodensity contours. FASTELL is NOT restricted to
small ellipticity.

The method is described in a paper, also available at the above Web
page. The paper builds on the work of T. Schramm, Astron. Astrophys.
231, 19 (1990), who expressed the x and y components of the
deflection angle due to an elliptical mass distribution as integrals.
We simplify these integrals and then approximate the integrands in
order to be able to integrate analytically. We also take derivatives
in order to calculate the magnification matrix.

In addition to the FASTELL routines we include here the numerically
integrated 'slow' version, as well as the calculation of the
potential phi (needed for the gravitational time delay), which
must be integrated numerically and cannot be speeded up with
our methods.

The slow, numerically integrated version consists of the
subroutines ellipmag (deflections and magnification matrix)
and ellipdefl (deflections only). Note: these routines may not
be robust, i.e. their accuracy may be low for some parameter
values. The fast routines below, however, have been verified to be
extremely accurate over a wide range of parameter values.

The numerically integrated calculation of the gravitational
potential is ellipphi. It should be accurate over a wide
range of parameter values, thanks to a fix to an accuracy problem
pointed out by David Rusin. [Feb. 2000]

The fast routines are fastellmag (deflections and magnification
matrix) and fastelldefl (deflections only). They run fastest
with aggressive optimization, e.g. f77 -O5 fastell.f

In the routines below, we denote the projected mass density in
units of the critical density as kappa(x1,x2)=q [u2+s2]^(-gam),
where u2=[x1^2+x2^2/(arat^2)] and arat is the axis ratio. Note
that in section 2 of the paper this same kappa is denoted
[(u2+s^2)/E^2]^(eta/2-1) in terms of the same quantity u2.

The routines do not really calculate the magnification matrix,
they calculate the Jacobian matrix J_{ij}=d a_i/d x_j, where
a_i is the deflection. The magnification matrix can then be
obtained as the inverse matrix of delta_{ij}-J_{ij}.

A simple example program is included.


Installation
--------
The installation requires a fortran compiler installed.
 >>> cd projectrepo
 >>> python setup.py install --user
 
There might be a confusion with different compilers. Make sure that the path in the .config (.profile) file points at
the right compiler.
