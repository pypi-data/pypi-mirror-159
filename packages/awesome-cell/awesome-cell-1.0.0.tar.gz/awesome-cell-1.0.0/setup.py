"""Setup file for the PARC quantum diagnostic package.

Copyright 2022, Palo Alto Research Center
"""

from setuptools import setup, find_packages


setup(name="awesome-cell",
      version="1.0.0",
      author="The Awesome Possums",
      author_email="possums@parc.com",
      entry_points={
          'console_scripts': ['awesome-segment=awesome_cell.segment:main'],
      },
      install_requires=['numpy',
                        'scipy',
                        'scikit-image',
                        'opencv-python'],  # Should match 'requirements.txt'
      packages=find_packages())
