from prepar3d._internal.id import Id
from prepar3d._internal.simconnect import SimConnect_AddClientEventToNotificationGroup, SIMCONNECT_GROUP_PRIORITY_HIGHEST
from prepar3d.connection import Connection

class EventGroup(list):
    
    def __init__(self, name=None, events=[], priority=SIMCONNECT_GROUP_PRIORITY_HIGHEST):
        self._id = Id().get('GroupID')
        self._priority = priority
        for event in events:
            self.append(event)

    def append(self, event):
        SimConnect_AddClientEventToNotificationGroup(Connection()._handle, self._id, event._id)
        return list.append(self, event)