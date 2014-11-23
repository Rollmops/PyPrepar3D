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


def data_callback(data):
    print('received: ', (data['VERTICAL SPEED'] * 60))
    

if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Data Request Sample', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1) 
        
    print('Connected to Prepar3d!')
    
    request_data = [prepar3d.SimulationVariable(variable) for variable in ['VERTICAL SPEED']]
    
    prepar3d.DataEvent(request_data, callback=data_callback, at_sim_start=False)
    
    prepar3d.EventListener().listen()
      
