from prepar3d._internal.system import regkey_value


class PathType:
    BASE = 0


def get_base_path():
    """get the Prepar3d base installation path

    :return: installation path
    :rtype: str
    :raises WindowsError:  if installation path not found
    """
    #TODO
    return regkey_value(r"HKEY_CURRENT_USER\Software\Python\PythonCore\2.7\InstallPath", "", None)


def get_path(type=PathType.BASE):
    pass