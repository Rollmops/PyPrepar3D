import prepar3d
from prepar3d._internal import simconnect

from base_event import BaseEvent


class SystemEvent(BaseEvent):
    __SYSTEM_EVENTS__ = { 
         '1sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         '4sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         '6sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'AircraftLoaded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,
         'Crashed': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'CrashReset': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'FlightLoaded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,
         'FlightSaved': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,
         'FlightPlanActivated': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,
         'FlightPlanDeactivated': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'Frame': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME,
         'Pause': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'Paused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'PauseFrame': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME,
         'PositionChanged': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'Sim': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'SimStart': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'SimStop': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'Sound': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'Unpaused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'View': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         'WeatherModeChanged': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,
         # AI related
         'ObjectAdded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE,
         'ObjectRemoved': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE
    }
        
    def __init__(self, trigger, callback=None, register=True):
        super(SystemEvent, self).__init__(callback)
        if trigger not in SystemEvent.__SYSTEM_EVENTS__.keys():
            # TODO rause
            pass
        self._trigger = trigger
        self._recv_id = SystemEvent.__SYSTEM_EVENTS__[trigger]
        
        if register:
            self.register()
        
    def register(self):
        prepar3d.EventListener().register_event(self)
        self._registered = True    
    
    def occur(self, event, data, context):
        return
    
