from _winreg import *

def regkey_value(reg_path ):
    aKey = OpenKey(ConnectRegistry(None, reg_path[0]), reg_path[1])
    try:
        return QueryValueEx(aKey, reg_path[2])[0]
    except EnvironmentError:
        return None