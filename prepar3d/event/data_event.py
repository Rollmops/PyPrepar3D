from .base_event import BaseEvent
from prepar3d._internal import simconnect
from prepar3d._internal.id import Id
    
import logging

class DataEvent(BaseEvent):
    '''Event that handles data changes
    '''
    
    def __init__(self,
                 variables,
                 callback=None,
                 period=simconnect.SIMCONNECT_PERIOD.SIMCONNECT_PERIOD_SIM_FRAME,  # @UndefinedVariable
                 flags=simconnect.SIMCONNECT_DATA_REQUEST_FLAG_CHANGED,  # @UndefinedVariable
                 at_sim_start=True):

        self.logger = logging.getLogger(__name__)

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
        self._object_id = simconnect.SIMCONNECT_OBJECT_ID_USER  # @UndefinedVariable


    def subscribe(self, connection):
        self.logger.info('Subscribing data event %s', self)
        connection._dispatch_handler.subscribeDataEvent(self)

    def event(self, data):
        return

    def __str__(self):
        return 'DataEvent< Variables: %s > -> %s' % (self._variables, self._callback)
