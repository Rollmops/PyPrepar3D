/*
 * dispatch_listener.hpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik Tuerke
 */

#ifndef __PREPAR3D_SIMCONNECT_DISPATCH_HANDLER_HPP_
#define __PREPAR3D_SIMCONNECT_DISPATCH_HANDLER_HPP_

#include "common.hpp"
#include <vector>
#include <map>

namespace prepar3d
{
namespace simconnect
{
class DispatchHandler
{
public:
	typedef std::map<DWORD, object> EventIDCallbackType;
	typedef std::map<DWORD, EventIDCallbackType> EventMapType;

	DispatchHandler(PyObject *handle);

	HRESULT subscribeSystemEvent(const char *eventName, const DWORD &recvID, object callable, const int &id, const SIMCONNECT_STATE &state);
	HRESULT subscribeInputEvent(const char *inputTrigger, object callable, const int &id, const SIMCONNECT_STATE &state, const DWORD &priority, const char *simEvent);
	void subscribeRecvIDEvent(const DWORD &recvID, object callable);

	void listen(const DWORD &sleepTime);

	EventMapType eventMap;
	EventIDCallbackType recvIdMap;

	boost::shared_ptr<PyObject> getHandle() const
	{
		return _handle;
	}

private:
	boost::shared_ptr<PyObject> _handle;

};

} // end namespace simconnect
} // end namespace prepar3d

#endif /* __PREPAR3D_SIMCONNECT_DISPATCH_HANDLER_HPP_ */