from prepar3d._internal import simconnect

from _internal.singleton import Singleton


class Connection(object):
    __metaclass__ = Singleton
    
    def __init__(self):
        self._connected = False
        self._handle = None
        self._name = None
        pass
        
    def open(self, name, window_handle=None, user_event_win32=0, event_handle=None, config_index=0):
        self._name = name
        (result, self._handle) = simconnect.SimConnect_Open(self._name, window_handle, user_event_win32, event_handle, config_index)
        
        self._connected = result == 0 and self._handle is not None
        
    def close(self):
        if self._connected and self._handle is not None:
            simconnect.SimConnect_Close(self._handle)
        pass
        
    def __del__(self):
        self.close()
    
    
