from math import radians, cos, sin, asin, sqrt
import re

from prepar3d._internal import earth_properties


class LatLon(object):
    
    _MULTIPLICATOR = {'N':1, 'S':-1, 'W':-1, 'E':1}

    # N37 36' 26.00"
    _DEG_MIN_SEC_LAT_REGEX = re.compile(r'^(N|S)(\d+)\s+(\d+).\s+(\d{1,2}\.\d+).\s*$', re.IGNORECASE)
    _DEG_MIN_SEC_LON_REGEX = re.compile(r'^(W|E)(\d+)\s+(\d+).\s+(\d{1,2}\.\d+).\s*$', re.IGNORECASE)

    def __init__(self, lat_lon):
        self._lat = lat_lon[0]
        self._lon = lat_lon[1]
        self._lat_rad = radians(lat_lon[0])
        self._lon_rad = radians(lat_lon[1])
        
    @staticmethod
    def from_deg_min_sec(lat_lon):
        mlat = LatLon._DEG_MIN_SEC_LAT_REGEX.match(lat_lon[0])
        mlon = LatLon._DEG_MIN_SEC_LON_REGEX.match(lat_lon[1])
        
        if mlat and mlon:
            return LatLon(((int(mlat.group(2)) + int(mlat.group(3)) / 60 + float(mlat.group(4)) / 3600.0) * LatLon._MULTIPLICATOR[mlat.group(1)],
                          (int(mlon.group(2)) + int(mlon.group(3)) / 60 + float(mlat.group(4)) / 3600.0) * LatLon._MULTIPLICATOR[mlon.group(1)]))
        else:
            return None

    
    def __eq__(self, other):
        return self._lat == other._lat and self._lon == other._lon
    
    def distance(self, other):
        dlat = other._lat_rad - self._lat_rad
        dlon = other._lon_rad - self._lon_rad
        
        a = sin(dlat / 2) ** 2 + cos(self._lat_rad) * cos(other._lat_rad) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a)) 
         
        return abs(earth_properties.EARTH_SEMI_MINOR_RADIUS_IN_METERS * c)
    
    def move(self, meters, heading):
        pass
        
        
        
    
        
        
