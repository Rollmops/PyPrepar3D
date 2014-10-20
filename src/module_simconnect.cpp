
#include <boost/python.hpp>

char const *greet()
{
	return "Hello World!";
}

BOOST_PYTHON_MODULE(ext_module)
{
	boost::python::def("greet", greet);
}

