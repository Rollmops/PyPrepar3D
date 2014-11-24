
class LoopNumber:
    
    def __init__(self, start, end, value=None):
        assert(start < end)
        self._start = start
        self._end = end
        self._span = end - start + 1
        self._value = start if value is None else value
    
    def set(self, value):
        assert(value >= self._start and value <= self._end)
        self._value = value

    def get(self):
        return self._value
        
    def __add__(self, other):
        v = self._value + (other % self._span)
        if v > self._end:
            v = self._start + (v - self._end - 1)
        return v
    
    def __sub__(self, other):
        v = self._value - (other % self._span)
        if v < self._start:
            v = self._end - (self._start - v) + 1
        return v
        
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self._value == other
        elif isinstance(other, LoopNumber):
            return self._value == other._value
        else:
            raise TypeError('Need int or LoopNumber for LoopNumber.__eq__()')
    
    def __repr__(self):
        return self._value
        