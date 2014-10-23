def __bootstrap__():
    global __bootstrap__, __loader__, __file__
    import sys, pkg_resources, imp
    __file__ = pkg_resources.resource_filename('prepar3d._simconnect', '_simconnect.pyd')
    __loader__ = None; del __bootstrap__, __loader__
    import ctypes
    ctypes.PyDLL(name=__file__, mode = ctypes.RTLD_GLOBAL)
    imp.load_dynamic(__name__,__file__)
__bootstrap__()
