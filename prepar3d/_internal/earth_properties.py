from math import pi, radians, cos

EARTH_CIRCUMFERENCE_AROUND_EQUATOR_IN_METERS = 40075000.0
EARTH_CIRCUMFERENCE_THROUGH_POLES_IN_METERS = 40007000.0

EARTH_SEMI_MAJOR_RADIUS_IN_METERS = EARTH_CIRCUMFERENCE_AROUND_EQUATOR_IN_METERS / (pi * 2.0)
EARTH_SEMI_MINOR_RADIUS_IN_METERS = EARTH_CIRCUMFERENCE_THROUGH_POLES_IN_METERS / (pi * 2.0)

LAT_METERS_TO_POLE = EARTH_CIRCUMFERENCE_THROUGH_POLES_IN_METERS / 4

def radians_to_lat_meters(lat_radians):
    return lat_radians * (LAT_METERS_TO_POLE / (pi / 2.0))

def degrees_to_lat_meters(lat_degrees):
    return radians_to_lat_meters(radians(lat_degrees))

def radians_to_lon_meters(lon_radians, ref_lat_radians):
    return lon_radians * (EARTH_CIRCUMFERENCE_AROUND_EQUATOR_IN_METERS / (pi * 2.0)) * cos(ref_lat_radians)

def degrees_to_lon_meters(lon_degrees, ref_lat_degrees):
    return radians_to_lon_meters(radians(lon_degrees), radians(ref_lat_radians))
    
def lat_meters_to_radians(lat_meters):
    return lat_meters * (1.0 / EARTH_SEMI_MINOR_RADIUS_IN_METERS)

def lon_meters_to_radians(lon_meters, ref_lat_radians):
    return lon_meters / (radians_to_lon_meters(1, ref_lat_radians))

