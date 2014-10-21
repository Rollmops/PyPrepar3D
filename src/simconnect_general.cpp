#include "module_simconnect.hpp"

namespace prepar3d
{

using namespace boost::python;

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
	return SimConnect_Close(PyCObject_AsVoidPtr(handle));
}

} // end namespace prepar3d
