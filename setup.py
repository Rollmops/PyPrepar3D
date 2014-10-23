#!/usr/bin/env python
import glob
import os
from setuptools import setup, Extension, find_packages
import glob

BOOST_DIR=os.environ.get('BOOST_DIR', 'C:\\SDK\\boost_1_56_0')

def get_boost_lib_name(name):
    return 'boost_%s-vc100-mt-1_56' % name

simconnect_module = Extension('prepar3d._simconnect',
                              sources=glob.glob('src/simconnect/*.cpp'),
                            include_dirs=[BOOST_DIR, 'inc'],
                              library_dirs=['lib'],
                              libraries=[get_boost_lib_name('python'),
                                         get_boost_lib_name('regex'),
                                         get_boost_lib_name('system'), 
                                         get_boost_lib_name('filesystem'),
                                         'SimConnect', 'Ole32', 'odbccp32', 'shell32', 'user32', 'AdvAPI32' ],
                              extra_compile_args=['/EHsc', '/MP4']
                              )

setup(name='prepar3d',
      version='0.1.0',
      author='Erik Tuerke',
      packages=find_packages(),
      ext_modules = [simconnect_module],
      zip_safe=False,
      data_files=[('prepar3d',['lib/boost_python-vc-mt-1_56.dll'])]
      )