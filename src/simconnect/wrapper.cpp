#include "wrapper.hpp"

namespace prepar3d {
namespace simconnect {
namespace wrapper {

using namespace boost::python;

namespace _internal {
static object *__callback__;
void CALLBACK __caller__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext) {
	_internal::__callback__->operator ()(pData, cbData,
			handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
}
} // end namespace _internal

HRESULT addClientEventToNotificationGroup(PyObject *handle, SIMCONNECT_NOTIFICATION_GROUP_ID groupID, SIMCONNECT_CLIENT_EVENT_ID eventID, bool bMaskable)
{
	return SimConnect_AddClientEventToNotificationGroup(PyCObject_AsVoidPtr(handle), groupID, eventID, bMaskable);
}

HRESULT addToClientDataDefinition(PyObject *handle, SIMCONNECT_CLIENT_DATA_DEFINITION_ID  defineID, DWORD dwOffset, DWORD  dwSizeOrType, float  fEpsilon, DWORD  datumID ) {
	return SimConnect_AddToClientDataDefinition(PyCObject_AsVoidPtr(handle), defineID, dwOffset, dwSizeOrType, fEpsilon, datumID);
}

tuple open(PCSTR szName, HWND hWnd, DWORD UserEventWin32,
		HANDLE hEventHandle, DWORD ConfigIndex) {
	HANDLE phSimConnect;
	const HRESULT result = SimConnect_Open(&phSimConnect, szName, hWnd,
			UserEventWin32, hEventHandle, ConfigIndex);

	//TODO check if we need to borrow the object
	return make_tuple(result,
			handle<>(PyCObject_FromVoidPtr(phSimConnect, NULL)));
}

HRESULT close(PyObject *handle) {
	HRESULT ret = E_FAIL;
	HANDLE han = PyCObject_AsVoidPtr(handle);
	if (han != NULL) {
		ret = SimConnect_Close(han);
	}
	return ret;
}

HRESULT subscribeToSystemEvent(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName)
{
	return SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(handle), eventID, systemEventName);
}

HRESULT callDispatch(PyObject *handle, object callback,
		PyObject *content) {
	_internal::__callback__ = &callback;
	return SimConnect_CallDispatch(PyCObject_AsVoidPtr(handle),
			_internal::__caller__, NULL);
}

} // end namespace wrapper
} // end namespace simconnect
} // end namespace prepar3d
