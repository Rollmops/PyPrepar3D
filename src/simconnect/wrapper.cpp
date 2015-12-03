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

HRESULT addClientEventToNotificationGroup(PyObject *handle, SIMCONNECT_NOTIFICATION_GROUP_ID groupID, SIMCONNECT_CLIENT_EVENT_ID eventID,
		bool bMaskable)
{
	return SimConnect_AddClientEventToNotificationGroup(PyCapsule_GetPointer(handle, NULL), groupID, eventID, bMaskable);
}

HRESULT addToClientDataDefinition(PyObject *handle, SIMCONNECT_CLIENT_DATA_DEFINITION_ID defineID, DWORD dwOffset, DWORD dwSizeOrType,
		float fEpsilon, DWORD datumID)
{
	return SimConnect_AddToClientDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID, dwOffset, dwSizeOrType, fEpsilon, datumID);
}

HRESULT addToDataDefinition(PyObject *hSimConnect, SIMCONNECT_DATA_DEFINITION_ID DefineID, const char* DatumName, const char* UnitsName,
		SIMCONNECT_DATATYPE DatumType, float fEpsilon, DWORD DatumID)
{
	return SimConnect_AddToDataDefinition(PyCapsule_GetPointer(hSimConnect, NULL), DefineID, DatumName, UnitsName, DatumType, fEpsilon,
			DatumID);
}

HRESULT changeVehicle(PyObject* handle, const char *vehicleTitle)
{
	return SimConnect_ChangeVehicle(PyCapsule_GetPointer(handle, NULL), vehicleTitle);
}

HRESULT clearClientDataDefinition(PyObject *handle, SIMCONNECT_CLIENT_DATA_DEFINITION_ID defineID)
{
	return SimConnect_ClearClientDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID);
}

HRESULT clearDataDefinition(PyObject *handle, SIMCONNECT_DATA_DEFINITION_ID defineID)
{
	return SimConnect_ClearDataDefinition(PyCapsule_GetPointer(handle, NULL), defineID);
}

HRESULT clearInputGroup(PyObject *handle, SIMCONNECT_INPUT_GROUP_ID groupID)
{
	return SimConnect_ClearInputGroup(PyCapsule_GetPointer(handle, NULL), groupID);
}

HRESULT clearNotificationGroup(PyObject *handle, SIMCONNECT_NOTIFICATION_GROUP_ID groupID)
{
	return SimConnect_ClearNotificationGroup(PyCapsule_GetPointer(handle, NULL), groupID);
}

HRESULT close(PyObject *handle)
{
	return SimConnect_Close(PyCapsule_GetPointer(handle, NULL));
}

HRESULT createClientData(PyObject *handle, SIMCONNECT_CLIENT_DATA_ID dataID, DWORD dwSize, SIMCONNECT_CREATE_CLIENT_DATA_FLAG dataFlags)
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

HRESULT flightSave(PyObject *handle, const char *fileName, const char *title, const char *description, DWORD flags)
{
	return SimConnect_FlightSave(PyCapsule_GetPointer(handle, NULL), fileName, title, description, flags);
}

HRESULT mapInputEventToClientEvent(PyObject *handle, const int &eventGroup, const char *inputTrigger, const int &id)
{
	return SimConnect_MapInputEventToClientEvent(PyCapsule_GetPointer(handle, NULL), eventGroup, inputTrigger, id);
}

HRESULT requestDataOnSimObjectType(PyObject *handle, const SIMCONNECT_DATA_REQUEST_ID &id,
		const SIMCONNECT_DATA_DEFINITION_ID &dataDefinitionID, const DWORD &radius, const SIMCONNECT_SIMOBJECT_TYPE &objetID)
{
	return SimConnect_RequestDataOnSimObjectType(PyCapsule_GetPointer(handle, NULL), id, dataDefinitionID, radius, objetID);
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

tuple getLastSentPacketID(PyObject *handle)
{
	DWORD id;
	HRESULT result = SimConnect_GetLastSentPacketID(PyCapsule_GetPointer(handle, NULL), &id);
	return make_tuple(result, id);
}

tuple open(PCSTR szName, HWND hWnd, DWORD UserEventWin32, HANDLE hEventHandle, DWORD ConfigIndex)
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

HRESULT callDispatch(PyObject *handle, object callback, PyObject *content)
{
	_internal::__callback__ = &callback;
	return SimConnect_CallDispatch(PyCapsule_GetPointer(handle, NULL), _internal::__caller__, NULL);
}

} // end namespace wrapper
} // end namespace simconnect
} // end namespace prepar3d
