#!/usr/bin/env python
#------------------------------------------------------------------------------ 
# 
#  SimConnect Joystick Control Sample 
#  
#    Description: 
#                Use the "z" key to step through the events sent by the Joystick 
#                including X,Y,Z axes, Slider and Hat switch 
#------------------------------------------------------------------------------ 

# we need this to enable print inside a lambda function in python 2.7
from __future__ import print_function

from collections import deque
import sys

import prepar3d


class ControlRotation(prepar3d.InputEvent):
    
    def __init__(self, events):
        super(ControlRotation, self).__init__('z')
        self.events = deque(events)    

    def event(self, event, data, context):
        # sort of tricky approach to loop through joystick events and enable only one with each iteration
        self.events.rotate()
        [e[1].set_enabled(e[0] == 0) for e in enumerate(self.events)]
        
        
        
if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Joystick Input', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1)
    
    print('Connected to Prepar3d!')
    
    joystickEvents = [prepar3d.InputEvent('joystick:0:slider', callback=lambda e, d, c: print('slider: %d' % e.dwData), enabled=False),
                      prepar3d.InputEvent('joystick:0:XAxis', callback=lambda e, d, c: print('XAxis: %d' % e.dwData), enabled=False),
                      prepar3d.InputEvent('joystick:0:YAxis', callback=lambda e, d, c: print('YAxis: %d' % e.dwData), enabled=False),
                      prepar3d.InputEvent('joystick:0:RzAxis', callback=lambda e, d, c: print('RzAxis: %d' % e.dwData), enabled=False),
                      prepar3d.InputEvent('joystick:0:POV', callback=lambda e, d, c: print('POV: %d' % e.dwData), enabled=False)
                      ]
    
    ControlRotation(joystickEvents) 
    
    prepar3d.EventListener().listen(frequency=100)
    
    
    
    
    
    
    
    
    
    
    
    
