import prepar3d
from .base_event import BaseEvent
from prepar3d._internal.simconnect import SIMCONNECT_GROUP_PRIORITY_HIGHEST, SimConnect_SetInputGroupState, SIMCONNECT_STATE

import logging

class InputEvent(BaseEvent):
    def __init__(self,
                 trigger,
                 sim_event='',
                 callback=None,
                 state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON,
                 priority=SIMCONNECT_GROUP_PRIORITY_HIGHEST,
                 at_sim_start=False):

        self._trigger = trigger
        self._sim_event = sim_event
        super().__init__(callback=callback,
                         state=state,
                         priority=priority,
                         at_sim_start=at_sim_start)

#     def set_state(self, state):
#         self._state = state
#         if self._registered:
#             SimConnect_SetInputGroupState(prepar3d.Connection()._handle, self._id, self._state)

#     def set_priority(self, priority):
#         self._priority = priority
#         if self._registered:
#             SimConnect_SetInputGroupPriority(prepar3d.Connection()._handle, self._id, self._priority)
            
    def subscribe(self, connection):
        logging.info('Subscribing event %s', self)
        return connection._dispatch_handler.subscribeInputEvent(self._trigger, self._callback, self._id, self._state, self._priority, self._sim_event) == 0


    def event(self, event, data):
        return
    
    def __str__(self):
        return 'InputEvent<%s, %s> -> %s' % (self._trigger, self._sim_event, self._callback)
