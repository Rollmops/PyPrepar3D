#include "wrapper.hpp"

#include "dispatch_receiver.hpp"

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
	_internal::__callback__->operator ()(pData, cbData,
			handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
}
} // end namespace _internal

HRESULT addClientEventToNotificationGroup(PyObject *handle,
		SIMCONNECT_NOTIFICATION_GROUP_ID groupID,
		SIMCONNECT_CLIENT_EVENT_ID eventID, bool bMaskable)
{
	return SimConnect_AddClientEventToNotificationGroup(
			PyCObject_AsVoidPtr(handle), groupID, eventID, bMaskable);
}

HRESULT addToClientDataDefinition(PyObject *handle,
		SIMCONNECT_CLIENT_DATA_DEFINITION_ID defineID, DWORD dwOffset,
		DWORD dwSizeOrType, float fEpsilon, DWORD datumID)
{
	return SimConnect_AddToClientDataDefinition(PyCObject_AsVoidPtr(handle),
			defineID, dwOffset, dwSizeOrType, fEpsilon, datumID);
}

HRESULT addToDataDefinition(PyObject *hSimConnect,
		SIMCONNECT_DATA_DEFINITION_ID DefineID, const char* DatumName,
		const char* UnitsName, SIMCONNECT_DATATYPE DatumType, float fEpsilon,
		DWORD DatumID)
{
	return SimConnect_AddToDataDefinition(PyCObject_AsVoidPtr(hSimConnect),
			DefineID, DatumName, UnitsName, DatumType, fEpsilon, DatumID);
}

HRESULT changeVehicle(PyObject* handle, const char *vehicleTitle)
{
	return SimConnect_ChangeVehicle(PyCObject_AsVoidPtr(handle), vehicleTitle);
}

HRESULT clearClientDataDefinition(PyObject *handle,
		SIMCONNECT_CLIENT_DATA_DEFINITION_ID defineID)
{
	return SimConnect_ClearClientDataDefinition(PyCObject_AsVoidPtr(handle),
			defineID);
}

HRESULT clearDataDefinition(PyObject *handle,
		SIMCONNECT_DATA_DEFINITION_ID defineID)
{
	return SimConnect_ClearDataDefinition(PyCObject_AsVoidPtr(handle), defineID);
}

HRESULT clearInputGroup(PyObject *handle, SIMCONNECT_INPUT_GROUP_ID groupID)
{
	return SimConnect_ClearInputGroup(PyCObject_AsVoidPtr(handle), groupID);
}

HRESULT clearNotificationGroup(PyObject *handle,
		SIMCONNECT_NOTIFICATION_GROUP_ID groupID)
{
	return SimConnect_ClearNotificationGroup(PyCObject_AsVoidPtr(handle),
			groupID);
}

HRESULT close(PyObject *handle)
{
	return SimConnect_Close(PyCObject_AsVoidPtr(handle));
}

HRESULT createClientData(PyObject *handle, SIMCONNECT_CLIENT_DATA_ID dataID,
		DWORD dwSize, SIMCONNECT_CREATE_CLIENT_DATA_FLAG dataFlags)
{
	return SimConnect_CreateClientData(PyCObject_AsVoidPtr(handle), dataID,
			dwSize, dataFlags);
}

HRESULT flightLoad(PyObject *handle, const char* fileName)
{
	return SimConnect_FlightLoad(PyCObject_AsVoidPtr(handle), fileName);
}

HRESULT flightPlanLoad(PyObject *handle, const char* fileName)
{
	return SimConnect_FlightPlanLoad(PyCObject_AsVoidPtr(handle), fileName);
}

HRESULT flightSave(PyObject *handle, const char *fileName, const char *title,
		const char *description, DWORD flags)
{
	return SimConnect_FlightSave(PyCObject_AsVoidPtr(handle), fileName, title,
			description, flags);
}

tuple getLastSentPacketID(PyObject *handle)
{
	DWORD id;
	HRESULT result = SimConnect_GetLastSentPacketID(PyCObject_AsVoidPtr(handle), &id);
	return make_tuple(result, id);
}

void registerSimConnectRecvId(SIMCONNECT_RECV_ID id)
{
	util::Singletons::get<DispatchReceiver, 1>().registerID(id);
}

 tuple getNextDispatch(PyObject *handle)
{
	 DispatchReceiver &receiver = util::Singletons::get<DispatchReceiver, 1>();
	 return receiver(PyCObject_AsVoidPtr(handle));
}

tuple open(PCSTR szName, HWND hWnd, DWORD UserEventWin32, HANDLE hEventHandle,
		DWORD ConfigIndex)
{
	HANDLE phSimConnect;
	const HRESULT result = SimConnect_Open(&phSimConnect, szName, hWnd,
			UserEventWin32, hEventHandle, ConfigIndex);

	//TODO check if we need to borrow the object
	return make_tuple(result,
			handle<>(PyCObject_FromVoidPtr(phSimConnect, NULL)));
}

HRESULT subscribeToSystemEvent(PyObject *handle,
		SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName)
{
	return SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(handle),
			eventID, systemEventName);
}

HRESULT callDispatch(PyObject *handle, object callback, PyObject *content)
{
	_internal::__callback__ = &callback;
	return SimConnect_CallDispatch(PyCObject_AsVoidPtr(handle),
			_internal::__caller__, NULL);
}

} // end namespace wrapper
} // end namespace simconnect
} // end namespace prepar3d
