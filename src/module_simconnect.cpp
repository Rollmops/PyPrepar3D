#include "module_simconnect.hpp"

BOOST_PYTHON_MODULE(_simconnect)
{
	using namespace boost::python;

	scope().attr("S_OK") = S_OK;
	scope().attr("S_FALSE") = S_FALSE;

	boost::python::def("open", prepy3d::simconnect_open);
}

