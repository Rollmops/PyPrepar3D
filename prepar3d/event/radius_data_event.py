from .data_event import DataEvent

class RadiusDataEvent(DataEvent):
    
    def __init__(self,
                 variables,
                 radius,
                 object_type,
                 callback=None,
                 period=simconnect.SIMCONNECT_PERIOD.SIMCONNECT_PERIOD_SIM_FRAME,  # @UndefinedVariable
                 flags=simconnect.SIMCONNECT_DATA_REQUEST_FLAG_CHANGED,  # @UndefinedVariable
                 at_sim_start=True):
        
        super().__init__(variables, callback, period, flags, at_sim_start)
        
        self._radius = radius
        self._object_type = object_type
        self._data = dict()

        
    def subscribe(self, connection):
        self.logger.info('Subscribing radius data event %s', self)
        connection._dispatch_handler.subscribeRadiusDataEvent(self)
        
    def event(self):
        return
