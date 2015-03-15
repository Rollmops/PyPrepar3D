from .base_event import BaseEvent

import logging

class RecvIdEvent(BaseEvent):
    
    def __init__(self,
                 recv_id,
                 callback=None,
                 at_sim_start=False):

        self._recv_id = recv_id

        logging.info('Creating recvid event for id %d', self._recv_id)

        super().__init__(callback=callback,
                         at_sim_start=at_sim_start)


    def subscribe(self, connection):
        logging.info('Subscribing recvid event %s', self)
        connection._dispatch_handler.subscribeRecvIDEvent(self._recv_id, self._callback)


    def unsubscribe(self, connection=None):
        logging.info('Unsubscribing recvid event %s', self)
        (connection or self.connection)._dispatch_handler.unsubscribeRecvIDEvent(self._recv_id)


    def event(self, event, data):
        pass
    
    def set_priority(self, priority):
        return 
    
    def __str__(self):
        return 'RecvIdEvent<%d, %s>' % (self._recv_id, self._callback)
