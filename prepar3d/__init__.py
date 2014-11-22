class Prepar3dException(Exception):
    def __init__(self):
        super(Prepar3dException, self).__init__()
        
    def __str__(self, *args, **kwargs):
        return 'A Prepar3d-related error occurred'
    

import prepar3d._internal
from prepar3d.connection import Connection, ConnectionException, OpenConnectionException, CloseConnectionException
from prepar3d.input_event import InputEvent
from prepar3d.recv_id_event import RecvIdEvent
from prepar3d.system_event import SystemEvent
from prepar3d.data_event import DataEvent
from prepar3d.event_listener import EventListener

import prepar3d.planning

