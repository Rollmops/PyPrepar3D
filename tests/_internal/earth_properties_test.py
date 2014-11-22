'''
Created on Nov 21, 2014

@author: Erik
'''
import unittest
from prepar3d._internal import earth_properties

class Test(unittest.TestCase):


    def testName(self):
        print(earth_properties.degrees_to_lat_meters(1))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()