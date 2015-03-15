#------------------------------------------------------------------------------ 
# 
#  SimConnect Tagged Data Request Sample 
#  
#    Description: 
#                After a flight has loaded, request the vertical speed and pitot 
#                heat switch setting of the user aircraft, but only when the data 
#                has changed 
#------------------------------------------------------------------------------ 
import prepar3d
from prepar3d.event import DataEvent
from prepar3d.util import LatLon

import logging
logging.basicConfig(level=logging.DEBUG)


def title_callback(data):
    lat_lon = LatLon.from_simconnect_data_latlonalt(data['STRUCT LATLONALT'])
    print('LatLon: %s' % lat_lon)

if __name__ == '__main__':
    
    with prepar3d.connect('Data Request Sample') as connection:
        position_event = DataEvent(prepar3d.SimulationVariable('STRUCT LATLONALT'), callback=title_callback)
        connection.subscribe(title_event)
        connection.listen()
