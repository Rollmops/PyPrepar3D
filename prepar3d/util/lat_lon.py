# http://www.movable-type.co.uk/scripts/latlong.html
from math import radians, cos, sin, asin, atan2, sqrt, degrees
import re

from prepar3d._internal import earth_properties
from prepar3d._internal.loop_number import LoopNumber 

class Longitude(LoopNumber):
    def __init__(self, value):
        super(Longitude, self).__init__(start=-180, end=180, value=value)
        


class LatLon:
    
    _MULTIPLICATOR = {'N':1, 'S':-1, 'W':-1, 'E':1}

    # N37 36' 26.00"
    _DEG_MIN_SEC_LAT_REGEX = re.compile(r'^(N|S)(\d+)\s+(\d+).\s*(\d{1,2}\.\d+).\s*$', re.IGNORECASE)
    _DEG_MIN_SEC_LON_REGEX = re.compile(r'^(W|E)(\d+)\s+(\d+).\s*(\d{1,2}\.\d+).\s*$', re.IGNORECASE)

    def __init__(self, lat_lon):
        self.lat = lat_lon[0]
        self.lon = lat_lon[1]
        self.lat_lon = lat_lon
        self.lat_rad = radians(lat_lon[0])
        self.lon_rad = radians(lat_lon[1])
    
    @staticmethod
    def from_deg_min_sec(lat_lon):
        mlat = LatLon._DEG_MIN_SEC_LAT_REGEX.match(lat_lon[0])
        mlon = LatLon._DEG_MIN_SEC_LON_REGEX.match(lat_lon[1])
        
        if mlat and mlon:
            return LatLon(((int(mlat.group(2)) + int(mlat.group(3)) / 60 + float(mlat.group(4)) / 3600) * LatLon._MULTIPLICATOR[mlat.group(1)],
                          (int(mlon.group(2)) + int(mlon.group(3)) / 60 + float(mlon.group(4)) / 3600) * LatLon._MULTIPLICATOR[mlon.group(1)]))
        else:
            return None

    @staticmethod
    def from_simconnect_data_latlonalt(latlonalt):
        return LatLon((latlonalt.Latitude, latlonalt.Longitude))

    @staticmethod
    def from_simconnect_data_initposition(initposition):
        return LatLon.from_simconnect_data_latlonalt(initposition)

    @staticmethod
    def _deg_min_sec_tuple(coord):
        deg = int(coord)
        min = int(60 * (coord - deg))
        sec = round(3600 * abs(coord - deg - min / 60), 2)
        return (deg, min, sec)

    def str_deg_min_sec(self):
        dms_lat = LatLon._deg_min_sec_tuple(abs(self.lat))
        dms_lon = LatLon._deg_min_sec_tuple(abs(self.lon))
        _lat = '%s%d %d%s %.2f%s' % ('S' if self.lat < 0 else 'N', dms_lat[0], dms_lat[1], chr(39), dms_lat[2], chr(34))
        _lon = '%s%d %d%s %.2f%s' % ('W' if self.lon < 0 else 'E', dms_lon[0], dms_lon[1], chr(39), dms_lon[2], chr(34))
        
        return '%s,%s' % (_lat, _lon)

    def __str__(self):
        return self.str_deg_min_sec()

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    
    def distance(self, other):
        dlat_rad = other.lat_rad - self.lat_rad
        dlon_rad = other.lon_rad - self.lon_rad
        
        a = sin(dlat_rad / 2) ** 2 + cos(self.lat_rad) * cos(other.lat_rad) * sin(dlon_rad / 2) ** 2
        c = 2 * asin(sqrt(a)) 
        return abs(earth_properties.EARTH_SEMI_MINOR_RADIUS_IN_METERS * c)
    
    def move(self, distance_in_meters, heading):
        angular_distance = distance_in_meters / earth_properties.EARTH_SEMI_MINOR_RADIUS_IN_METERS
        bearing_rad = radians(heading)
        lat_rad_dest = asin(sin(self.lat_rad) * cos(angular_distance) + cos(self.lat_rad) * sin(angular_distance) * cos(bearing_rad))
        lon_rad_dest = self.lon_rad + atan2(sin(bearing_rad) * sin(angular_distance) * cos(self.lat_rad), cos(angular_distance) - sin(self.lat_rad) * sin(lat_rad_dest))
        
        self.lat_rad = lat_rad_dest
        self.lon_rad = lon_rad_dest
        self.lat = degrees(lat_rad_dest)
        self.lon = degrees(lon_rad_dest)
        self.lat_lon = (self.lat, self.lon)
