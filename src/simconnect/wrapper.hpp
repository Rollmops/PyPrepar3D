#ifndef __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
#define __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_

#include "common.hpp"

namespace prepar3d {
namespace simconnect {
namespace wrapper {

HRESULT addClientEventToNotificationGroup(PyObject *handle, SIMCONNECT_NOTIFICATION_GROUP_ID groupID, SIMCONNECT_CLIENT_EVENT_ID eventID, bool bMaskable);
HRESULT addToClientDataDefinition(PyObject *handle, SIMCONNECT_CLIENT_DATA_DEFINITION_ID  defineID, DWORD dwOffset, DWORD  dwSizeOrType, float  fEpsilon, DWORD  DatumID );

boost::python::tuple open(LPCSTR szName, HWND  hWnd, DWORD  UserEventWin32, HANDLE  hEventHandle, DWORD  ConfigIndex);
HRESULT close(PyObject *handle);
HRESULT subscribeToSystemEvent(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName);
HRESULT callDispatch(PyObject *handle, boost::python::object callback, PyObject *content);

} // end namepsace wrapper
} // end namepspace simconnect
} // end namespace prepar3d



#endif //  __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
