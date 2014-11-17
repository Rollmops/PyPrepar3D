/*
 * dispatch_listener.cpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#include "event_listener.hpp"
#include "recv_type_converter.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace _internal
{
static EventListener *__listener__;
void CALLBACK __eventCallback__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	const RecvTypeConverter &converter = util::Singletons::get<RecvTypeConverter, 1>();
	EventListener::EventMapType::const_iterator iter = __listener__->eventMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (iter != __listener__->eventMap.end())
	{
		const object &callback = iter->second.at(((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID);
		callback(converter(pData), cbData, handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
	}

	EventListener::EventIDCallbackType::const_iterator cb = __listener__->genericEventMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if( cb != __listener__->genericEventMap.end())
	{
		cb->second(converter(pData), cbData, handle<>(PyCObject_FromVoidPtr(pContext, NULL)));
	}
}
} // end namepsace _internal

EventListener::EventListener(PyObject *handle) :
		_handle(boost::shared_ptr<PyObject>(handle))
{
	_internal::__listener__ = this;
}

HRESULT EventListener::subscribeSystemEvent(const char *eventName, const DWORD &recvID, object callable, const DWORD &id)
{
	// TODO check for correct eventName
	EventIDCallbackType &callbackVector = eventMap[recvID];
	HRESULT res = SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(_handle.get()), id, eventName);
	if (res == S_OK)
	{
		callbackVector[id] = callable;
	}
	return res;
}

HRESULT EventListener::subscribeInputEvent(const char *inputTrigger, const DWORD &recvID, object callable, const DWORD &id)
{
	EventIDCallbackType &callbackVector = eventMap[recvID];
	// create a private event
	HRESULT res1 = SimConnect_MapInputEventToClientEvent(PyCObject_AsVoidPtr(_handle.get()), 0, inputTrigger, id);
	// sign up for notifications
	HRESULT res2 = SimConnect_AddClientEventToNotificationGroup(PyCObject_AsVoidPtr(_handle.get()), 0, id);

	HRESULT res3 = SimConnect_SetInputGroupState(PyCObject_AsVoidPtr(_handle.get()), 0, SIMCONNECT_STATE_ON);

	if ((res1 || res2 || res3) == S_OK)
	{
		callbackVector[id] = callable;
	}
	return (res1 || res2 || res3);
}

void EventListener::subscribe( const DWORD &recvID, object callable )
{
	genericEventMap[recvID] = callable;
}

void EventListener::listen(const float &frequency)
{
	const DWORD sleepTime = (float) 1000 / frequency;
	HRESULT res = S_OK;
	while (res == S_OK)
	{
		res = SimConnect_CallDispatch(PyCObject_AsVoidPtr(_handle.get()), _internal::__eventCallback__, NULL);
		Sleep(sleepTime);
	}
}

} // end namespace simconnect
} // end namespace prepar3d

