/*
 * dispatch_listener.hpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik Tuerke
 */

#ifndef __PREPAR3D_SIMCONNECT_DISPATCH_LISTENER_HPP_
#define __PREPAR3D_SIMCONNECT_DISPATCH_LISTENER_HPP_

#include "common.hpp"

namespace prepar3d
{
namespace simconnect
{

class DispatchListener
{
public:
	DispatchListener(PyObject *handle);

private:
	PyObject *_handle;
};

} // end namespace simconnect
} // end namespace prepar3d

#endif /* __PREPAR3D_SIMCONNECT_DISPATCH_LISTENER_HPP_ */
