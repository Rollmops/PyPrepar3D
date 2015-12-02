import glob
import os

from setuptools import setup, Extension, find_packages
from prepar3d import __version__, __author__

BOOST_DIR = os.environ.get('BOOST_DIR', r'C:\SDK\boost_1_59_0')
PREPAR3D_SDK_DIR = os.environ.get('PREPAR3D_SDK_DIR', r'C:\SDK\Prepar3D v3 SDK')

def get_boost_lib_name(name):
    return 'boost_%s-vc120-mt-1_59' % name

simconnect_module = Extension('prepar3d._internal.simconnect',
                              sources=glob.glob('src/simconnect/*.cpp')
                                + glob.glob('src/util/*.cpp'),
                              include_dirs=['src/util/',
                                            BOOST_DIR,
                                            os.path.join(PREPAR3D_SDK_DIR, 'Utilities', 'SimConnect SDK', 'Inc')],
                              library_dirs=[os.path.join(BOOST_DIR, 'lib32-msvc-12.0'),
                                            os.path.join(PREPAR3D_SDK_DIR, 'Utilities', 'SimConnect SDK', 'lib')],
                              libraries=[get_boost_lib_name('python'),
                                         get_boost_lib_name('regex'),
                                         get_boost_lib_name('system'),
                                         get_boost_lib_name('filesystem'),
                                         'SimConnect', 'Ole32', 'odbccp32', 'shell32', 'user32', 'AdvAPI32' ],
                              extra_compile_args=[]
                              )


setup(name='prepar3d',
      version=__version__,
      author=__author__,
      packages=find_packages(),
      ext_modules=[simconnect_module],
      zip_safe=False,
      data_files=[('prepar3d/_internal', glob.glob('lib/*.dll'))]
      )
