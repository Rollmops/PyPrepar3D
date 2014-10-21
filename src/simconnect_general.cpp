#include "module_simconnect.hpp"
#include <boost/function.hpp>

namespace prepar3d
{

using namespace boost::python;
namespace _internal {
static object *__callback__;
}

tuple simconnect_open(PCSTR szName, HWND hWnd,
		DWORD UserEventWin32, HANDLE hEventHandle, DWORD ConfigIndex)
{
	HANDLE phSimConnect;
	const HRESULT result = SimConnect_Open(&phSimConnect, szName, hWnd, UserEventWin32,
			hEventHandle, ConfigIndex);

	return make_tuple(result, handle<>(borrowed(PyCObject_FromVoidPtr(phSimConnect, NULL))));
}

HRESULT simconnect_close(PyObject *handle)
{
	HRESULT ret = E_FAIL;
	HANDLE han = PyCObject_AsVoidPtr(handle);
	if( han != NULL ) {
		ret = SimConnect_Close(han);
	}
	return ret;
}

void CALLBACK MyDispatchProcDLL(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	_internal::__callback__->operator ()( pData, cbData, handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
}

enum EVENT_ID
{
	EVENT_ADDED_AIRCRAFT
};

HRESULT simconnect_calldispatch(PyObject *handle, object callback, PyObject *content)
{
	_internal::__callback__ = &callback;
//	boost::function<void(SIMCONNECT_RECV* , DWORD , void* )> f(callback);
//	DispatchProc fp = *f.target<DispatchProc>();
	SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(handle), EVENT_ADDED_AIRCRAFT, "Paused");
	return SimConnect_CallDispatch(PyCObject_AsVoidPtr(handle), MyDispatchProcDLL, NULL);
}

} // end namespace prepar3d
