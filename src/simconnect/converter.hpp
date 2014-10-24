#ifndef __PYPREPAR3D_CONVERTER_HPP_
#define __PYPREPAR3D_CONVERTER_HPP_

#include "common.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace converter
{

struct FROM_DWORD
{
	static PyObject *convert(const DWORD &value)
	{
		return PyLong_FromUnsignedLong(value);
	}
};

struct FROM_CHAR
{
	static PyObject *convert(const char &value)
	{
		return boost::python::incref(boost::python::object(value).ptr());
	}
};

template<unsigned int LENGTH>
struct FROM_CHAR_ARRAY
{
	static PyObject *convert(char array[LENGTH])
	{
		return PyString_FromString(array);
	}
};

template<typename TYPE, unsigned int LENGTH>
struct FROM_TYPE_ARRAY
{
	static PyObject *convert(TYPE array[LENGTH])
	{
		boost::python::list ret;
		for (unsigned int i = 0; i < LENGTH; ++i)
		{
			ret.append(array[i]);
		}
		return boost::python::incref(boost::python::object(ret).ptr());
	}
};

} // end namespace converter
} // end namespace simconnect
} // end namespace prepar3d

#endif // __PYPREPAR3D_CONVERTER_HPP_
