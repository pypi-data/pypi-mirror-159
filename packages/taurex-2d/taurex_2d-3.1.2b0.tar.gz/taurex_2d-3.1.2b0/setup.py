#!/usr/bin/env python
from setuptools import find_packages
from numpy.distutils.core import setup

packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_2d', ]

requires = []

install_requires = ['taurex',
                    'numpy',
                    'numba',
                    'astropy',
                    'pandas',
                    'numexpr',
                    'tabulate', ]

console_scripts = ['taurex-plot-2d=taurex_2d.plot.plotter:main [Plot]']

entry_points = {'console_scripts': console_scripts,
                'taurex.plugins': '2D = taurex_2d'}

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
]

# Handle versioning
version = '3.1.2-beta'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='taurex_2d',
      author='Aurélien Falco',
      author_email='aurelien.falco@u-bordeaux.fr',
      license="BSD",
      version=version,
      description='TauREx 2D plugin',
      classifiers=classifiers,
      packages=packages,
      long_description=long_description,
      url='https://forge.oasu.u-bordeaux.fr/falco/taurex_2d.git',
      long_description_content_type="text/markdown",
      keywords = ['exoplanet','retrieval','taurex','taurex3','taurex2d','atmosphere','atmospheric'],
      include_package_data=True,
      entry_points=entry_points,
      provides=provides,
      requires=requires,
      install_requires=install_requires,
      extras_require={
        'Plot':  ["matplotlib"], },
      )
