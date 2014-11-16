from prepar3d._internal import simconnect


class Connection(object):
    
    def __init__(self, name, window_handle=None, user_event_win32=0, event_handle=None, config_index=0, open=False):
        self._name = name
        self._window_handle = window_handle
        self._user_event_win32 = user_event_win32
        self._event_handle = event_handle
        self._config_index = config_index
        self._connected = False
        self._handle = None
        
        if open:
            self.open()
            
    def open(self):
        (result, self._handle) = simconnect.SimConnect_Open(self._name, self._window_handle, self._user_event_win32, self._event_handle, self._config_index)
        
        self._connected = result == 0 and self._handle is not None
        
    def close(self):
        if self._connected and self._handle is not None:
            simconnect.SimConnect_Close(self._handle)
        pass
        
    def __del__(self):
        self.close()
    
    