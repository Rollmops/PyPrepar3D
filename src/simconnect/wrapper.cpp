#include "wrapper.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace wrapper
{
namespace _internal
{
static object *__callback__;
void CALLBACK __caller__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	_internal::__callback__->operator ()(pData, cbData, handle<>(PyCapsule_New(pContext, NULL, NULL)));
}
} // end namespace _internal

HRESULT addClientEventToNotificationGroup(PyObject *handle, const SIMCONNECT_NOTIFICATION_GROUP_ID &groupID,
		const SIMCONNECT_CLIENT_EVENT_ID &eventID, const bool &bMaskable)
{
	return SimConnect_AddClientEventToNotificationGroup(PyCapsule_GetPointer(handle, NULL), groupID, eventID, bMaskable);
}

HRESULT addToClientDataDefinition(PyObject *handle, const SIMCONNECT_CLIENT_DATA_DEFINITION_ID &defineID, const DWORD &dwOffset,
		const DWORD &dwSizeOrType, const float &fEpsilon, const DWORD &datumID)
{
	return SimConnect_AddToClientDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID, dwOffset, dwSizeOrType, fEpsilon, datumID);
}

HRESULT addToDataDefinition(PyObject *hSimConnect, const SIMCONNECT_DATA_DEFINITION_ID &DefineID, const char* DatumName,
		const char* UnitsName, const SIMCONNECT_DATATYPE &DatumType, const float &fEpsilon, const DWORD &DatumID)
{
	return SimConnect_AddToDataDefinition(PyCapsule_GetPointer(hSimConnect, NULL), DefineID, DatumName, UnitsName, DatumType, fEpsilon,
			DatumID);
}

HRESULT changeVehicle(PyObject* handle, const char *vehicleTitle)
{
	return SimConnect_ChangeVehicle(PyCapsule_GetPointer(handle, NULL), vehicleTitle);
}

HRESULT clearClientDataDefinition(PyObject *handle, const SIMCONNECT_CLIENT_DATA_DEFINITION_ID &defineID)
{
	return SimConnect_ClearClientDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID);
}

HRESULT clearDataDefinition(PyObject *handle, const SIMCONNECT_DATA_DEFINITION_ID &defineID)
{
	return SimConnect_ClearDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID);
}

HRESULT clearInputGroup(PyObject *handle, const SIMCONNECT_INPUT_GROUP_ID &groupID)
{
	return SimConnect_ClearInputGroup(PyCapsule_GetPointer(handle, NULL), groupID);
}

HRESULT clearNotificationGroup(PyObject *handle, const SIMCONNECT_NOTIFICATION_GROUP_ID &groupID)
{
	return SimConnect_ClearNotificationGroup(PyCapsule_GetPointer(handle, NULL), groupID);
}

HRESULT close(PyObject *handle)
{
	return SimConnect_Close(PyCapsule_GetPointer(handle, NULL));
}

HRESULT createClientData(PyObject *handle, const SIMCONNECT_CLIENT_DATA_ID &dataID, const DWORD &dwSize,
		const SIMCONNECT_CREATE_CLIENT_DATA_FLAG &dataFlags)
{
	return SimConnect_CreateClientData(PyCapsule_GetPointer(handle, NULL), dataID, dwSize, dataFlags);
}

HRESULT flightLoad(PyObject *handle, const char* fileName)
{
	return SimConnect_FlightLoad(PyCapsule_GetPointer(handle, NULL), fileName);
}

HRESULT flightPlanLoad(PyObject *handle, const char* fileName)
{
	return SimConnect_FlightPlanLoad(PyCapsule_GetPointer(handle, NULL), fileName);
}

HRESULT flightSave(PyObject *handle, const char *fileName, const char *title, const char *description, const DWORD &flags)
{
	return SimConnect_FlightSave(PyCapsule_GetPointer(handle, NULL), fileName, title, description, flags);
}

HRESULT mapInputEventToClientEvent(PyObject *handle, const int &eventGroup, const char *inputTrigger, const int &id)
{
	return SimConnect_MapInputEventToClientEvent(PyCapsule_GetPointer(handle, NULL), eventGroup, inputTrigger, id);
}

HRESULT mapClientDataNameToID(PyObject *handle, const char *szClientDataName, const SIMCONNECT_CLIENT_DATA_ID &ClientDataID)
{
	return SimConnect_MapClientDataNameToID(PyCapsule_GetPointer(handle, NULL), szClientDataName, ClientDataID);
}

