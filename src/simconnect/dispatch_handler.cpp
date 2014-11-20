/*
 * dispatch_listener.cpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#include "dispatch_handler.hpp"

#include "recv_type_converter.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace _internal
{
static DispatchHandler *__listener__;

void CALLBACK __dispatchCallback__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	const RecvTypeConverter &converter = util::Singletons::get<RecvTypeConverter, 1>();

	// handle all system events and input events
	DispatchHandler::EventMapType::const_iterator iter = __listener__->eventMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (iter != __listener__->eventMap.end())
	{
		const object &callback = iter->second.at(((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID);
		callback(converter(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}

	// handle all the RecvID events such as Exception Event
	DispatchHandler::EventIDCallbackType::const_iterator cb = __listener__->recvIdMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (cb != __listener__->recvIdMap.end())
	{
		cb->second(converter(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}
}
} // end namepsace _internal

DispatchHandler::DispatchHandler(PyObject *handle) :
		_handle(boost::shared_ptr<PyObject>(handle))
{
	_internal::__listener__ = this;
}

HRESULT DispatchHandler::subscribeSystemEvent(const char *eventName, const DWORD &recvID, object callable, const int &id,
		const SIMCONNECT_STATE &state)
{
	EventIDCallbackType &callbackMap = eventMap[recvID];
	HANDLE handle = PyCapsule_GetPointer(_handle.get(), NULL);
	HRESULT res = SimConnect_SubscribeToSystemEvent(handle, id, eventName);
	SimConnect_SetSystemEventState(handle, id, state);
	if (res == S_OK)
	{
		callbackMap[id] = callable;
	}
	return res;
}

HRESULT DispatchHandler::subscribeInputEvent(const char *inputTrigger, object callable, const int &id, const SIMCONNECT_STATE &state,
		const DWORD &priority, const char *simEvent)
{
	assert(id > 0);
	EventIDCallbackType &callbackMap = eventMap[SIMCONNECT_RECV_ID_EVENT];
	HANDLE handle = PyCapsule_GetPointer(_handle.get(), NULL);
	const HRESULT hr1 = SimConnect_MapClientEventToSimEvent(handle, id, simEvent);

	// we are using 0 for the init group
	const HRESULT hr2 = SimConnect_AddClientEventToNotificationGroup(handle, 0, id);
	const HRESULT hr3 = SimConnect_SetNotificationGroupPriority(handle, 0, priority);

	const HRESULT hr4 = SimConnect_MapInputEventToClientEvent(handle, id, inputTrigger, id);
	const HRESULT hr5 = SimConnect_SetInputGroupState(handle, id, state);

	if ((hr1 || hr2 || hr3 || hr4 || hr5) == 0)
	{
		callbackMap[id] = callable;
		return S_OK;
	}
	else
	{
		return E_FAIL;
	}
}

void DispatchHandler::subscribeRecvIDEvent(const DWORD &recvID, object callable)
{
	recvIdMap[recvID] = callable;
}

void DispatchHandler::listen(const DWORD &sleepTime)
{
	HRESULT res = S_OK;
	while (res == S_OK)
	{
		res = SimConnect_CallDispatch(PyCapsule_GetPointer(_handle.get(), NULL), _internal::__dispatchCallback__, NULL);
		Sleep(sleepTime);
	}
}

} // end namespace simconnect
} // end namespace prepar3d

