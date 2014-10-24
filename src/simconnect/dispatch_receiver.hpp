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
	typedef boost::function<object(SIMCONNECT_RECV*)> FunctionType;
public:
	DispatchReceiver()
	{
	}
	;

	DispatchReceiver(PyObject *handle) :
			_handle(handle)
	{
	}

	void registerID(SIMCONNECT_RECV_ID id);

	tuple getNextDispatch()
	{
		return getNextDispatchForHandle(_handle);
	}
	tuple getNextDispatchForHandle(PyObject *handle);
private:

	std::map<SIMCONNECT_RECV_ID, FunctionType> _registeredIdList;

	PyObject *_handle;
};

} // end namespace simconnect
} // end namespace prepar3d

#endif // __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_
