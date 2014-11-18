import abc

class ServiceBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def find(self, departure, destination, cycle, flightlevel_from, flightlevel_to):
        return