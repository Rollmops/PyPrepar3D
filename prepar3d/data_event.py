from prepar3d._internal.simconnect import SimConnect_AddToDataDefinition
from prepar3d._internal.id import Id
import prepar3d

class DataEvent:
    
    
    def __init__(self, data_fields, callback=None):
        self._data_fields = data_fields
        self._callback = self.event if callback is None else callback
        self._id = Id().get('DataEventID')
        
        prepar3d.EventListener().register_event(self)
        
    def event(self, data):
        return