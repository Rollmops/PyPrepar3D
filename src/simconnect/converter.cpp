#include "converter.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace converter
{

void initializeConverters()
{
	to_python_converter<DWORD, prepar3d::simconnect::converter::FROM_DWORD>();
	to_python_converter<char, prepar3d::simconnect::converter::FROM_CHAR>();
	to_python_converter<unsigned char[8], prepar3d::simconnect::converter::FROM_TYPE_ARRAY<unsigned char, 8> >();
	to_python_converter<boost::shared_ptr<PyObject>, prepar3d::simconnect::converter::FROM_BOOST_SHARED_PTR>();
	to_python_converter<SIMCONNECT_DATA_GROUND_INFO[1], prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_GROUND_INFO, 1> >();
	to_python_converter<char[128], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<128> >();
	to_python_converter<char[64], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<64> >();
	to_python_converter<SIMCONNECT_DATA_FACILITY_VOR[1], prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_FACILITY_VOR, 1> >();
	to_python_converter<SIMCONNECT_DATA_FACILITY_TACAN[1],
			prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_FACILITY_TACAN, 1> >();
	to_python_converter<SIMCONNECT_DATA_FACILITY_NDB[1], prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_FACILITY_NDB, 1> >();
	to_python_converter<SIMCONNECT_DATA_FACILITY_WAYPOINT[1],
			prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_FACILITY_WAYPOINT, 1> >();
	to_python_converter<SIMCONNECT_DATA_FACILITY_AIRPORT[1],
			prepar3d::simconnect::converter::FROM_TYPE_ARRAY<SIMCONNECT_DATA_FACILITY_AIRPORT, 1> >();
	to_python_converter<char[9], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<9> >();
	to_python_converter<char[50], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<50> >();
	to_python_converter<char[30], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<30> >();
	to_python_converter<BYTE[1], prepar3d::simconnect::converter::FROM_TYPE_ARRAY<BYTE, 1> >();
	to_python_converter<char[1], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<1> >();
	to_python_converter<char[MAX_PATH], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<MAX_PATH> >();
	to_python_converter<char[256], prepar3d::simconnect::converter::FROM_CHAR_ARRAY<256> >();
}

}
}
}
