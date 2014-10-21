/*
 * module_simconnect.hpp
 *
 *  Created on: 21.10.2014
 *      Author: qxh6010
 */

#ifndef __PREPY3D_MODULE_SIMCONNECT_HPP_
#define __PREPY3D_MODULE_SIMCONNECT_HPP_

#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include "SimConnect.h"
#include <boost/python.hpp>
#include <iostream>


#define ADD_ATTRIBUTE(SCOPE, ATTRIBUTE) SCOPE->attr(#ATTRIBUTE) = ATTRIBUTE

namespace prepar3d {
namespace _internal {
void define_constants(boost::python::scope *scope);
}

boost::python::tuple simconnect_open(LPCSTR szName, HWND  hWnd, DWORD  UserEventWin32, HANDLE  hEventHandle, DWORD  ConfigIndex);
HRESULT simconnect_close(PyObject *handle);
HRESULT simconnect_subscribe_to_system_event(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName);
HRESULT simconnect_calldispatch(PyObject *handle, boost::python::object callback, PyObject *content);

void test_handle(HANDLE han);

} // end namespace prepar3d

#endif /* __PREPY3D_MODULE_SIMCONNECT_HPP_ */
