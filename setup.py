#!/usr/bin/env python

import os
import setuptools
from numpy.distutils.core import setup


readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation can be generated with Sphinx"""

history = open('HISTORY.rst').read().replace('.. :changelog:', '')

required = ["numpy"]
tests_require=['pytest>=2.3'] #for testing

PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration("fastell4py", parent_package, top_path,
                           namespace_packages = ['fastell4py'],
                           version='0.1.0',
                           author  = 'Joel Akeret',
                           author_email="jakeret@phys.ethz.ch",
                           description='Wrapper for the fastell fortran code',
                           url='http://www.astro.ethz.ch/refregier/research/index',
                           long_description=readme + '\n\n' + doclink + '\n\n' + history,)

    config.add_extension('_fastell',
                         sources=['src/fastell.f', 'fastell.pyf'] ,
#                             include_dirs = include_dirs,
#                             library_dirs = library_dirs,
#                             libraries = libraries,
#                             extra_f90_compile_args=extra_f90_compile_args,
#                             extra_link_args=extra_link_args
                            )

    return config




setup(configuration=configuration,
        packages=setuptools.find_packages(PACKAGE_PATH, "test"),
        include_package_data = True,
        platforms = ["any"],
        install_requires=[required],
        package_data={"": ["LICENSE"]},
        license='Proprietary',
        zip_safe = False,
        classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        'License :: Other/Proprietary License',
        "Programming Language :: Python",
    ])



