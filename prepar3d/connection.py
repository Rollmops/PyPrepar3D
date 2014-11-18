from prepar3d import Prepar3dException
from prepar3d._internal.simconnect import SIMCONNECT_RECV_ID
from prepar3d._internal.simconnect import SimConnect_Close, SimConnect_Open
from prepar3d._internal.singleton import Singleton
from prepar3d.recv_id_event import RecvIdEvent


class ConnectionException(Prepar3dException):
    def __init__(self, name):
        super(ConnectionException, self).__init__()
        self.name = name
        
    def __str__(self):
        return 'A connection error for connection \'%s\' occurred' % self.name

class OpenConnectionException(ConnectionException):
    def __init__(self, name, result):
        super(OpenConnectionException, self).__init__(name)
        self.result = result
        
    def __str__(self):
        return 'Opening the connection \'%s\' failed with result \'%d\'' % (self.name, self.result)

class CloseConnectionException(ConnectionException):
    def __init__(self, name, result):
        super(CloseConnectionException, self).__init__(name)
        self.result = result
        
    def __str__(self):
        return 'Closing the connection \'%s\' failed with result \'%d\'' % (self.name, self.result)


class Connection(object):
    __metaclass__ = Singleton
    
    def __init__(self):
        self._connected = False
        self._handle = None
        self._name = None
        
    def open(self, name, window_handle=None, user_event_win32=0, event_handle=None, config_index=0, auto_close=True):
        self._name = name
        (result, self._handle) = SimConnect_Open(self._name, window_handle, user_event_win32, event_handle, config_index)
        self._connected = result == 0 and self._handle is not None
        
        if not self._connected:
            raise OpenConnectionException(self._name, result)
        
        if auto_close:        
            RecvIdEvent(SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_QUIT, self.close)
        
    def close(self, _, __, ___):
        if self._connected and self._handle is not None:
            result = SimConnect_Close(self._handle)
            if result == 0:
                self._connected = False
            else:
                raise CloseConnectionException(self.name, result)
        return
    
    
    def __del__(self):
        self.close()
    
    
