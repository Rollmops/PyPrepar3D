import prepar3d

class PauseEvent(prepar3d.Event):
    
    def __init__(self):
        super(PauseEvent, self).__init__('Paused')
        
    def occur(self, event, cbData, context):
        print('Paused')


class FrameEvent(prepar3d.Event):
    
    def __init__(self):
        super(FrameEvent, self).__init__('Frame')
        
    def occur(self, event, cbData, context):
        print('Frame')


if __name__ == '__main__':
    
    connection = prepar3d.Connection('EventTest', open=True)
    
    event_listener = prepar3d.EventListener(connection=connection)
    event_listener.register_event(FrameEvent())
    event_listener.register_event(PauseEvent())

    event_listener.listen()
    
        
    connection.close()