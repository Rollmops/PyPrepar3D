import prepar3d 

class RollEvent(prepar3d.DataEvent):
    
    def __init__(self):
        self._re = re
        request_data = [prepar3d.SimulationVariable(variable) for variable in ['title', 'STRUCT LATLONALT']]
        super(RollEvent, self).__init__(request_data, at_sim_start=False)
        
    def event(self, data):
        print('huhu')
        print(self._re._data)


if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Data Request Sample', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1) 
        
    print('Connected to Prepar3d!')
    
    request_data = [prepar3d.SimulationVariable(variable) for variable in ['title', 'STRUCT LATLONALT']]
    
    r=RollEvent(prepar3d.RadiusData(request_data, radius=1000))
    
    prepar3d.EventListener().listen()
    
