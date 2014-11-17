import prepar3d


class JoystickEvent(prepar3d.InputEvent):
    
    def __init__(self):
        super(JoystickEvent, self).__init__('Joystick:0:POV', state=prepar3d.SIMCONNECT_STATE.SIMCONNECT_STATE_OFF)
        
        
    def occur(self, event, data, context):
        print('Joystick')

def frame(event, data, context):
    print ('Frame')

def error(event, data, context):
    print('Error occurred: %s' % event.dwException)

if __name__ == '__main__':
    
    prepar3d.Connection().open('EventTest')

    prepar3d.RecvIdEvent(prepar3d.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EXCEPTION, error)
    
    joystickEvent = JoystickEvent()
    
    frameEvent = prepar3d.SystemEvent('Frame', callback=frame, state=prepar3d.SIMCONNECT_STATE.SIMCONNECT_STATE_OFF)
    
    prepar3d.InputEvent('z', callback=lambda _, __, ___: frameEvent.set_state(prepar3d.SIMCONNECT_STATE.SIMCONNECT_STATE_ON))
    
    
    
    prepar3d.EventListener().listen()
        
