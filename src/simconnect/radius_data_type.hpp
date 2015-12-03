/*
 * radius_data_type.hpp
 *
 *  Created on: 02.12.2015
 *      Author: erik_
 */

#ifndef SRC_SIMCONNECT_RADIUS_DATA_TYPE_HPP_
#define SRC_SIMCONNECT_RADIUS_DATA_TYPE_HPP_

#include "SimConnect.h"

namespace pyprepar3d
{

struct RadiusDataType
{

	SIMCONNECT_DATA_DEFINITION_ID dataDefinitionID;
	DWORD radius;
	SIMCONNECT_SIMOBJECT_TYPE simObjectType;

};

} // end namespace pyprepar3d

#endif /* SRC_SIMCONNECT_RADIUS_DATA_TYPE_HPP_ */
