#ifndef __PYPREPAR3D_SIMCONNECT_DATATYPE_CONVERTER_HPP_
#define __PYPREPAR3D_SIMCONNECT_DATATYPE_CONVERTER_HPP_

#include "common.hpp"
#include <map>
#include <boost/function.hpp>

#define REGISTER_DATA_TYPE_CONVERTER(TYPE_NAME, TYPE, SIZE) _functionMap[SIMCONNECT_DATATYPE_ ## TYPE_NAME] = std::make_pair(SIZE / sizeof(DWORD), _internal::castToTypedObject<TYPE>)

namespace prepar3d
{

namespace simconnect
{

class DataTypeConverter
{
public:
	typedef boost::function<boost::python::object(void*)> FunctionType;
	typedef std::pair<std::size_t, FunctionType> SizeFunctionType;
	typedef std::map<SIMCONNECT_DATATYPE, SizeFunctionType> DataTypeConverterMapType;

	DataTypeConverter();
	void init();

	SizeFunctionType &getConverter(const SIMCONNECT_DATATYPE &dataType)
	{
		return _functionMap.at(dataType);
	}

private:
	DataTypeConverterMapType _functionMap;

};

namespace _internal
{
template<typename TYPE>
object castToTypedObject(void * const & source)
{

	return object(static_cast<TYPE *>(source));
}

} // end namespace _internal

} // end namespace simconnect
} // end namespace prepar3d

#endif // __PYPREPAR3D_SIMCONNECT_DATATYPE_CONVERTER_HPP_
