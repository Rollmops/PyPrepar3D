import threading
import abc
import prepar3d
from prepar3d._internal import simconnect, singleton


class EventListener(object):
    __metaclass__ = singleton.Singleton
    
    __SYSTEM_EVENTS__ = { 'Unpaused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
                          'Paused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
                         'SimStart': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
                         'Frame': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME }
    
    def __init__(self, connection, frequency=10):
        self._listener = simconnect.EventListener(connection._handle)
        self._frequency = frequency

    def register_event(self, event):
        if event._trigger in EventListener.__SYSTEM_EVENTS__.keys():
            self._listener.subscribeSystemEvent(event._trigger, EventListener.__SYSTEM_EVENTS__[event._trigger], event.occur)
        else:
            self._listener.subscribeInputEvent(event._trigger, simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT, event.occur)
 
    def listen(self):
        self._listener.listen(self._frequency)
        
        
        
        
        