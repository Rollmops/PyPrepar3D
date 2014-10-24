#include "dispatch_receiver.hpp"

namespace prepar3d {
namespace simconnect {

DispatchReceiver::DispatchReceiver() {
	_functionMap[SIMCONNECT_RECV_ID_OPEN] =
			castToRecvType<SIMCONNECT_RECV_OPEN>;
}

void DispatchReceiver::registerID(SIMCONNECT_RECV_ID id)
{
	_registeredIdList[id] = _functionMap.at(id);
}

tuple DispatchReceiver::operator()(HANDLE handle) {
	if (!_registeredIdList.empty())
	{
		SIMCONNECT_RECV* pData;
		DWORD cbData;
		HRESULT res = SimConnect_GetNextDispatch(handle, &pData, &cbData);
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
