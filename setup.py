#!/usr/bin/env python
from setuptools import setup, Extension
import os

BOOST_DIR=os.environ.get('BOOST_DIR', 'C:\\SDK\\boost_1_56_0')
SIMCONNECT_DIR=os.environ.get('SIMCONNECT_DIR', 'C:\\SDK\Prepar3D v2 SDK 2.4.11570.0\Utilities\SimConnect SDK')

def get_boost_lib_name(name):
    return 'boost_%s-vc100-mt-1_56' % name

simconnect_module = Extension('simconnect',
                              sources=['src/module_simconnect.cpp'],
                              include_dirs=[BOOST_DIR, os.path.join(SIMCONNECT_DIR, 'Inc')],
                              library_dirs=['lib', os.path.join(SIMCONNECT_DIR, 'lib')],
                              libraries=[get_boost_lib_name('python'),
                                         get_boost_lib_name('regex'),
                                         get_boost_lib_name('system'), 
                                         get_boost_lib_name('filesystem'),
                                         'SimConnect', 'Ole32', 'odbccp32', 'shell32', 'user32', 'AdvAPI32' ]
                              )

setup(name='prepy3d',
      version='0.1.0',
      author='Erik Tuerke',
      ext_modules = [simconnect_module],
      zip_safe=False,
      data_files=[os.path.join('lib', 'boost_python-vc-mt-1_56.dll')]
      )