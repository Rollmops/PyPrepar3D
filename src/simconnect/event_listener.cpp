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
	EventListener::EventMapType::const_iterator iter = __listener__->eventMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (iter != __listener__->eventMap.end())
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

EventListener::EventListener(PyObject *handle) :
		_handle(boost::shared_ptr<PyObject>(handle))
{
	_internal::__listener__ = this;
}


HRESULT EventListener::subscribeSystemEvent(const char *eventName, const int &recvID, object callable)
{
	// TODO check for correct eventName
	EventIDCallbackType &callbackVector = eventMap[recvID];
	HRESULT res = SimConnect_SubscribeToSystemEvent(PyCObject_AsVoidPtr(_handle.get()), callbackVector.size(), eventName);
	if (res == S_OK)
	{
		callbackVector.push_back(callable);
	}
	return res;
}

HRESULT EventListener::subscribeInputEvent(const char *inputTrigger, const int &recvID, object callable)
{
	EventIDCallbackType &callbackVector = eventMap[recvID];
	// create a private event
	HRESULT res1 = SimConnect_MapClientEventToSimEvent(PyCObject_AsVoidPtr(_handle.get()), callbackVector.size());
	HRESULT res2 = SimConnect_MapInputEventToClientEvent(PyCObject_AsVoidPtr(_handle.get()), 0, inputTrigger, callbackVector.size());
	// sign up for notifications
	HRESULT res3 = SimConnect_AddClientEventToNotificationGroup(PyCObject_AsVoidPtr(_handle.get()), 0, callbackVector.size());

	if ((res1 || res2 || res3) == S_OK)
	{
		callbackVector.push_back(callable);
	}
	std::cout << res1 << ":" << res2 << ":" << res3 << std::endl;
	return (res1 || res2 || res3);
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

