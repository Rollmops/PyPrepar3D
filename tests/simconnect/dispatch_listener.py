#!/usr/bin/env python
from prepar3d._internal import simconnect

frames = 0

def got_frame(event, cbData, blubb):
    print event.fFrameRate


(result, handle) = simconnect.SimConnect_Open("Test", None, 0, None, 0)

print result

listener = simconnect.DispatchListener(handle)

print listener.subscribeSystemEvent("Frame", simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME, got_frame)

listener.listen()

simconnect.SimConnect_Close(handle)