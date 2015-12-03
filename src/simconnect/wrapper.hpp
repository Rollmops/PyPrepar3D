#ifndef __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
#define __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_

#include "common.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace wrapper
{

HRESULT addClientEventToNotificationGroup(PyObject *, const SIMCONNECT_NOTIFICATION_GROUP_ID &, const SIMCONNECT_CLIENT_EVENT_ID &, const bool &);
HRESULT addToClientDataDefinition(PyObject *, const SIMCONNECT_CLIENT_DATA_DEFINITION_ID &, const DWORD &, const DWORD &, const float &, const DWORD &);
HRESULT addToDataDefinition(PyObject *, const SIMCONNECT_DATA_DEFINITION_ID &, const char*, const char*, const SIMCONNECT_DATATYPE &, const float &, const DWORD &);

HRESULT changeVehicle(PyObject*, const char *);

HRESULT clearClientDataDefinition(PyObject *, const SIMCONNECT_CLIENT_DATA_DEFINITION_ID &);

HRESULT clearDataDefinition(PyObject *, const SIMCONNECT_DATA_DEFINITION_ID &);

HRESULT clearInputGroup(PyObject *, const SIMCONNECT_INPUT_GROUP_ID &);

HRESULT clearNotificationGroup(PyObject *, const SIMCONNECT_NOTIFICATION_GROUP_ID &);

HRESULT close(PyObject *handle);

HRESULT createClientData(PyObject *, const SIMCONNECT_CLIENT_DATA_ID &, const DWORD &, const SIMCONNECT_CREATE_CLIENT_DATA_FLAG &);

HRESULT flightLoad(PyObject *, const char*);

HRESULT flightPlanLoad(PyObject *, const char*);

HRESULT flightSave(PyObject *, const char*, const char*, const char*, const DWORD &);

HRESULT mapInputEventToClientEvent(PyObject *, const int &eventGroup, const char *inputTrigger, const int &id);

HRESULT mapClientDataNameToID(PyObject *, const char *, const SIMCONNECT_CLIENT_DATA_ID &);

HRESULT removeClientEvent(PyObject *, const SIMCONNECT_NOTIFICATION_GROUP_ID &, const SIMCONNECT_CLIENT_EVENT_ID &);

HRESULT removeInputEvent(PyObject *, const SIMCONNECT_INPUT_GROUP_ID &, const char *);

HRESULT requestDataOnSimObjectType(PyObject *, const SIMCONNECT_DATA_REQUEST_ID &id, const SIMCONNECT_DATA_DEFINITION_ID &dataDefinitionID,
		const DWORD &radius, const SIMCONNECT_SIMOBJECT_TYPE &objetID);

HRESULT setDataOnSimObject(PyObject *, const SIMCONNECT_DATA_DEFINITION_ID &, const SIMCONNECT_OBJECT_ID &, const SIMCONNECT_DATA_SET_FLAG &, const DWORD &, const DWORD &, PyObject* );


HRESULT setInputGroupState(PyObject *, const int &, const int &);
HRESULT setInputGroupPriority(PyObject *, const int &, const DWORD &);

HRESULT setNotificationGroupPriority(PyObject *, const int &, const DWORD &);

HRESULT setSystemEventState(PyObject *, const DWORD &, const int &);

HRESULT setTrafficSettings(PyObject *, const UINT &, const UINT &, const UINT &, const UINT &, const UINT &,
		const SIMCONNECT_DYNAMIC_FREQUENCY &, const BOOL &);

tuple getLastSentPacketID(PyObject *);

//tuple getNextDispatch(PyObject *);

tuple open(LPCSTR szName, HWND hWnd, const DWORD &UserEventWin32, HANDLE hEventHandle, const DWORD &ConfigIndex);

HRESULT subscribeToSystemEvent(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName);
HRESULT callDispatch(PyObject *handle, boost::python::object &callback, PyObject *content);

} // end namepsace wrapper
} // end namepspace simconnect
} // end namespace prepar3d

#endif //  __PYPREPAR3D_SIMCONNECT_WRAPPER_HPP_
