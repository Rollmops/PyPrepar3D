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
struct DummyObject
{
};

DispatchHandler *__dispatchHandler__;

void CALLBACK __dispatchCallback__(SIMCONNECT_RECV* pData, DWORD cbData, void *pContext)
{
	// handle all system events and input events
	DispatchHandler::EventMapType::const_iterator iter = __dispatchHandler__->eventMap.find(static_cast<DWORD>(pData->dwID));
	if (iter != __dispatchHandler__->eventMap.end())
	{
		const DispatchHandler::EventCallbackConverterType &callbackConverter = iter->second.at(
				((SIMCONNECT_RECV_EVENT_BASE*) pData)->uEventID);
		callbackConverter.first(callbackConverter.second(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}

	// handle all the RecvID events such as Exception Event
	DispatchHandler::EventIDCallbackType::const_iterator cb = __dispatchHandler__->recvIdMap.find(
			static_cast<SIMCONNECT_RECV_ID>(pData->dwID));
	if (cb != __dispatchHandler__->recvIdMap.end())
	{
		const DispatchHandler::EventCallbackConverterType &callbackConverter = cb->second;
		callbackConverter.first(callbackConverter.second(pData), cbData/*, handle<>(PyCapsule_New(pContext, NULL, NULL))*/);
	}

	if (pData->dwID == SIMCONNECT_RECV_ID_SIMOBJECT_DATA)
	{
		const SIMCONNECT_RECV_SIMOBJECT_DATA *pObjData = (const SIMCONNECT_RECV_SIMOBJECT_DATA *) pData;
		const DispatchHandler::DataEventObjectStructureInfoType &callbackDataTypeList = __dispatchHandler__->dataEventMap.at(
				pObjData->dwRequestID);
		const DispatchHandler::DataEventStructureInfoType &structureInfo = callbackDataTypeList.get<1>();
		size_t pos = 0;
		boost::python::dict *dataStructure = callbackDataTypeList.get<2>().get();
		for (DispatchHandler::DataEventStructureInfoType::const_iterator iter = structureInfo.begin(); iter != structureInfo.end(); ++iter)
		{
			const DataTypeConverter::SizeFunctionType &sizeConverter = iter->second;
			dataStructure->operator [](iter->first.c_str()) = sizeConverter.second((void*) &((&pObjData->dwData)[pos]));
			pos += sizeConverter.first;

		}
		callbackDataTypeList.get<0>()(*dataStructure);
	}
}

} // end namespace _internal

DispatchHandler::DispatchHandler(PyObject *handle) :
		_handle(boost::shared_ptr<PyObject>(handle))
{
	_internal::__dispatchHandler__ = this;
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

HRESULT DispatchHandler::subscribeDataEvent(list simulation_varaibles, const int &id, object callable, const SIMCONNECT_PERIOD &period,
		const DWORD &flag)
{
	const boost::python::ssize_t n = boost::python::len(simulation_varaibles);
	const HANDLE handle = PyCapsule_GetPointer(_handle.get(), NULL);

	DataEventStructureInfoType dataTypeList;
	HRESULT ret = S_OK;
	for (boost::python::ssize_t i = 0; i < n; ++i)
	{
		boost::python::object simulation_variable = extract<object>(simulation_varaibles[i]);

		const char * dataName = extract<const char *>(simulation_variable.attr("_name"));
		const char * dataUnit = extract<const char *>(simulation_variable.attr("_unit"));
		const char * attribute = extract<const char *>(simulation_variable.attr("_key"));
		const SIMCONNECT_DATATYPE &dataType = extract<SIMCONNECT_DATATYPE>(simulation_variable.attr("_data_type"));

		const DataTypeConverter::SizeFunctionType &sizeFunction = util::Singletons::get<DataTypeConverter, 1>().getConverter(dataType);
		dataTypeList.push_back(std::make_pair(std::string(attribute), sizeFunction));
		ret = ret || SimConnect_AddToDataDefinition(handle, id, dataName, strlen(dataUnit) > 0 ? dataUnit : NULL, dataType);
	}

	ret = ret || SimConnect_RequestDataOnSimObject(handle, id, id, SIMCONNECT_OBJECT_ID_USER, period, flag);
	if (ret == S_OK)
	{
		dataEventMap[id] = boost::make_tuple(callable, dataTypeList, boost::shared_ptr<boost::python::dict>(new boost::python::dict()));
	}
	return ret;
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

