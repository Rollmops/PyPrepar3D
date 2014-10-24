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
	DispatchListener::SystemEventMapType::iterator iter = __listener__->systemEventMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (iter != __listener__->systemEventMap.end())
	{
		DispatchListener::EventIDCallbackType::iterator callback = iter->second.find(((SIMCONNECT_RECV_EVENT_BASE *) pData)->uEventID);
		if (callback != iter->second.end())
		{
			const RecvTypeConverter &converter = util::Singletons::get<RecvTypeConverter, 1>();
			object &callFunc = callback->second;
			callFunc.operator ()(converter(pData), cbData, handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
		}
	}

}
} // end namepsace _internal

DispatchListener::DispatchListener(PyObject *handle) :
		_handle(handle), _sleepTime(100)
{
	_internal::__listener__ = this;
}

void DispatchListener::subscribe(const SIMCONNECT_RECV_ID &id, object callable)
{
}

HRESULT DispatchListener::subscribeSystemEvent(const char *eventName, const SIMCONNECT_RECV_ID &recvID, object callable)
{
	// TODO check for correct eventName
	DWORD id = 0;
	HRESULT res = SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(_handle), id, eventName);
	if (res == S_OK)
	{
		systemEventMap[recvID][id] = callable;
	}
	return res;
}

void DispatchListener::listen()
{
	HRESULT res = S_OK;
	while (res == S_OK)
	{
		res = SimConnect_CallDispatch(PyCObject_AsVoidPtr(_handle), _internal::__dispatchCallback__, NULL);
		Sleep(_sleepTime);
	}
}

} // end namespace simconnect
} // end namespace prepar3d

