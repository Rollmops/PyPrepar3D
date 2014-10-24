/*
 * recv_type_converter.hpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#ifndef __PREPAR3D_SIMCONNECT_RECV_TYPE_CONVERTER_HPP_
#define __PREPAR3D_SIMCONNECT_RECV_TYPE_CONVERTER_HPP_

#include <boost/function.hpp>
#include "common.hpp"

#define MAP_TO_FUNC(NAME) _functionMap[SIMCONNECT_RECV_ID_ ## NAME] = _internal::castToRecvType<SIMCONNECT_RECV_ ## NAME>

namespace prepar3d
{
namespace simconnect
{
class RecvTypeConverter
{
	typedef boost::function<object(SIMCONNECT_RECV*)> FunctionType;
public:

	object operator()( SIMCONNECT_RECV *recv) const;

	const FunctionType &getConverterForID(const SIMCONNECT_RECV_ID &id) const
	{
		return _functionMap.at(id);
	}
private:
	void init();

	std::map<SIMCONNECT_RECV_ID, FunctionType> _functionMap;

};
namespace _internal
{
template<typename TYPE>
object castToRecvType(SIMCONNECT_RECV * const & source)
{
	return object((TYPE *) source);
}
} // end namespace _internal
} // end namespace simconnect
} // end namespace prepar3d

#endif /* __PREPAR3D_SIMCONNECT_RECV_TYPE_CONVERTER_HPP_ */
