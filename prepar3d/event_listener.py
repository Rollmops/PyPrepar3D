import abc
import threading

from prepar3d._internal.simconnect import DispatchHandler
from prepar3d._internal.singleton import Singleton
from prepar3d.connection import Connection
from prepar3d.input_event import InputEvent
from prepar3d.recv_id_event import RecvIdEvent
from prepar3d.system_event import SystemEvent
from prepar3d.data_event import DataEvent


class EventListener(metaclass=Singleton):
    
    def __init__(self):
        self._allow_running_sim_for_all_events = False
        
        self._dispatch_handler = DispatchHandler(Connection()._handle)
        self._sim_start_events = list()
        
        self._sim_start_registered = False


    def _register_events(self, _, __, ___):
        for event in self._sim_start_events:
            self._register_event(event)
            
        
    def _register_event(self, event):
        if isinstance(event, InputEvent):
            return self._dispatch_handler.subscribeInputEvent(event._trigger, event._callback, event._id, event._state, event._priority, event._sim_event) == 0
        
        elif isinstance(event, SystemEvent):        
            return self._dispatch_handler.subscribeSystemEvent(event._trigger, event._recv_id, event._callback, event._id, event._state) == 0
            
        elif isinstance(event, RecvIdEvent):
            return self._dispatch_handler.subscribeRecvIDEvent(event._recv_id, event._callback) == 0
            
        elif isinstance(event, DataEvent):
            return self._dispatch_handler.subscribeDataEvent(event._data_fields, event._id, event._callback)
        else:
            # TODO exception
            pass
        
    def set_allow_running_sim_for_all_events(self, allow):
        ''' Ignore at_sim_start option for all events.
        This allows the developer to test python scripts 
        and receive events with option at_sim_start=True
        even if the sim is already running. 
        
        '''
        self._allow_running_sim_for_all_events = allow
        
    def register_event(self, event):
        if event._at_sim_start and not self._allow_running_sim_for_all_events:
            self._sim_start_events.append(event)
            if not self._sim_start_registered:
                self._sim_start_registered = True
                # register SimStart event 
                SystemEvent('SimStart', callback=self._register_events, at_sim_start=False)
            return True
        else:
            return self._register_event(event)

         
    def listen(self, period=100):
        self._dispatch_handler.listen(period)

