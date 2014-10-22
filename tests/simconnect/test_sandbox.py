from prepar3d import _simconnect
import time

a = _simconnect.SIMCONNECT_RECV_EVENT_OBJECT_ADDREMOVE()

a.eObjType = _simconnect.SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_GROUND

print type(a.eObjType)

#frames = 0

# 
# def f(pData, cbData, pContext):
#     global frames
#     frames += 1  
# 
# 
# (ret, handle) = _simconnect.open("Test", None, 0, None, 0)
# print ret
# 
# _simconnect.subscribe_to_system_event(handle, 1, 'Frame')
# 
# while True:
#     _simconnect.call_dispatch(handle, f, None) 
#     time.sleep(2)
#     global frames
#     print frames