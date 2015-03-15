import unittest

from prepar3d.util import LatLon
from prepar3d.util.lat_lon import Longitude
from math import radians

class Test(unittest.TestCase):
 
    def test_longitude_value(self):
        
        l = Longitude(179)
        self.assertEqual(l, 179)
        
        self.assertEqual(l+2, -179)
        self.assertEqual(l+2.5, -178.5)
        
        l.set(l+180)
        self.assertEqual(l, 180)
        self.assertEqual(l, -180)
        
 
    def test_lat_lon_from_deg_min_sec(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))
          
        self.assertTrue(lat_lon1 is not None)
        self.assertAlmostEqual(lat_lon1.get_lat(), 37.607222, places=5)
        self.assertAlmostEqual(lat_lon1.get_lon(), -122.38044166666666, places=10)
         
        self.assertEqual(lat_lon1.get_lat_in_radians(), radians(lat_lon1.get_lat()))
        self.assertEqual(lat_lon1.get_lon_in_radians(), radians(lat_lon1.get_lon()))
      
    def test_lat_lon_eq(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'W122 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N37 36. 26.00.', 'E122 22. 49.59.'))
          
        self.assertEqual(lat_lon1, lat_lon1)
        self.assertNotEqual(lat_lon1, lat_lon2)
          
  
    def test_distance_lat(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N34 36. 26.00.', 'W121 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N35 36. 26.00.', 'W121 22. 49.59.'))
          
        one_lat = 111130.55555555
          
        self.assertAlmostEqual(lat_lon1.distance(lat_lon2), one_lat, places=7)
        self.assertEqual(lat_lon1.distance(lat_lon2), lat_lon2.distance(lat_lon1))
          
        lat_lon3 = LatLon.from_deg_min_sec(('N36 36. 26.00.', 'W121 22. 49.59.'))
        self.assertAlmostEqual(lat_lon1.distance(lat_lon3), one_lat * 2, places=7)
  
  
    def test_distance_lon(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N0 0. 0.00.', 'W121 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N0 0. 0.00.', 'W122 22. 49.59.'))
        lat_lon3 = LatLon.from_deg_min_sec(('N1 0. 0.00.', 'W121 22. 49.59.'))
  
        self.assertAlmostEqual(lat_lon1.distance(lat_lon2), lat_lon1.distance(lat_lon3), places=7)
          
        lat_lon4 = LatLon.from_deg_min_sec(('N90 0. 0.00.', 'W121 22. 49.59.'))
        lat_lon5 = LatLon.from_deg_min_sec(('N90 0. 0.00.', 'W122 22. 49.59.'))
          
        self.assertAlmostEqual(lat_lon4.distance(lat_lon5), 0, places=10)
 
     
    def test_distance(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N0 0. 0.00.', 'W121 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N1 0. 0.00.', 'W122 22. 49.59.'))
         
        self.assertAlmostEqual(lat_lon1.distance(lat_lon2), 157158.34911586, places=7)
        

    def test_move(self):
        lat_lon1 = LatLon.from_deg_min_sec(('N0 0. 0.00.', 'W121 22. 49.59.'))
        lat_lon2 = LatLon.from_deg_min_sec(('N1 47. 58.87.', 'W121 22. 49.59.'))
        
        lat_lon1.move(200000, 0)
        
        # epsilon is 0.11 so we take 0.2 (20cm)
        self.assertLess(lat_lon1.distance(lat_lon2), 0.2)
        
        # move back and forth
        lat_lon3 = LatLon.from_deg_min_sec(('N1 47. 58.87.', 'W121 22. 49.59.'))
        
        lat_lon2.move(123456, 0)
        self.assertAlmostEqual(lat_lon2.distance(lat_lon3), 123456, places=10)
        self.assertAlmostEqual(lat_lon3.distance(lat_lon2), 123456, places=10)

        lat_lon2.move(123456, 180)
        self.assertAlmostEqual(lat_lon3.distance(lat_lon2), 0, places=10)
        self.assertAlmostEqual(lat_lon2.distance(lat_lon3), 0, places=10)

        
 
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
