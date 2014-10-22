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

#define ADD_ATTRIBUTE(SCOPE, ATTRIBUTE) SCOPE->attr(#ATTRIBUTE) = ATTRIBUTE

#define ENUM(NAME) boost::python::enum_<NAME>(#NAME)
#define ENUM_VALUE(NAME) .value(#NAME, NAME)

#define STRUCT(NAME) boost::python::class_<NAME>(#NAME)
#define STRUCT_DERIVED(NAME, DERIVED) boost::python::class_<NAME, bases<DERIVED> >(#NAME)
#define STRUCT_VALUE(NAME, STRUCT_NAME) .def_readwrite(#NAME, &STRUCT_NAME::NAME)

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

#endif /* __PYPREPAR3D_MODULE_SIMCONNECT_HPP_ */
