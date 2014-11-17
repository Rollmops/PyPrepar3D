/*
 * dispatch_listener.hpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik Tuerke
 */

#ifndef __PREPAR3D_SIMCONNECT_EVENT_LISTENER_HPP_
#define __PREPAR3D_SIMCONNECT_EVENT_LISTENER_HPP_

#include "common.hpp"
#include <vector>
#include <map>

namespace prepar3d
{
namespace simconnect
{
class EventListener
{
public:
	typedef std::map<DWORD, object> EventIDCallbackType;
	typedef std::map<DWORD, EventIDCallbackType> EventMapType;

	EventListener(PyObject *handle);

	HRESULT subscribeSystemEvent(const char *eventName, const DWORD &recvID, object callable, const DWORD &id);
	HRESULT subscribeInputEvent(const char *inputTrigger, const DWORD &recvID, object callable, const DWORD &id);
	void EventListener::subscribe(const DWORD &recvID, object callable);

	void listen(const float &frequency);

	EventMapType eventMap;
	EventIDCallbackType genericEventMap;

	boost::shared_ptr<PyObject> getHandle() const
	{
		return _handle;
	}

private:
	boost::shared_ptr<PyObject> _handle;

};

} // end namespace simconnect
} // end namespace prepar3d

#endif /* __PREPAR3D_SIMCONNECT_EVENT_LISTENER_HPP_ */
