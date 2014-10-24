from _winreg import *

def regkey_value(start_key, path, key ):
    aKey = OpenKey(ConnectRegistry(None, start_key), path)
    try:
        return QueryValueEx(aKey, key)[0]
    except EnvironmentError:
        return None