HRESULT removeClientEvent(PyObject *handle, const SIMCONNECT_NOTIFICATION_GROUP_ID &GroupID, const SIMCONNECT_CLIENT_EVENT_ID &EventID)
{
	return SimConnect_RemoveClientEvent(PyCapsule_GetPointer(handle, NULL), GroupID, EventID);
}

HRESULT removeInputEvent(PyObject *handle, const SIMCONNECT_INPUT_GROUP_ID &GroupID, const char *pszInputDefinition)
{
	return SimConnect_RemoveInputEvent(PyCapsule_GetPointer(handle, NULL), GroupID, pszInputDefinition);
}

HRESULT requestDataOnSimObjectType(PyObject *handle, const SIMCONNECT_DATA_REQUEST_ID &id,
		const SIMCONNECT_DATA_DEFINITION_ID &dataDefinitionID, const DWORD &radius, const SIMCONNECT_SIMOBJECT_TYPE &objetID)
{
	return SimConnect_RequestDataOnSimObjectType(PyCapsule_GetPointer(handle, NULL), id, dataDefinitionID, radius, objetID);
}

HRESULT setDataOnSimObject(PyObject *handle, const SIMCONNECT_DATA_DEFINITION_ID &DefineID, const SIMCONNECT_OBJECT_ID &ObjectID,
		const SIMCONNECT_DATA_SET_FLAG &Flags, const DWORD &ArrayCount, const DWORD &cbUnitSize, PyObject *pDataSet)
{
	return SimConnect_SetDataOnSimObject(PyCapsule_GetPointer(handle, NULL), DefineID, ObjectID, Flags, ArrayCount, cbUnitSize,
			PyCapsule_GetPointer(pDataSet, NULL));
}

HRESULT setInputGroupState(PyObject *handle, const int &id, const int &state)
{
	return SimConnect_SetInputGroupState(PyCapsule_GetPointer(handle, NULL), id, state);
}

HRESULT setInputGroupPriority(PyObject *handle, const int &id, const DWORD &priorioty)
{
	return SimConnect_SetInputGroupPriority(PyCapsule_GetPointer(handle, NULL), id, priorioty);
}

HRESULT setNotificationGroupPriority(PyObject *handle, const int &groupId, const DWORD &priorioty)
{
	return SimConnect_SetNotificationGroupPriority(PyCapsule_GetPointer(handle, NULL), groupId, priorioty);
}

HRESULT setSystemEventState(PyObject *handle, const DWORD &eventId, const int &state)
{
	return SimConnect_SetSystemEventState(PyCapsule_GetPointer(handle, NULL), eventId, static_cast<SIMCONNECT_STATE>(state));
}

HRESULT setTrafficSettings(PyObject *handle, const UINT &uAirlineDensity, const UINT &uGADensity, const UINT &uRoadTrafficDensity,
		const UINT &uShipsAndFerriesDensity, const UINT &uLeisureBoatDensity, const SIMCONNECT_DYNAMIC_FREQUENCY &eAirportVehicleDensity,
		const BOOL &bIFROnly)
{
	return SimConnect_SetTrafficSettings(PyCapsule_GetPointer(handle, NULL), uAirlineDensity, uGADensity, uRoadTrafficDensity,
			uShipsAndFerriesDensity, uLeisureBoatDensity, eAirportVehicleDensity, bIFROnly);
}

tuple getLastSentPacketID(PyObject *handle)
{
	DWORD id;
	HRESULT result = SimConnect_GetLastSentPacketID(PyCapsule_GetPointer(handle, NULL), &id);
	return make_tuple(result, id);
}

tuple open(PCSTR szName, HWND hWnd, const DWORD &UserEventWin32, HANDLE hEventHandle, const DWORD &ConfigIndex)
{
	HANDLE phSimConnect;
	const HRESULT result = SimConnect_Open(&phSimConnect, szName, hWnd, UserEventWin32, hEventHandle, ConfigIndex);
	if (result == S_OK && phSimConnect != NULL)
	{
		//TODO check if we need to borrow the object
		return make_tuple(result, handle<>(PyCapsule_New(phSimConnect, NULL, NULL)));
	}
	else
	{
		return make_tuple(result, object());
	}
}

HRESULT subscribeToSystemEvent(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName)
{
	return SimConnect_SubscribeToSystemEvent(PyCapsule_GetPointer(handle, NULL), eventID, systemEventName);
}

HRESULT callDispatch(PyObject *handle, boost::python::object &callback, PyObject *content)
{
	_internal::__callback__ = &callback;
	return SimConnect_CallDispatch(PyCapsule_GetPointer(handle, NULL), _internal::__caller__, NULL);
}

} // end namespace wrapper
} // end namespace simconnect
} // end namespace prepar3d
