import re

class LatLon(object):
    
    _MULTIPLICATOR = {'N':1, 'S':-1, 'W':-1, 'E':1}

    # N37 36' 26.00"
    _DEG_MIN_SEC_LAT_REGEX = re.compile(r'^(N|S)(\d+)\s+(\d+).\s+(\d{1,2}\.\d+).$', re.IGNORECASE)
    _DEG_MIN_SEC_LON_REGEX = re.compile(r'^(W|E)(\d+)\s+(\d+).\s+(\d{1,2}\.\d+).$', re.IGNORECASE)

    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon
        
    @staticmethod
    def from_deg_min_sec(lat, lon):
        mlat = LatLon._DEG_MIN_SEC_LAT_REGEX.match(lat)
        mlon = LatLon._DEG_MIN_SEC_LON_REGEX.match(lon)
        
        if mlat and mlon:
            return LatLon((int(mlat.group(2)) + int(mlat.group(3)) / 60 + float(mlat.group(4)) / 3600.0) * LatLon._MULTIPLICATOR[mlat.group(1)],
                          (int(mlon.group(2)) + int(mlon.group(3)) / 60 + float(mlat.group(4)) / 3600.0) * LatLon._MULTIPLICATOR[mlon.group(1)])
        else:
            return None
