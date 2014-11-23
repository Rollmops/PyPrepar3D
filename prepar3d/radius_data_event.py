from prepar3d.data_event import DataEvent, SimulationVariable
from prepar3d._internal import simconnect
from prepar3d.connection import Connection

class RadiusDataEvent(DataEvent):
    
    def __init__(self, variables, radius, callback=None, object_type=simconnect.SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_AIRCRAFT, at_sim_start=True):
        self._object_type = object_type
        self._radius = radius
        
        super(RadiusDataEvent, self).__init__(variables, callback, at_sim_start=at_sim_start)
        
    def event(self, data):
        return
    
    def refresh(self):
        simconnect.SimConnect_RequestDataOnSimObjectType(Connection()._handle, self._id, self._data_definition_id, self._radius, self._object_id)