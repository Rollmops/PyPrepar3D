import prepar3d
from prepar3d._internal import simconnect
from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SimConnect_AddToDataDefinition
from prepar3d._internal.simulation_variables import _SIMULATION_VARIABLES


class SimulationVariable:

    def __init__(self, name, key=None, unit=None, data_type=None, epsilon=0):
        default = _SIMULATION_VARIABLES[name]
        self._name = name
        self._key = name if key is None else key
        self._unit = default[0] if unit is None else unit
        self._data_type = default[1] if data_type is None else data_type
        self._epsilon = epsilon
        self._id = Id().get('SimulationVariableID')
        
class DataEvent:
    
    def __init__(self, variables, callback=None, period=simconnect.SIMCONNECT_PERIOD.SIMCONNECT_PERIOD_SIM_FRAME, flags=simconnect.SIMCONNECT_DATA_REQUEST_FLAG_CHANGED, at_sim_start=True):
        self._variables = variables
        self._callback = self.event if callback is None else callback
        self._id = Id().get('DataEventID')
        self._data_definition_id = Id().get("DataDefinitionID")
        self._at_sim_start = at_sim_start
        self._period = period
        self._flags = flags
        self._object_id = simconnect.SIMCONNECT_OBJECT_ID_USER

        prepar3d.EventListener().register_event(self)
        
    def event(self, data):
        return
