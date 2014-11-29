from prepar3d._internal.simulation_variables import _SIMULATION_VARIABLES
from prepar3d._internal.id import Id

class SimulationVariable:

    def __init__(self, name, key=None, unit=None, data_type=None, epsilon=0):
        default = _SIMULATION_VARIABLES[name]
        self._name = name
        self._key = name if key is None else key
        self._unit = default[0] if unit is None else unit
        self._data_type = default[1] if data_type is None else data_type
        self._epsilon = epsilon
        self._id = Id().get('SimulationVariableID')