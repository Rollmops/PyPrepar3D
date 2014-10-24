#include "dispatch_receiver.hpp"

namespace prepar3d {
namespace simconnect {

void DispatchReceiver::init()
{
	_functionMap[SIMCONNECT_RECV_ID_OPEN] =	_internal::castToRecvType<SIMCONNECT_RECV_OPEN>;
	_functionMap[SIMCONNECT_RECV_ID_EVENT] = _internal::castToRecvType<SIMCONNECT_RECV_EVENT>;
}

void DispatchReceiver::registerID(SIMCONNECT_RECV_ID id)
{
	_registeredIdList[id] = _functionMap.at(id);
}

tuple DispatchReceiver::getNextDispatchForHandle(PyObject *handle) {
	if (!_registeredIdList.empty())
	{
		SIMCONNECT_RECV* pData;
		DWORD cbData;
		HRESULT res = SimConnect_GetNextDispatch(PyCObject_AsVoidPtr(handle), &pData, &cbData);
		std::map<SIMCONNECT_RECV_ID, FunctionType>::iterator iter = _registeredIdList.find(	static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
		if (iter != _registeredIdList.end()) {
			return make_tuple(res, iter->second(pData), cbData);
		} else {
			return tuple();
		}
	} else {
		//TODO throw
		return tuple();
	}
}

} // end namespace simconnect
} // end namespace prepar3d
