import prepar3d
from .base_event import BaseEvent
from prepar3d._internal import simconnect
from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SimConnect_AddToDataDefinition
from prepar3d import SimulationVariable
    
import logging

class DataEvent(BaseEvent):
    
    def __init__(self,
                 variables,
                 callback=None,
                 period=simconnect.SIMCONNECT_PERIOD.SIMCONNECT_PERIOD_SIM_FRAME,
                 flags=simconnect.SIMCONNECT_DATA_REQUEST_FLAG_CHANGED,
                 at_sim_start=True):

        if not isinstance(variables,list):
            self._variables = [variables]
        else:
            self._variables = variables
            
        super().__init__(callback=callback,
                         at_sim_start=at_sim_start)

        self._period = period
        self._flags = flags

        self._data_definition_id = Id().get("DataDefinition")
        self._at_sim_start = at_sim_start
        self._object_id = simconnect.SIMCONNECT_OBJECT_ID_USER


    def subscribe(self, connection):
        logging.info('Subscribing event %s', self)
        connection._dispatch_handler.subscribeDataEvent(self)

    def event(self, data):
        return

    def __str__(self):
        return 'DataEvent< Variables: %s > -> %s' % (self._variables, self._callback)
