'''
Created on Nov 19, 2014

@author: Erik
'''
import unittest
from prepar3d._internal.lat_lon import LatLon

class Test(unittest.TestCase):


    def test_lat_lon_from_deg_min_sec(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))
        
        self.assertTrue(lat_lon1 is not None)
        self.assertAlmostEqual(lat_lon1._lat, 37.607222, places=5)
        self.assertAlmostEqual(lat_lon1._lon, -122.373888, places=5)
    
    def test_lat_lon_eq(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'E122 22. 49.59.'))
        
        self.assertEqual(lat_lon1, lat_lon1)
        self.assertNotEqual(lat_lon1, lat_lon2)
        

    def test_distance(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W13 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N34 36. 26.00.', 'W122 22. 49.59.'))

        self.assertAlmostEqual(lat_lon1.distance(lat_lon2), 9149.306289152, 6)
        self.assertAlmostEqual(lat_lon2.distance(lat_lon1), 9149.306289152, 6)
        self.assertEqual(lat_lon1.distance(lat_lon1), 0)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
