__version__ = '0.1.0'
__author__ = 'Erik Tuerke'


class Prepar3dException(Exception):
    def __init__(self):
        super(Prepar3dException, self).__init__()
        
    def __str__(self):
        return 'A Prepar3d-related error occurred'

try:
    from .simulation_variable import SimulationVariable
    from .connect import connect
except:
    pass
