import prepar3d
from prepar3d._internal import simconnect


def ai_added(event, data, context):
    print 'X pressed'

def error(event, data, context):
    print event.dwException
    print('Error occurred: %s' % event.dwException)

if __name__ == '__main__':
    
    prepar3d.Connection().open('EventTest')
    
    prepar3d.SystemEvent('Frame', callback=ai_added)
    
    prepar3d.EventListener().listen()
        
