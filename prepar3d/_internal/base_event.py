import abc

import prepar3d
from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SIMCONNECT_GROUP_PRIORITY_HIGHEST, SIMCONNECT_STATE, SimConnect_SetInputGroupState


class BaseEvent(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, callback=None, state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON, priority=SIMCONNECT_GROUP_PRIORITY_HIGHEST, register=True, enabled=None):
        self._id = Id().get('EventID')
        self._callback = self.event if callback is None else callback
        if enabled is not None:
            self._state = SIMCONNECT_STATE.SIMCONNECT_STATE_ON if enabled else SIMCONNECT_STATE.SIMCONNECT_STATE_OFF
        else:
            self._state = state
        self._priority = priority
        self._registered = False
        
        if register:
            self.register()

    def register(self):
        self._registered = prepar3d.EventListener().register_event(self)

    @abc.abstractmethod
    def set_state(self, state):
        return
    
    @abc.abstractmethod
    def set_priority(self, priority):
        return

    @abc.abstractmethod
    def event(self, event, data, context):
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
