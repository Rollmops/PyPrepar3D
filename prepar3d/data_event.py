import prepar3d
from prepar3d._internal import simconnect
from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SimConnect_AddToDataDefinition
from prepar3d.simulation_variable import SimulationVariable
        
class DataEvent:
    
    def __init__(self, variables, callback=None, period=simconnect.SIMCONNECT_PERIOD.SIMCONNECT_PERIOD_SIM_FRAME, flags=simconnect.SIMCONNECT_DATA_REQUEST_FLAG_CHANGED, at_sim_start=True):
        self._variables = variables
        self._callback = self.event if callback is None else callback
        self._id = Id().get('DataEvent')
        self._data_definition_id = Id().get("DataDefinition")
        self._at_sim_start = at_sim_start
        self._period = period
        self._flags = flags
        self._object_id = simconnect.SIMCONNECT_OBJECT_ID_USER

        prepar3d.EventListener().register_event(self)
        
    def event(self, data):
        return
