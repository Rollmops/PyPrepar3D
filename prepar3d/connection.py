import logging

from contextlib import contextmanager
from prepar3d import Prepar3dException
from .simconnect import SimConnect_Close, SimConnect_Open  # @UnresolvedImport
from .simconnect import DispatchHandler  # @UnresolvedImport
from .singleton import Singleton

from prepar3d.event.base_event import BaseEvent



class Connection(metaclass=Singleton):
    
    def __init__(self, name):
        self._name = name
        
        self.logger = logging.getLogger(__name__)
        self._connected = False
        self._handle = None
        self._name = None
        self._dispatch_handler = None
        self._events = []
        self._predefined_events = []

    @contextmanager
    def open(self,
             window_handle=None,
             user_event_win32=0,
             event_handle=None,
             config_index=0):

        self.logger.debug('About to call SimConnect_Open')
        (result, self._handle) = SimConnect_Open(self._name, window_handle, user_event_win32, event_handle, config_index)
        self.logger.info('SimConnect_Open -> result: %d', result)
        self._connected = result == 0 and self._handle is not None
        if not self._connected:
            raise OpenConnectionException(self._name, result)

        self._dispatch_handler = DispatchHandler(self._handle)
        
        for event in self._predefined_events:
            self.subscribe(event)
            self._predefined_events.remove(event)
            
        yield
        
        self.close()
            
    # do not delete arguments since these are needed for using close as a callback function
    def close(self, _=None, __=None, ___=None):
        if self._connected and self._handle is not None:
            self.logger.info('Closing connection \'%s\'', self._name)
            result = SimConnect_Close(self._handle)
            self.logger.info('Closed connection \'%s\' with return code %d', self._name, result)
            if result == 0:
                self._connected = False
            else:
                raise CloseConnectionException(self.name, result)
        return
    
    def is_open(self):
        return self._connected


    def subscribe(self, event):
        if not isinstance(event, BaseEvent):
            raise TypeError('Expected BaseEvent derived type in Connection.subscribe() but got %s' % type(event))
        if not self._connected or self._dispatch_handler is None:
            self.logger.info('Presubscribing event %s', event)
            self._predefined_events.append(event)
        else:
            event.subscribe(self)
            event.connection = self
            self._events.append(event)

        
    def unsubscribe(self, event):
        if not event in self._events:
            raise RuntimeError('Trying to unsubscribe not subscribed event %s' % event)
        event.unsubscribe(self)


    def listen(self, period=100):
        if not self._connected or self._dispatch_handler is None:
            raise RuntimeError('Trying to listen with a non yet connected connection')
        self.logger.info('Start to listen for connection \'%s\'', self._name)
        self._dispatch_handler.listen(period)
        
        
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

