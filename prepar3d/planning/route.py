from service_route_finder import ServiceRouteFinder

class AirwayLevel:
    HIGH = 'H'
    LOW = 'L'
    BOTH = 'B'


class Route(list):
    
    def __init__(self, departure, destination, flightlevel, cycle=None, level=AirwayLevel.BOTH, service=ServiceRouteFinder() ):
        self._departure = departure
        self._destination = destination
        self._flightlevel = flightlevel
        self._cycle = cycle
        self._level = level
        self._distance = None
        
        service.find(departure, destination, cycle, flightlevel[0], flightlevel[1], level )
            
    def find(self):
        pass