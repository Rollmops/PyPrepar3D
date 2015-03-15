import unittest
from timeit import timeit


class Test(unittest.TestCase):

    SETUP = 'from prepar3d.util.lat_lon import LatLon;'

    def test_lat_lon_benchmark(self):
        print('LatLon.from_deg_min_sec(): ', timeit('LatLon.from_deg_min_sec(("N37 36. 26.00.", "W122 22. 49.59."))', setup=Test.SETUP))
        
        print('LatLon.str_deg_min_sec(): ', timeit('lat_lon.str_deg_min_sec()'), setup=Test.SETUP + 'lat_lon=LatLon.from_deg_min_sec(("N37 36. 26.00.", "W122 22. 49.59."))')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
