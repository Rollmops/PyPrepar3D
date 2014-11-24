'''
Created on 24.11.2014

@author: QXH6010
'''
import unittest
from prepar3d.util import Position
from prepar3d.util import LatLon
from prepar3d._internal.earth_properties import FEET_TO_METERS_CONSTANT
from math import sqrt

class Test(unittest.TestCase):

    def test_position_distance_same_lat_lon(self):
        pos1 = Position.from_deg_min_sec_feet(('N37 36. 26.00.', 'W122 22. 49.59.'), 0)
        pos2 = Position.from_deg_min_sec_feet(('N37 36. 26.00.', 'W122 22. 49.59.'), 0)
        pos3 = Position.from_deg_min_sec_feet(('N37 36. 26.00.', 'W122 22. 49.59.'), 1000)
         
        self.assertEqual(pos1.distance(pos2), 0)
        self.assertEqual(pos1.distance(pos3), 1000 * FEET_TO_METERS_CONSTANT)
        
        pos4 = Position.from_deg_min_sec_meters(('N37 36. 26.00.', 'W122 22. 49.59.'), 0)
        pos5 = Position.from_deg_min_sec_meters(('N37 36. 26.00.', 'W122 22. 49.59.'), 1000)
        
        self.assertEqual(pos4.distance(pos5), 1000)
        
    def test_position_distance(self):
        altitude1 = 0
        altitude2 = 32000
        pos1 = Position.from_deg_min_sec_feet(('N37 36. 26.00.', 'W122 22. 49.59.'), altitude1)
        pos2 = Position.from_deg_min_sec_feet(('N36 36. 26.00.', 'W122 22. 49.59.'), altitude2)
        
        self.assertAlmostEqual(pos1.distance(pos2), sqrt((altitude2 * FEET_TO_METERS_CONSTANT) ** 2 + LatLon(pos1._lat_lon).distance(LatLon(pos2._lat_lon)) ** 2))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_position']
    unittest.main()
