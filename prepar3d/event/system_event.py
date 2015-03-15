from .base_event import BaseEvent
from prepar3d._internal.system_events import SYSTEM_EVENTS
from prepar3d._internal.simconnect import SIMCONNECT_STATE  # @UnresolvedImport

import logging

class SystemEvent(BaseEvent):
    def __init__(self,
                 trigger,
                 callback=None,
                 state=SIMCONNECT_STATE.SIMCONNECT_STATE_ON,
                 enabled=None,
                 at_sim_start=False):

        # check if we know the system trigger
        if trigger.lower() not in [key.lower() for key in SYSTEM_EVENTS.keys()]:
            raise RuntimeError('Unknown system event trigger \'%s\'' % trigger)

        self._trigger = trigger
        self._recv_id = SYSTEM_EVENTS[trigger]

        logging.info('Creating system event for trigger \'%s\'', self._trigger)
        super().__init__(callback=callback,
                         state=state,
                         enabled=enabled,
                         at_sim_start=at_sim_start)


    def subscribe(self, connection):
        logging.info('Subscribing system event %s', self)
        return connection._dispatch_handler.subscribeSystemEvent(self._trigger, self._recv_id, self._callback, self._id, self._state) == 0


    def unsubscribe(self, connection=None):
        logging.info('Unsubscribing system event %s', self)
        return (connection or self.connection)._dispatch_handler.unsubscribeSystemEvent(self._recv_id, self._id) == 0


    def set_priority(self, priority):
        return

    def event(self, event, data):
        return

    def __str__(self):
        return 'SystemEvent<%s, %s>' % (self._trigger, self._callback)

