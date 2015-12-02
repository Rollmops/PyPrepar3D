/*
 * recv_type_converter.hpp
 *
 *  Created on: Oct 24, 2014
 *      Author: Erik
 */

#ifndef __PREPAR3D_SIMCONNECT_RECV_TYPE_CONVERTER_HPP_
#define __PREPAR3D_SIMCONNECT_RECV_TYPE_CONVERTER_HPP_

#include <functional>
#include "common.hpp"

#define REGISTER_CONVERTER(NAME) _functionMap[SIMCONNECT_RECV_ID_ ## NAME] = _internal::castToRecvType<SIMCONNECT_RECV_ ## NAME>

namespace prepar3d
{
namespace simconnect
{
class RecvTypeConverter
{

public:
	typedef std::function<object(SIMCONNECT_RECV*)> ConvertFunctionType;
	RecvTypeConverter()
	{
		init();
	}

	object operator()(SIMCONNECT_RECV *recv) const;

	const ConvertFunctionType &getConverterForID(const SIMCONNECT_RECV_ID &id) const
	{
		return _functionMap.at(id);
	}
private:
	void init();

	std::map<SIMCONNECT_RECV_ID, ConvertFunctionType> _functionMap;

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
