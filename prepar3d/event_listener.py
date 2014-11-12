import threading
from prepar3d._internal import simconnect

class EventListener(threading.Thread):
    
    def __init__(self, handle, name, id, frequency=10):
        super(EventListener, self).__init__()
        self.dispatch_listener = simconnect.DispatchListener(handle)
        self.dispatch_listener.subscribeSystemEvent(name, id, self.event)
        self.frequency = frequency

    def event(self, event, cbData, blubb):
        pass
        
    def run(self):
        self.dispatch_listener.listen(self.frequency)
        
        
        
        
        