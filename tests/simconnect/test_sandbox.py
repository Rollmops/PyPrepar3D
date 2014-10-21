from prepar3d import _simconnect
import time

def f(pData, cbData, pContext):
    print "inside: "
    print pData.dwID 


(ret, handle) = _simconnect.open("Test", None, 0, None, 0)
print ret

while True:
    _simconnect.call_dispatch(handle, f, None) 
    time.sleep(1)