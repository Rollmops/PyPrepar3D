from prepar3d._internal.loop_number import LoopNumber

class Heading(LoopNumber):
    
    def __init__(self, value=0):
        super(Heading, self).__init__(start=0, end=360, value=value)
        
    def turn_left(self, heading):
        self._value = self - heading
        
    def turn_right(self, heading):
        self._value = self + heading
