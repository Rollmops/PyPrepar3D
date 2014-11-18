'''
Created on Nov 18, 2014

@author: Erik
'''
import unittest

from prepar3d._internal.singleton import Singleton


class MySingleton(object):
    
    __metaclass__ = Singleton
    
    def __init__(self):
        print 'init'
        self.value = 1

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        s1 = MySingleton()
        self.assertEqual(s1.value, 1)
        s1.value = 2
        self.assertEqual(s1.value, 2)
        
        s2 = MySingleton()
        self.assertEqual(s2.value, 2)
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()