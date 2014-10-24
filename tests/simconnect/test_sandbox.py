from prepar3d import system
from prepar3d._internal import simconnect
import time


(res, handle) = simconnect.SimConnect_Open("Test", None, 0, None, 0)


print res, handle
simconnect.SimConnect_RegisterIDForDispatch(simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_OPEN)
time.sleep(1)


a = simconnect.SimConnect_GetNextDispatch(handle)

print a

print system.get_path()