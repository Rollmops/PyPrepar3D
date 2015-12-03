#ifndef __PYPREPAR3D_CONVERTER_HPP_
#define __PYPREPAR3D_CONVERTER_HPP_

#include "common.hpp"

namespace prepar3d
{
namespace simconnect
{
namespace converter
{
void initializeConverters();

struct FROM_BOOST_SHARED_PTR
{
	static PyObject *convert(const boost::shared_ptr<PyObject> &value)
	{
		return value.get();
	}
};

struct FROM_DOUBLE
{
	static PyObject *convert(const double &value)
	{
		return PyFloat_FromDouble(value);
	}
};

struct FROM_FLOAT
{
	static PyObject *convert(const float &value)
	{
		return PyFloat_FromDouble(value);
	}
};

struct FROM_INT32
{
	static PyObject *convert(const int32_t &value)
	{
		return PyLong_FromLong(value);
	}
};

struct FROM_CHAR
{
	static PyObject *convert(const char &value)
	{
		return boost::python::incref(boost::python::object(value).ptr());
	}
};

struct FROM_CHAR_PTR
{
	static PyObject *convert(char * const & value)
	{
		return PyBytes_FromString(value);
	}
};

template<unsigned int LENGTH>
struct FROM_CHAR_ARRAY
{
	static PyObject *convert(char array[LENGTH])
	{
#if PY_MAJOR_VERSION <= 2
		return PyString_FromString(array);
#else
		return PyBytes_FromString(array);
#endif
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
