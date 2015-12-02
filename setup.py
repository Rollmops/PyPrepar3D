import glob
import os

from setuptools import setup, find_packages
from prepar3d import __version__, __author__

setup(name='prepar3d',
      version=__version__,
      author=__author__,
      packages=find_packages(),
      zip_safe=False
      )
