/*
 * dispatch_listener.cpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#include "dispatch_handler.hpp"

#include "recv_type_converter.hpp"
#include "data_type_converter.hpp"

#include <boost/python/stl_iterator.hpp>

namespace prepar3d
{
namespace simconnect
{
namespace _internal
{
static DispatchHandler *__listener__;

void CALLBACK __dispatchCallback__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	// handle all system events and input events
	DispatchHandler::EventMapType::const_iterator iter = __listener__->eventMap.find(static_cast<DWORD>(pData->dwID));
	if (iter != __listener__->eventMap.end())
	{
		const DispatchHandler::EventCallbackConverterType &callbackConverter = iter->second.at(
				((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID);
		callbackConverter.first(callbackConverter.second(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}

	// handle all the RecvID events such as Exception Event
	DispatchHandler::EventIDCallbackType::const_iterator cb = __listener__->recvIdMap.find(static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (cb != __listener__->recvIdMap.end())
	{
		const DispatchHandler::EventCallbackConverterType &callbackConverter = cb->second;
		callbackConverter.first(callbackConverter.second(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}

	if (pData->dwID == SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE)
	{

		const SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE *pObjData = (const SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE *) pData;
		const DispatchHandler::DataEventObjectStructureInfoType &callbackDataTypeList = __listener__->dataEventMap.at(
				pObjData->dwRequestID);
		const object &callback = callbackDataTypeList.first;
		const DispatchHandler::DataEventStructureInfoType &structureInfo = callbackDataTypeList.second;

		assert(structureInfo.size() == pObjData->dwDefineCount);
		size_t pos = 0;
		// test
		boost::python::dict structure;
		for (DispatchHandler::DataEventStructureInfoType::const_iterator iter = structureInfo.begin(); iter != structureInfo.end(); ++iter)
		{
			structure[iter->first]
					  = iter->second((void*)&((&pObjData->dwData)[pos]));
			pos += sizeof(double);
		}
		callback(structure);

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
		callbackMap[id] = std::make_pair(callable,
				util::Singletons::get<RecvTypeConverter, 1>().getConverterForID(static_cast<SIMCONNECT_RECV_ID>(recvID)));
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
		callbackMap[id] = std::make_pair(callable,
				util::Singletons::get<RecvTypeConverter, 1>().getConverterForID(SIMCONNECT_RECV_ID_EVENT));
		return S_OK;
	}
	else
	{
		return E_FAIL;
	}
}

void DispatchHandler::subscribeRecvIDEvent(const DWORD &recvID, object callable)
{
	recvIdMap[recvID] = std::make_pair(callable,
			util::Singletons::get<RecvTypeConverter, 1>().getConverterForID(static_cast<SIMCONNECT_RECV_ID>(recvID)));
}

HRESULT DispatchHandler::subscribeDataEvent(list data_fields, const int &id, object callable)
{
	const boost::python::ssize_t n = boost::python::len(data_fields);
	const HANDLE handle = PyCapsule_GetPointer(_handle.get(), NULL);

	char *dataName;
	char *unitsName;
	SIMCONNECT_DATATYPE dataType;
	DataEventStructureInfoType dataTypeList;

	for (boost::python::ssize_t i = 0; i < n; ++i)
	{
		boost::python::tuple elem = extract<tuple>(data_fields[i]);
		const boost::python::ssize_t length = boost::python::len(elem);
		assert(length >= 2);
		dataName = extract<char *>(elem[0]);
		unitsName = extract<char *>(elem[1]);
		dataType = SIMCONNECT_DATATYPE_FLOAT64;
		if (boost::python::len(elem) == 3)
		{
			dataType = extract<SIMCONNECT_DATATYPE>(elem[3]);
		}
		dataTypeList.push_back(std::make_pair(std::string(dataName), util::Singletons::get<DataTypeConverter, 1>().getConverter(dataType)));
		SimConnect_AddToDataDefinition(handle, 0, dataName, strlen(unitsName) == 0 ? NULL : unitsName, dataType);
	}

	SimConnect_RequestDataOnSimObjectType(handle, id, 0, 0, SIMCONNECT_SIMOBJECT_TYPE_USER);
	dataEventMap[id] = std::make_pair(callable, dataTypeList);
	return S_OK;
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

