import prepar3d
from prepar3d._internal.base_event import BaseEvent
from prepar3d._internal.simconnect import SIMCONNECT_GROUP_PRIORITY_HIGHEST, SimConnect_SetInputGroupState, SIMCONNECT_STATE


class InputEvent(BaseEvent):
    def __init__(self, trigger, callback=None, state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON, priority=SIMCONNECT_GROUP_PRIORITY_HIGHEST, register=True, enabled=None, at_sim_start=False):
        self._trigger = trigger
        super(InputEvent, self).__init__(callback, state, priority, register, enabled, at_sim_start)
        
    def set_state(self, state):
        self._state = state
        if self._registered:
            SimConnect_SetInputGroupState(prepar3d.Connection()._handle, self._id, self._state)

    def set_priority(self, priority):
        self._priority = priority
        if self._registered:
            SimConnect_SetInputGroupPriority(prepar3d.Connection()._handle, self._id, self._priority)
            

    def event(self, event, data, context):
        return
        
