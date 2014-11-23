import re

from prepar3d._internal import simconnect


class WildCardDict(dict):
    
    def __init__(self, _dict):
        super(WildCardDict, self).__init__(_dict)
    
    def __getitem__(self, key):
        for _key, _value in self.items():
            if re.match(_key, key, re.IGNORECASE):
                return _value


_UNIT_TYPES = {'number': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32,
                'bool': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32,
                'percent': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32,
                'enum': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32,
                'mask': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32,
                'feet per second': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
                'feet': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
                'knots': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64,
                'rpm': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT32,
                'xyz': simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_XYZ
                }


def _get_unit_type(unit):
    return (unit, _UNIT_TYPES[unit])

_SIMULATION_VARIABLES = WildCardDict({  'NUMBER OF ENGINES': _get_unit_type('number'),
                           'ENGINE CONTROL SELECT':  _get_unit_type('mask'),
                           'THROTTLE LOWER LIMIT': _get_unit_type('percent'),
                           'ENGINE TYPE': _get_unit_type('enum'),
                           'MASTER IGNITION SWITCH': _get_unit_type('bool'),
                           'GENERAL ENG COMBUSTION:\\d': _get_unit_type('bool'),
                           'GENERAL ENG MASTER ALTERNATOR:\\d': _get_unit_type('bool'),
                           'GENERAL ENG FUEL PUMP SWITCH:\\d':  _get_unit_type('bool'),
                           'GENERAL ENG FUEL PUMP ON:\\d': _get_unit_type('bool'),
                           'GENERAL ENG RPM:\\d':  _get_unit_type('rpm'),
                           'GENERAL ENG THROTTLE LEVER POSITION:\\d': _get_unit_type('percent'),
                           'RECIP ENG FUEL FLOW:\\d': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64),
                           'FUEL TANK CENTER LEVEL': _get_unit_type('percent'),
                           
                           # Aircraft Lights Data
                           'LIGHT STROBE': _get_unit_type('bool'),
                           'LIGHT PANEL': _get_unit_type('bool'),
                           'LIGHT LANDING':  _get_unit_type('bool'),
                           'LIGHT TAXI':  _get_unit_type('bool'),
                           'LIGHT BEACON':  _get_unit_type('bool'),
                           'LIGHT NAV':  _get_unit_type('bool'),
                           'LIGHT LOGO':  _get_unit_type('bool'),
                           'LIGHT WING':  _get_unit_type('bool'),
                           'LIGHT RECOGNITION':  _get_unit_type('bool'),
                           'LIGHT CABIN':  _get_unit_type('bool'),
                           'LIGHT ON STATES':  _get_unit_type('mask'),
                           'LIGHT STATES':  _get_unit_type('mask'),
                           'LANDING LIGHT PBH': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_XYZ),
                           'LIGHT STROBE ON': _get_unit_type('bool'),
                           'LIGHT PANEL ON': _get_unit_type('bool'),
                           'LIGHT LANDING ON':  _get_unit_type('bool'),
                           'LIGHT TAXI ON':  _get_unit_type('bool'),
                           'LIGHT BEACON ON':  _get_unit_type('bool'),
                           'LIGHT NAV ON':  _get_unit_type('bool'),
                           'LIGHT LOGO ON':  _get_unit_type('bool'),
                           'LIGHT WING ON':  _get_unit_type('bool'),
                           'LIGHT RECOGNITION ON':  _get_unit_type('bool'),
                           'LIGHT CABIN ON':  _get_unit_type('bool'),
                           'LIGHT BRAKE ON':  _get_unit_type('bool'),
                           'LIGHT HEAD ON':  _get_unit_type('bool'),
                           
                           # Aircraft Position and Speed Data
                           'GROUND VELOCITY':  _get_unit_type('knots'),
                           'TOTAL WORLD VELOCITY': _get_unit_type('feet per second'),
                           'VELOCITY BODY Z': _get_unit_type('feet per second'),
                           'VELOCITY BODY X': _get_unit_type('feet per second'),
                           'VELOCITY BODY Y': _get_unit_type('feet per second'),
                           'VELOCITY WORLD Z':_get_unit_type('feet per second'),
                           'VELOCITY WORLD X': _get_unit_type('feet per second'),
                           'VELOCITY WORLD Y': _get_unit_type('feet per second'),
                           'PLANE ALTITUDE': _get_unit_type('feet'),
                           'STRUCT SURFACE RELATIVE VELOCITY': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_XYZ),
                           'STRUCT WORLDVELOCITY': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_XYZ),
                           'STRUCT LATLONALT': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_LATLONALT),
                           
                           # Aircraft Flight Instrumentation Data
                           'VERTICAL SPEED': _get_unit_type('feet per second'),
                           
                           
                           'TITLE': ('', simconnect.SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING256)
                           })

