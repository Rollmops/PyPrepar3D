import abc
import threading

import prepar3d
from prepar3d._internal import simconnect, singleton, id


class EventListener(object):
    __metaclass__ = singleton.Singleton

    
    def __init__(self):
        self._listener = simconnect.EventListener(prepar3d.Connection()._handle)
        self._events = list()


    def register_event(self, event):
        self._events.append(event)
        
        if isinstance(event, prepar3d.InputEvent):
            self._listener.subscribeInputEvent(event._trigger, event._recv_id, event._callback, event._id)
        
        elif isinstance(event, prepar3d.SystemEvent):        
            self._listener.subscribeSystemEvent(event._trigger, event._recv_id, event._callback, event._id)
         
    def listen(self, frequency=10):
        self._listener.listen(frequency)
