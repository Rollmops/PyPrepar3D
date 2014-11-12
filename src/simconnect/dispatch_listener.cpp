/*
 * dispatch_listener.cpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#include "dispatch_listener.hpp"
#include "recv_type_converter.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace _internal
{
static DispatchListener *__listener__;
void CALLBACK __dispatchCallback__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	DispatchListener::SystemEventMapType::const_iterator iter = __listener__->systemEventMap.find(
			static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (iter != __listener__->systemEventMap.end())
	{
		if (((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID < iter->second.size())
		{
			const RecvTypeConverter &converter = util::Singletons::get<RecvTypeConverter, 1>();
			iter->second[((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID].operator ()(converter(pData), cbData,
					handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
		}
	}
}
} // end namepsace _internal

DispatchListener::DispatchListener(PyObject *handle) :
		_handle(handle)
{
	_internal::__listener__ = this;
}

void DispatchListener::subscribe(const SIMCONNECT_RECV_ID &id, object callable)
{
}

HRESULT DispatchListener::subscribeSystemEvent(const char *eventName, const SIMCONNECT_RECV_ID &recvID, object callable)
{
	// TODO check for correct eventName
	EventIDCallbackType &callbackVector = systemEventMap[recvID];
	HRESULT res = SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(_handle), callbackVector.size(), eventName);
	if (res == S_OK)
	{
		callbackVector.push_back(callable);
	}
	return res;
}

void DispatchListener::listen(const float &frequency)
{
	const DWORD sleepTime = (float)1000 / frequency;
	HRESULT res = S_OK;
	while (res == S_OK)
	{
		res = SimConnect_CallDispatch(PyCObject_AsVoidPtr(_handle), _internal::__dispatchCallback__, NULL);
		Sleep(sleepTime);
	}
}

} // end namespace simconnect
} // end namespace prepar3d

