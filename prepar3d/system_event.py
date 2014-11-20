import prepar3d
from prepar3d._internal import simconnect
from prepar3d._internal.base_event import BaseEvent
from prepar3d._internal.simconnect import SimConnect_SetSystemEventState, SIMCONNECT_STATE


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
        
    def __init__(self, trigger, callback=None, state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON, register=True, enabled=None, at_sim_start=False):
        
        # check if we know the system trigger
        if trigger.lower() not in [key.lower() for key in SystemEvent.__SYSTEM_EVENTS__.keys()]:
            # TODO rause
            pass
        
        self._trigger = trigger
        self._recv_id = SystemEvent.__SYSTEM_EVENTS__[trigger]
        
        super(SystemEvent, self).__init__(callback, state, None, register, enabled, at_sim_start)

        
    def set_state(self, state):
        self._state = state
        if self._registered:
            SimConnect_SetSystemEventState(prepar3d.Connection()._handle, self._id, self._state)

    def set_priority(self, priority):
        return

    def event(self, event, data):
        return
    
