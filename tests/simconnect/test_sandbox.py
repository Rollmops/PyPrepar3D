import ctypes
ctypes.PyDLL(r"C:\Python27\Lib\site-packages\prepar3d-0.1.0-py2.7-win32.egg\prepar3d\_simconnect.pyd")

# from prepar3d import _simconnect
# import time
# 
# (ret, handle) = _simconnect.open("Test", None, 0, None, 0)
# 
# print ret
# print handle
# # print _simconnect.subscribeToSystemEvent(handle, 10, "Frame")
# time.sleep(1)
# 
# a = _simconnect.getNextDispatch(handle)
# 
# print a
# 
# _simconnect.close(handle)

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