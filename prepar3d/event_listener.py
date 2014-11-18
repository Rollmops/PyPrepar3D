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
        self._sim_start_events = list()
        
        self._sim_start_registered = False


    def _register_events(self, _, __, ___):
        for event in self._sim_start_events:
            self._register_event(event)
            
        
    def _register_event(self, event):
        if isinstance(event, InputEvent):
            return self._listener.subscribeInputEvent(event._trigger, event._callback, event._id, event._state, event._priority, event._sim_event) == 0
        
        elif isinstance(event, SystemEvent):        
            return self._listener.subscribeSystemEvent(event._trigger, event._recv_id, event._callback, event._id, event._state) == 0
            
        elif isinstance(event, RecvIdEvent):
            return self._listener.subscribe(event._recv_id, event._callback) == 0
            
        else:
            # TODO exception
            pass
        
        
    def register_event(self, event):
        if event._at_sim_start:
            self._sim_start_events.append(event)
            if not self._sim_start_registered:
                self._sim_start_registered = True
                # register SimStart event 
                SystemEvent('SimStart', callback=self._register_events, sim_start=False)
            return True
        else:
            return self._register_event(event)

         
    def listen(self, frequency=100):
        self._listener.listen(frequency)

