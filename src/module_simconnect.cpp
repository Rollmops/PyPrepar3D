#include "module_simconnect.hpp"

BOOST_PYTHON_MODULE(_simconnect)
{
	using namespace boost::python;

	prepar3d::_internal::define_constants(&scope());

	def("open", prepar3d::simconnect_open);
	def("close", prepar3d::simconnect_close);
	def("call_dispatch", prepar3d::simconnect_calldispatch);
	def("subscribe_to_system_event", prepar3d::simconnect_subscribe_to_system_event);


	class_<SIMCONNECT_RECV>("SIMCONNECT_RECV")
			.def_readwrite("dwSize", &SIMCONNECT_RECV::dwSize)
			.def_readwrite("dwVersion", &SIMCONNECT_RECV::dwVersion)
			.def_readwrite("dwID", &SIMCONNECT_RECV::dwID);
}

