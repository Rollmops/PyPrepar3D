from prepar3d import _simconnect

(result, handle) = _simconnect.open('huhu', None, 0, None, 0)


print _simconnect.close(handle)