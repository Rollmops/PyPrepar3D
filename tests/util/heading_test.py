'''
Created on Nov 24, 2014

@author: Erik
'''
import unittest
from prepar3d.util import Heading

class Test(unittest.TestCase):


    def test_heading(self):
        h = Heading(10)
        
        self.assertEqual(h, 10)
        
        self.assertEqual(h+10, 20)
        self.assertEqual(h+349, 359)
        self.assertEqual(h+350, 0)
        self.assertEqual(h+350, 360)
        self.assertEqual(h+351, 1)
        self.assertEqual(h+360, 10)
        self.assertEqual(h+710, 0)
               
        [self.assertEqual(h+(v*360), 10) for v in range(0,10)]
        
        self.assertEqual(h-9, 1)
        self.assertEqual(h-10, 0)
        self.assertEqual(h-11, 359)
        self.assertEqual(h-12, 358)
        [self.assertEqual(h-(v*360), 10) for v in range(0,10)]
        
    def test_heading_turn(self):
        
        h = Heading()
        
        self.assertEqual(h, 0)
        
        h.turn_left(10)
        self.assertEqual(h, 350)
        
        h.turn_right(20)
        self.assertEqual(h, 10)
        
        h.turn_left(350)
        self.assertEqual(h, 20)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_heading']
    unittest.main()