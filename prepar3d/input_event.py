import prepar3d
from prepar3d._internal import simconnect

from base_event import BaseEvent


class InputEvent(BaseEvent):
    def __init__(self, trigger, callback=None, register=True):
        super(InputEvent, self).__init__(callback)
        self._trigger = trigger
        self._recv_id = simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT
        
        if register:
            self.register()

    def register(self):
        prepar3d.EventListener().register_event(self)
        self._registered = True

    def occur(self, event, data, context):
        return
        
