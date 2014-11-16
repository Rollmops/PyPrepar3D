from itertools import count
from singleton import Singleton

class Id():
    __metaclass__ = Singleton
    
    def __init__(self):
        self._ids = count(0)
        
    def get(self):
        return self._ids.next()