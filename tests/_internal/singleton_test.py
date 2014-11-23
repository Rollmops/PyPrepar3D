'''
Created on Nov 18, 2014

@author: Erik
'''
import unittest

from prepar3d._internal.singleton import Singleton


class Test(unittest.TestCase):

    class MySingleton(metaclass=Singleton):
        
        def __init__(self):
            self.value = 1

    def testName(self):
        s1 = Test.MySingleton()
        self.assertEqual(s1.value, 1)
        s1.value = 2
        self.assertEqual(s1.value, 2)
        
        s2 = Test.MySingleton()
        self.assertEqual(s2.value, 2)
        
        
        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
