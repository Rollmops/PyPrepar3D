'''
Created on Nov 19, 2014

@author: Erik
'''
import unittest
import timeit
from prepar3d._internal.lat_lon import LatLon

class Test(unittest.TestCase):


    def test_lat_lon(self):
        
        print(timeit.timeit("LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))", setup='from prepar3d._internal.lat_lon import LatLon'))
        
        print( LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))._lon)
        print( LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))._lat)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()