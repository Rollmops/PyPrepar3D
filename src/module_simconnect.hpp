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

namespace prepy3d {

void simconnect_open(const std::string &test)
{
	std::cout << "Toll: " << test << std::endl;
}

} // end namespace prepy3d

#endif /* __PREPY3D_MODULE_SIMCONNECT_HPP_ */
