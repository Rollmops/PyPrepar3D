class Prepar3dException(Exception):
    def __init__(self):
        super(Prepar3dException, self).__init__()
        
    def __str__(self, *args, **kwargs):
        return 'A Prepar3d-related error occurred'
    

from _internal.simconnect import *
import _internal

from connection import Connection, ConnectionException, OpenConnectionException, CloseConnectionException
from event_listener import EventListener
from input_event import InputEvent
from system_event import SystemEvent
from recv_id_event import RecvIdEvent

