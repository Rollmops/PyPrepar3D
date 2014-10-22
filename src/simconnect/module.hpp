/*
 * module_simconnect.hpp
 *
 *  Created on: 21.10.2014
 *      Author: qxh6010
 */

#ifndef __PYPREPAR3D_MODULE_SIMCONNECT_HPP_
#define __PYPREPAR3D_MODULE_SIMCONNECT_HPP_

#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <iostream>
#include <boost/python.hpp>

#include "SimConnect.h"

namespace prepar3d {

boost::python::tuple simconnect_open(LPCSTR szName, HWND  hWnd, DWORD  UserEventWin32, HANDLE  hEventHandle, DWORD  ConfigIndex);
HRESULT simconnect_close(PyObject *handle);
HRESULT simconnect_subscribe_to_system_event(PyObject *handle, SIMCONNECT_CLIENT_EVENT_ID eventID, const char *systemEventName);
HRESULT simconnect_calldispatch(PyObject *handle, boost::python::object callback, PyObject *content);

void test_handle(HANDLE han);

} // end namespace prepar3d

#endif /* __PYPREPAR3D_MODULE_SIMCONNECT_HPP_ */
