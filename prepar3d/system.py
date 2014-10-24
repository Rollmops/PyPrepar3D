from prepar3d._internal.system import regkey_value
import _winreg
import os

class PathType:
    SIM_BASE = [(_winreg.HKEY_CURRENT_USER, 'Software\Lockheed Martin\Prepar3D v2', 'AppPath'),
                (_winreg.HKEY_LOCAL_MACHINE, 'Software\Lockheed Martin\Prepar3D v2', 'AppPath'),
                (_winreg.HKEY_CURRENT_USER, 'SOFTWARE\Wow6432Node\Lockheed Martin\Prepar3D v2', 'AppPath'),
                (_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Wow6432Node\Lockheed Martin\Prepar3D v2', 'AppPath')]
    
def get_path(type=PathType.SIM_BASE):
    for reg_path in type:
        try:
            spath = regkey_value(reg_path)
            if spath is not None and os.path.isdir(spath):
                return spath
        except WindowsError:
            continue
    return None