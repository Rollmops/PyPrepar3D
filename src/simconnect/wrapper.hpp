#ifndef __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
#define __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_

#include "common.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace wrapper
{

HRESULT addClientEventToNotificationGroup(PyObject *,
		SIMCONNECT_NOTIFICATION_GROUP_ID, SIMCONNECT_CLIENT_EVENT_ID, bool);
HRESULT addToClientDataDefinition(PyObject *,
		SIMCONNECT_CLIENT_DATA_DEFINITION_ID, DWORD, DWORD, float, DWORD);
HRESULT addToDataDefinition(PyObject *, SIMCONNECT_DATA_DEFINITION_ID,
		const char*, const char*, SIMCONNECT_DATATYPE, float, DWORD);

HRESULT changeVehicle(PyObject*, const char *);

HRESULT clearClientDataDefinition(PyObject *,
		SIMCONNECT_CLIENT_DATA_DEFINITION_ID);

HRESULT clearDataDefinition(PyObject *, SIMCONNECT_DATA_DEFINITION_ID);

HRESULT clearInputGroup(PyObject *, SIMCONNECT_INPUT_GROUP_ID);

HRESULT clearNotificationGroup(PyObject *, SIMCONNECT_NOTIFICATION_GROUP_ID);

HRESULT close(PyObject *handle);

HRESULT createClientData(PyObject *, SIMCONNECT_CLIENT_DATA_ID, DWORD,
		SIMCONNECT_CREATE_CLIENT_DATA_FLAG);

HRESULT flightLoad(PyObject *, const char*);

HRESULT flightPlanLoad(PyObject *, const char*);

HRESULT flightSave(PyObject *, const char*, const char*, const char*, DWORD);

tuple getLastSentPacketID(PyObject *);

void registerSimConnectRecvId(SIMCONNECT_RECV_ID id);
tuple getNextDispatch(PyObject *) ;

tuple open(LPCSTR szName, HWND hWnd, DWORD UserEventWin32,
		HANDLE hEventHandle, DWORD ConfigIndex);

HRESULT subscribeToSystemEvent(PyObject *handle,
		SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName);
HRESULT callDispatch(PyObject *handle, boost::python::object callback,
		PyObject *content);

} // end namepsace wrapper
} // end namepspace simconnect
} // end namespace prepar3d

#endif //  __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
