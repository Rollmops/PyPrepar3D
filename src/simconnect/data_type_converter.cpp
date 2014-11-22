#include "data_type_converter.hpp"
#include <boost/math/cstdfloat/cstdfloat_types.hpp>

namespace prepar3d {

namespace simconnect {

DataTypeConverter::DataTypeConverter()
{
	init();
}

void DataTypeConverter::init()
{
	REGISTER_DATA_TYPE_CONVERTER(INT32, int32_t);
	REGISTER_DATA_TYPE_CONVERTER(INT64, int64_t);
	REGISTER_DATA_TYPE_CONVERTER(FLOAT32, boost::float32_t);
	REGISTER_DATA_TYPE_CONVERTER(FLOAT64, double);

	REGISTER_DATA_TYPE_CONVERTER(STRING8, char*);
}
} // end namespace simconnect
} // end namespace prepar3d
