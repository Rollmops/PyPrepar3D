#!/usr/bin/env python
#------------------------------------------------------------------------------ 
# 
#  With statement sample 
#  
#    Description: 
#                Using Pythons contextlib to automatically close
#                a connection when leaving the context.
#------------------------------------------------------------------------------

import prepar3d 

if __name__ == '__main__':
    
    with prepar3d.Connection().open('With statement test'):
        
        print('Connected to Prepar3d!')
        
    # here the connection should be closed again
    print('Connection is %s!', 'open' if prepar3d.Connection().is_open() else 'closed')
     
