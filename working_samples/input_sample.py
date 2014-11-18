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

# we need this to enable print inside a lambda function in python 2.7
from __future__ import print_function

import prepar3d 

if __name__ == '__main__':
    
    try:
        # the connection closes either when it gets destroyed or if an SIMCONNECT_RECV_ID_QUIT event is received
        prepar3d.Connection().open('Input Event', auto_close=True)
    except prepar3d.OpenConnectionException:
        print('Uups! Is Prepar3d running?')
        sys.exit(1)
    
    print('Connected to Prepar3d!')
        
    prepar3d.InputEvent('shift', callback=lambda e, d, c: print('brakes!'), sim_event='brakes')
    
    prepar3d.EventListener().listen()
