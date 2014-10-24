#!/usr/bin/env python
# monkey-patch for parallel compilation
def parallelCCompile(self, sources, output_dir=None, macros=None, include_dirs=None, debug=0, extra_preargs=None, extra_postargs=None, depends=None):
    # those lines are copied from distutils.ccompiler.CCompiler directly
    macros, objects, extra_postargs, pp_opts, build = self._setup_compile(output_dir, macros, include_dirs, sources, depends, extra_postargs)
    cc_args = self._get_cc_args(pp_opts, debug, extra_preargs)
    # parallel code
    N=1 # number of parallel compilations
    import multiprocessing.pool
    def _single_compile(obj):
        try: src, ext = build[obj]
        except KeyError: return
        self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
    # convert to list, imap is evaluated on-demand
    list(multiprocessing.pool.ThreadPool(N).imap(_single_compile,objects))
    return objects
import distutils.msvccompiler
# distutils.msvc9compiler.MSVCCompiler.compile=parallelCCompile

import glob
import os
from setuptools import setup, Extension, find_packages
import glob

BOOST_DIR=os.environ.get('BOOST_DIR', r'C:\SDK\\boost_1_56_0')
PREPAR3D_SDK_DIR=os.environ.get('PREPAR3D_SDK_DIR', r'C:\Program Files (x86)\Lockheed Martin\Prepar3D v2 SDK 2.4.11570.0')

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
                                         get_boost_lib_name('thread'),
                                         'SimConnect', 'Ole32', 'odbccp32', 'shell32', 'user32', 'AdvAPI32' ],
                              extra_compile_args=['/EHsc']
                              )

setup(name='prepar3d',
      version='0.1.0',
      author='Erik Tuerke',
      packages=find_packages(),
      ext_modules = [simconnect_module],
      zip_safe=False,
      data_files=[('prepar3d/_internal',['lib/boost_python-vc100-mt-1_56.dll'])]
      )