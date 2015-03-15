import abc

from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SIMCONNECT_STATE, SIMCONNECT_GROUP_PRIORITY_HIGHEST  # @UnresolvedImport

import logging

class BaseEvent(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self,
                 callback,
                 state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON,
                 priority=SIMCONNECT_GROUP_PRIORITY_HIGHEST,
                 enabled=None,
                 at_sim_start=False):

        self._id = Id().get('EventID')
        self._callback = callback or self.event
        self._priority = priority

        if enabled is not None:
            self._state = SIMCONNECT_STATE.SIMCONNECT_STATE_ON if enabled else SIMCONNECT_STATE.SIMCONNECT_STATE_OFF
        else:
            self._state = state
        self._at_sim_start = at_sim_start
        
        self.connection = None
        
    @abc.abstractmethod
    def subscribe(self, connection):
        return
    
    @abc.abstractmethod
    def unsubscribe(self):
        return
    
    
    @abc.abstractmethod
    def set_state(self, state):
        return
    
    @abc.abstractmethod
    def set_priority(self, priority):
        return

    @abc.abstractmethod
    def event(self, event, data):
        return
        
    def get_priority(self):
        return self._priority
    
    def get_state(self):
        return self._state
    
    def is_registered(self):
        return self._registered
    
    def get_id(self):
        return self._id
    
    def set_enabled(self, enabled):
        self.set_state(SIMCONNECT_STATE.SIMCONNECT_STATE_ON if enabled else SIMCONNECT_STATE.SIMCONNECT_STATE_OFF)
        
    def is_enabled(self):
        return self._state == SIMCONNECT_STATE.SIMCONNECT_STATE_ON
