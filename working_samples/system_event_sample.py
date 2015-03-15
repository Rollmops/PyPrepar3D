import prepar3d
from prepar3d.event import SystemEvent
import logging


class MySystemEvent(SystemEvent):
    
    def __init__(self):
        self.count = 0
        super().__init__('1sec')

    def event(self, event, cbData):
        self.count += 1
        print('Event occurred %d times' % self.count)
        if self.count >= 4:
            self.unsubscribe()


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    with prepar3d.connect('System Event Sample') as connection:
        connection.subscribe(MySystemEvent())
        connection.listen(100)
