class Prepar3dException(Exception):
    def __init__(self):
        super(Prepar3dException, self).__init__()
        
    def __str__(self, *args, **kwargs):
        return 'A Prepar3d-related error occurred'
    

import _internal
from _internal.simconnect import *
from connection import Connection, ConnectionException, OpenConnectionException, CloseConnectionException
from event_listener import EventListener
from input_event import InputEvent
from recv_id_event import RecvIdEvent
from system_event import SystemEvent


