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
from prepar3d.util import LatLon

def title_callback(data):
    print('Title: %s' % data['title'])

def latlon_callback(data):
    lat_lon = LatLon.from_simconnect_data_latlonalt(data['STRUCT LATLONALT'])
    print('LatLon: %s' % lat_lon)
    

if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if a SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Data Request Sample', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1) 
        
    print('Connected to Prepar3d!')
    
    title_event = prepar3d.DataEvent(prepar3d.SimulationVariable('title'),
                                     callback=title_callback,
                                     at_sim_start=False,
                                     register=False)

    latlon_event = prepar3d.DataEvent(prepar3d.SimulationVariable('STRUCT LATLONALT'),
                                      callback=latlon_callback,
                                      at_sim_start=False,
                                      register=False)
    
    title_event.register()
    latlon_event.register()
    
    prepar3d.EventListener().listen()
