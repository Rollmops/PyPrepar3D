from itertools import count

from singleton import Singleton


class Id():
    __metaclass__ = Singleton
    
    def __init__(self):
        self._ids = dict()
        
    def get(self, id_type='__global__'):
        if id_type in self._ids:
            return self._ids[id_type].next()
        else:
            self._ids[id_type] = count(start=1)
            return self._ids[id_type].next()
