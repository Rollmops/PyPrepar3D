from . import simconnect

SYSTEM_EVENTS = { 
     '1sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     '4sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     '6sec':  simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'AircraftLoaded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,  # @UndefinedVariable
     'Crashed': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'CrashReset': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'FlightLoaded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,  # @UndefinedVariable
     'FlightSaved': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,  # @UndefinedVariable
     'FlightPlanActivated': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FILENAME,  # @UndefinedVariable
     'FlightPlanDeactivated': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'Frame': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME,  # @UndefinedVariable
     'Pause': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'Paused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'PauseFrame': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME,  # @UndefinedVariable
     'PositionChanged': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'Sim': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'SimStart': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'SimStop': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'Sound': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'Unpaused': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'View': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     'WeatherModeChanged': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT,  # @UndefinedVariable
     # AI related
     'ObjectAdded': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE,  # @UndefinedVariable
     'ObjectRemoved': simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE  # @UndefinedVariable
}