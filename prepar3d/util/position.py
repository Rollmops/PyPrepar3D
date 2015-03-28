from prepar3d.util.lat_lon import LatLon
from prepar3d._internal.earth_properties import FEET_TO_METERS_CONSTANT
from math import sqrt

class Position(LatLon):

    def __init__(self, lat_lon, altitude):
        super().__init__(lat_lon)
        self._altitude_feet = altitude
        self._altitude_meters = altitude * FEET_TO_METERS_CONSTANT
        
    @staticmethod
    def from_deg_min_sec_feet(lat_lon, altitude):
        return Position(LatLon.from_deg_min_sec(lat_lon)._lat_lon, altitude)  
    
    @staticmethod
    def from_deg_min_sec_meters(lat_lon, altitude):
        return Position(LatLon.from_deg_min_sec(lat_lon)._lat_lon, altitude / FEET_TO_METERS_CONSTANT)
    
    @staticmethod
    def from_simconnect_data_latlonalt(self, latlonalt):
        return Position((latlonalt.Latitude, latlonalt.Longitude), latlonalt.Altitude)
    
    @staticmethod
    def from_simconnect_data_initposition(self, initposition):
        return Position.from_simconnect_data_latlonalt(initposition)
    
    def distance(self, other):
        dalt = abs(self._altitude_meters - other._altitude_meters)
        return sqrt(super(Position, self).distance(other) ** 2 + dalt ** 2)

    def move(self,
             distance_in_meters,
             heading,
             altitude_in_feet):

        LatLon.move(self, distance_in_meters, heading)
        if (self._altitude_feet + altitude_in_feet) < 0:
            self._altitude_feet = 0
        else:
            self._altitude_feet += altitude_in_feet
        
        self._altitude_meters = self._altitude_feet * FEET_TO_METERS_CONSTANT

    def _get_altitude_in_feet(self):
        return self._altitude_feet

    def _get_altitude_in_meters(self):
        return self._altitude_meters
    
    #TODO add setter for both properties
    altitude_feet = property(_get_altitude_in_feet)
    altitude_meters = property(_get_altitude_in_meters)
