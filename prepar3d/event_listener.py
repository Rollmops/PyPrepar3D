import abc
import threading

from prepar3d._internal.simconnect import EventListenerInternal
from prepar3d._internal.singleton import Singleton
from prepar3d.connection import Connection
from prepar3d.input_event import InputEvent
from prepar3d.recv_id_event import RecvIdEvent
from prepar3d.system_event import SystemEvent


class EventListener(object):
    __metaclass__ = Singleton

    
    def __init__(self):
        self._listener = EventListenerInternal(Connection()._handle)
        self._events = list()
        
        


    def register_event(self, event):
        self._events.append(event)
        
        if isinstance(event, InputEvent):
            return self._listener.subscribeInputEvent(event._trigger, event._callback, event._id, event._state, event._priority) == 0
        
        elif isinstance(event, SystemEvent):        
            return self._listener.subscribeSystemEvent(event._trigger, event._recv_id, event._callback, event._id, event._state) == 0
            
        elif isinstance(event, RecvIdEvent):
            return self._listener.subscribe(event._recv_id, event._callback) == 0
            
        else:
            # TODO exception
            pass
         
    def listen(self, frequency=10):
        self._listener.listen(frequency)

    def get_events(self):
        return self._events
