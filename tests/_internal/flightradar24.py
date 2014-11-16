# from prepar3d._internal.flightradar24 import Flightradar24
# import unittest
# 
# 
# airports = [("EDDF", "Frankfurt Airport"),
#             ("EDDC", "Dresden Airport"),
#     ("CYXX", "Abbotsford International Airport")]
# 
# 
# class TestCaseFlightradar24(unittest.TestCase):
#     def setUp(self):
#         self.flightradar = Flightradar24()
# 
#     def test_common(self):
#         self.assertGreater(len(self.flightradar.airports), 0)
#         self.assertGreater(len(self.flightradar.zones), 0)
#         self.assertGreater(len(self.flightradar.airlines), 0)
#         self.assertGreater(len(self.flightradar.aircrafts), 0)
# 
#         num_aircrafts_full = len(self.flightradar.aircrafts)
# 
#         self.flightradar.refresh_aircrafts(zone="europe")
#         self.assertGreater(num_aircrafts_full, len(self.flightradar.aircrafts))
# 
#     def test_airpots(self):
#         for aiport in airports:
#             elem = [ap for ap in self.flightradar.airports if ap['icao'] == aiport[0]][0]
#             self.assertTrue(len(elem) > 0)
#             self.assertEqual(elem['name'], aiport[1])
# 
# 
# if __name__ == '__main__':
#     unittest.main()
