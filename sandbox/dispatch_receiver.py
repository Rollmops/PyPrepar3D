#!/usr/bin/env python

import time

from prepar3d._internal import simconnect


(result, handle) = simconnect.SimConnect_Open("Test", None, 0, None, 0)

receiver = simconnect.DispatchReceiver(handle)
receiver.registerID(simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN)

time.sleep(0.5)

(res, open_recv, size) = receiver.getNextDispatch()

print open_recv

# print open_recv.szApplicationName
# print open_recv.dwApplicationVersionMajor
# print open_recv.dwApplicationVersionMinor
# print open_recv.dwApplicationBuildMajor
