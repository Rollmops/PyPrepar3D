#include "module_simconnect.hpp"

BOOST_PYTHON_MODULE(_simconnect)
{
	using namespace boost::python;

	scope().attr("S_OK") = S_OK;
	scope().attr("S_FALSE") = S_FALSE;
	scope().attr("E_FAIL") = E_FAIL;
	scope().attr("E_INVALIDARG") = E_INVALIDARG;
	scope().attr("SIMCONNECT_OPEN_CONFIGINDEX_LOCAL") = SIMCONNECT_OPEN_CONFIGINDEX_LOCAL;

	def("open", prepar3d::simconnect_open);
	def("close", prepar3d::simconnect_close);
	def("call_dispatch", prepar3d::simconnect_calldispatch);

	class_<SIMCONNECT_RECV>("SIMCONNECT_RECV")
			.def_readwrite("dwSize", &SIMCONNECT_RECV::dwSize)
			.def_readwrite("dwVersion", &SIMCONNECT_RECV::dwVersion)
			.def_readwrite("dwID", &SIMCONNECT_RECV::dwID);
}

