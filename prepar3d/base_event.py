import abc

from _internal.id import Id


class BaseEvent(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, callback=None):
        self._id = Id().get()
        self._callback = self.occur if callback is None else callback
        self._registered = False
    
    
    
    
    @abc.abstractmethod
    def occur(self, event, data, context):
        return
        
