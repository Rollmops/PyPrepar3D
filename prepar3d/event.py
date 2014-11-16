import abc
class Event(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, trigger):
        self._trigger = trigger
        
    @abc.abstractmethod
    def occur(self, event, cbData, context):
        return
        