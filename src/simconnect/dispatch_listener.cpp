/*
 * dispatch_listener.cpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#include "dispatch_listener.hpp"

namespace prepar3d
{
namespace simconnect
{

DispatchListener::DispatchListener(PyObject *handle) :
		_handle(handle)
{

}

} // end namespace simconnect
} // end namespace prepar3d

