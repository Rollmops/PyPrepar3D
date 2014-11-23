#include "data_type_converter.hpp"
#include <boost/math/cstdfloat/cstdfloat_types.hpp>
#include <utility>

namespace prepar3d
{

namespace simconnect
{

namespace _internal
{

template<>
object castToTypedObject<std::string>(void * const & source)
{
	return object(std::string(static_cast<const char *>(source)));
}

} // end namespace _internal
DataTypeConverter::DataTypeConverter()
{
	init();
}

void DataTypeConverter::init()
{
	REGISTER_DATA_TYPE_CONVERTER(INT32, int32_t, sizeof(int32_t));
	REGISTER_DATA_TYPE_CONVERTER(INT64, int64_t, sizeof(int64_t));
	REGISTER_DATA_TYPE_CONVERTER(FLOAT32, boost::float32_t, sizeof(boost::float32_t));
	REGISTER_DATA_TYPE_CONVERTER(FLOAT64, boost::float64_t, sizeof(boost::float64_t));

	REGISTER_DATA_TYPE_CONVERTER(STRING8, std::string, 8);
	REGISTER_DATA_TYPE_CONVERTER(STRING32, std::string, 32);
	REGISTER_DATA_TYPE_CONVERTER(STRING64, std::string, 64);
	REGISTER_DATA_TYPE_CONVERTER(STRING128, std::string, 128);
	REGISTER_DATA_TYPE_CONVERTER(STRING256, std::string, 256);
	REGISTER_DATA_TYPE_CONVERTER(STRING260, std::string, 260);
	REGISTER_DATA_TYPE_CONVERTER(STRINGV, std::string, 512);

	REGISTER_DATA_TYPE_CONVERTER(XYZ, SIMCONNECT_DATA_XYZ, sizeof(SIMCONNECT_DATA_XYZ));
	REGISTER_DATA_TYPE_CONVERTER(LATLONALT, SIMCONNECT_DATA_LATLONALT, sizeof(SIMCONNECT_DATA_LATLONALT));

}

} // end namespace simconnect
} // end namespace prepar3d
