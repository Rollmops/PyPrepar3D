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
		std::cout << "dwData: " << ((SIMCONNECT_RECV_EVENT_BASE*) pData)->dwData  << std::endl;
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

HRESULT EventListener::subscribeSystemEvent(const char *eventName, const DWORD &recvID, object callable, const int &id, const SIMCONNECT_STATE &state)
{
	// TODO check for correct eventName
	EventIDCallbackType &callbackMap = eventMap[recvID];
	HANDLE handle = PyCObject_AsVoidPtr(_handle.get());
	HRESULT res = SimConnect_SubscribeToSystemEvent(handle, id, eventName);
	SimConnect_SetSystemEventState(handle, id, state);
	if (res == S_OK)
	{
		callbackMap[id] = callable;
	}
	return res;
}

HRESULT EventListener::subscribeInputEvent(const char *inputTrigger, object callable, const int &id, const SIMCONNECT_STATE &state, const DWORD &priority)
{

	EventIDCallbackType &callbackMap = eventMap[SIMCONNECT_RECV_ID_EVENT];
	HANDLE handle = PyCObject_AsVoidPtr(_handle.get());
	HRESULT hr;
    hr = SimConnect_MapClientEventToSimEvent(handle, id);

    // we are using -1 for the init group
    hr = SimConnect_AddClientEventToNotificationGroup(handle, -1, id);
    hr = SimConnect_SetNotificationGroupPriority(handle, -1, priority);

    hr = SimConnect_MapInputEventToClientEvent(handle, id, inputTrigger, id);
    hr = SimConnect_SetInputGroupState(handle, id, state);
    callbackMap[id] = callable;

	return S_OK;
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

