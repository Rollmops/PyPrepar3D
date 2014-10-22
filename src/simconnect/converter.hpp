#ifndef __PYPREPAR3D_CONVERTER_HPP_
#define __PYPREPAR3D_CONVERTER_HPP_

#include "module.hpp"

namespace prepar3d
{

namespace _internal
{

struct DWORD_CONVERTER
{
	static PyObject *convert(const DWORD &value)
	{
		return PyLong_FromUnsignedLong(value);
	}
};

struct CHAR_CONVERTER
{
	static PyObject *convert(const char &value)
	{
		return boost::python::incref(boost::python::object(value).ptr());
	}
};

template<unsigned int LENGTH>
struct CHAR_ARRAY_CONVERTER {
	static PyObject *convert(char array[LENGTH]) {
		return PyString_FromString(array);
	}
};

}

}

#endif // __PYPREPAR3D_CONVERTER_HPP_
