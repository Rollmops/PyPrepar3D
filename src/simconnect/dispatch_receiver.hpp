#ifndef __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_
#define __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_

#include "common.hpp"
#include <map>
#include <list>
#include <utility>
#include <boost/function.hpp>

namespace prepar3d
{
namespace simconnect
{

class DispatchReceiver
{
	typedef boost::function<boost::python::object(SIMCONNECT_RECV*)> FunctionType;
public:
	DispatchReceiver(PyObject *handle) :
			_handle(boost::shared_ptr<PyObject>(handle))
	{
	}

	void registerID(SIMCONNECT_RECV_ID id);

	tuple getNextDispatch()
	{
		return getNextDispatchForHandle(_handle);
	}
	tuple getNextDispatchForHandle(const boost::shared_ptr<PyObject> &handle);
private:

	std::map<SIMCONNECT_RECV_ID, FunctionType> _registeredIdList;

	boost::shared_ptr<PyObject> _handle;
};

} // end namespace simconnect
} // end namespace prepar3d

#endif // __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_
