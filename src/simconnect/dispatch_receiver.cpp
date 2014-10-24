#include "dispatch_receiver.hpp"
#include "recv_type_converter.hpp"

namespace prepar3d
{
namespace simconnect
{

void DispatchReceiver::registerID(SIMCONNECT_RECV_ID id)
{
	_registeredIdList[id] = util::Singletons::get<RecvTypeConverter, 1>().getConverterForID(id);
}

tuple DispatchReceiver::getNextDispatchForHandle(PyObject *handle)
{
	if (!_registeredIdList.empty())
	{
		SIMCONNECT_RECV* pData;
		DWORD cbData;
		HRESULT res = SimConnect_GetNextDispatch(PyCObject_AsVoidPtr(handle), &pData, &cbData);
		std::map<SIMCONNECT_RECV_ID, FunctionType>::iterator iter = _registeredIdList.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
		if (iter != _registeredIdList.end())
		{
			RecvTypeConverter &converter = util::Singletons::get<RecvTypeConverter, 1>();
			return make_tuple(res, converter(pData), cbData);
		}
		else
		{
			return tuple();
		}
	}
	else
	{
		//TODO throw
		return tuple();
	}
}

} // end namespace simconnect
} // end namespace prepar3d
