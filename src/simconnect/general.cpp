#include <boost/function.hpp>

#include "module.hpp"

namespace prepar3d {

using namespace boost::python;
namespace _internal {
static object *__callback__;
void CALLBACK __caller__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext) {
	_internal::__callback__->operator ()(pData, cbData,
			handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
}

}

tuple simconnect_open(PCSTR szName, HWND hWnd, DWORD UserEventWin32,
		HANDLE hEventHandle, DWORD ConfigIndex) {
	HANDLE phSimConnect;
	const HRESULT result = SimConnect_Open(&phSimConnect, szName, hWnd,
			UserEventWin32, hEventHandle, ConfigIndex);

	return make_tuple(result,
			handle<>(borrowed(PyCObject_FromVoidPtr(phSimConnect, NULL))));
}

HRESULT simconnect_close(PyObject *handle) {
	HRESULT ret = E_FAIL;
	HANDLE han = PyCObject_AsVoidPtr(handle);
	if (han != NULL) {
		ret = SimConnect_Close(han);
	}
	return ret;
}

HRESULT simconnect_subscribe_to_system_event(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName)
{
	return SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(handle), eventID, systemEventName);
}

HRESULT simconnect_calldispatch(PyObject *handle, object callback,
		PyObject *content) {
	_internal::__callback__ = &callback;
	return SimConnect_CallDispatch(PyCObject_AsVoidPtr(handle),
			_internal::__caller__, NULL);
}

} // end namespace prepar3d
