#!/usr/bin/env python
import glob
import os

from setuptools import setup, Extension, find_packages


BOOST_DIR = os.environ.get('BOOST_DIR', r'C:\SDK\\boost_1_56_0')
PREPAR3D_SDK_DIR = os.environ.get('PREPAR3D_SDK_DIR', r'C:\Program Files (x86)\\Lockheed Martin\\Prepar3D v2 SDK 2.5.12943.0')

def get_boost_lib_name(name):
    return 'boost_%s-vc100-mt-1_56' % name

simconnect_module = Extension('prepar3d._internal.simconnect',
                              sources=glob.glob('src/simconnect/*.cpp')
                                + glob.glob('src/util/*.cpp'),
                              include_dirs=['src/util/',
                                            BOOST_DIR,
                                            os.path.join(PREPAR3D_SDK_DIR, 'Utilities', 'SimConnect SDK', 'Inc')],
                              library_dirs=[os.path.join(BOOST_DIR, 'stage', 'lib'),
                                            os.path.join(PREPAR3D_SDK_DIR, 'Utilities', 'SimConnect SDK', 'lib')],
                              libraries=[get_boost_lib_name('python'),
                                         get_boost_lib_name('regex'),
                                         get_boost_lib_name('system'),
                                         get_boost_lib_name('filesystem'),
                                         'SimConnect', 'Ole32', 'odbccp32', 'shell32', 'user32', 'AdvAPI32' ],
                              extra_compile_args=['/EHsc']
                              )


if __name__ == '__main__':
    setup(name='prepar3d',
          version='0.1.0',
          author='Erik Tuerke',
          packages=find_packages(),
          ext_modules=[simconnect_module],
          zip_safe=False,
          data_files=[('prepar3d/_internal', glob.glob('lib/*.dll'))]
          )
