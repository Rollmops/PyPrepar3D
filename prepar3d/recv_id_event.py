import prepar3d
from prepar3d._internal.base_event import BaseEvent


class RecvIdEvent(BaseEvent):
    
    def __init__(self, recv_id, callback=None, register=True):
        self._recv_id = recv_id
        super(RecvIdEvent, self).__init__(callback, register)
    
    def event(self, event, data, context):
        pass
    
    def set_priority(self, priority):
        return 
    
    def set_state(self, state):
        return 
    
