#include "singletons.hpp"
#include <boost/foreach.hpp>

namespace prepar3d
{
namespace util
{
Singletons &Singletons::getMaster()
{
	static Singletons me;
	return me;
}
Singletons::~Singletons()
{
	while (!map.empty())
	{
		map.begin()->second();
		map.erase(map.begin());
	}
}
Singletons::Singletons()
{
}

}
}
