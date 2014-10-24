#ifndef __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_
#define __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_

#include "common.hpp"
#include <map>
#include <list>
#include <utility>
#include <boost/function.hpp>

namespace prepar3d {
namespace simconnect {

class DispatchReceiver {
	typedef boost::function<tuple (SIMCONNECT_RECV*) > FunctionType;
public:
	DispatchReceiver();

	tuple operator()(HANDLE handle) ;
	void registerID(SIMCONNECT_RECV_ID id);
private:
	std::map<SIMCONNECT_RECV_ID, FunctionType > _functionMap;
	std::map<SIMCONNECT_RECV_ID, FunctionType > _registeredIdList;
};

template<typename TYPE>
tuple castToRecvType(SIMCONNECT_RECV *source) {
	return make_tuple(static_cast<TYPE*>(source));
}

} // end namespace simconnect
} // end namespace prepar3d


#endif // __PREPAR3D_SIMCONNECT_DISPATCH_RECEIVER_HPP_
