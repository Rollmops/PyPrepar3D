import prepar3d 

def data_callback(data):
    print('received: ', data)

if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Data Request Sample', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1) 
        
    print('Connected to Prepar3d!')
    
    prepar3d.DataEvent(data_fields=[('Plane Altitude', 'feet')], callback=data_callback)
    
    prepar3d.EventListener().listen()
      