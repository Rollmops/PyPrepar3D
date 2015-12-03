import sys
import re
from prepar3d.connection import Connection
from prepar3d.event import RadiusDataEvent
 
class RollEvent(RadiusDataEvent):
     
    def __init__(self):
        variables = [prepar3d.SimulationVariable(variable) for variable in ['title', 'STRUCT LATLONALT']]
        super().__init__(variables,
                         radius=1000,
                         object_type=SIMCONNECT_SIMOBJECT_TYPE.SIMCONNECT_SIMOBJECT_TYPE_AIRCRAFT,
                         at_sim_start=False)
         
    def event(self, data):
        print('huhu')
        print(data)
 
 
if __name__ == '__main__':
    with Connection('Data Request Sample').open() as connection:
                 
        print('Connected to Prepar3d!')
        
        connection.subscribe(RollEvent())
        connection.listen()
