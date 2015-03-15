#!/usr/bin/env python
#------------------------------------------------------------------------------ 
# 
#  SimConnect Input Sample 
#  
#    Description: 
#                Ctrl-Shift-U key combination sets the brakes 
#------------------------------------------------------------------------------

# NOTE: This was taken from http://www.prepar3d.com/SDKv2/LearningCenter/LearningCenter.php
# As the description states this example should set the brakes when the key combination shift+ctrl+u is pressed.
# Apparently this is not the way it works cause pressing the default brakes key triggers the InputEvent and the
# key combination shift+ctrl+u does nothing at all!

import prepar3d 
from prepar3d.event import InputEvent

if __name__ == '__main__':
    
    with prepar3d.connect('Input Event Sample') as connection:
        brakes_event = InputEvent('ctrl+u', callback=lambda e,d: print('Brakes'), sim_event='parking_brakes')
        connection.subscribe(brakes_event)
        connection.listen()
