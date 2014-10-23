from prepar3d import _simconnect

a = _simconnect.getNextDispatch(None)

print a

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