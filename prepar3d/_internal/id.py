from itertools import count

from prepar3d._internal.singleton import Singleton


class Id(metaclass=Singleton):
    
    def __init__(self):
        self._ids = dict()
        
    def get(self, id_type='__global__'):
        if id_type in self._ids:
            return next(self._ids[id_type])
        else:
            self._ids[id_type] = count(start=1)
            return next(self._ids[id_type])
