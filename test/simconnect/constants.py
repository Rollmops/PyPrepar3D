import unittest
from prepar3d import _simconnect

class TestCaseSimconnectConstants(unittest.TestCase):
    def test_win_constants(self):
        self.assertEqual(_simconnect.S_OK, 0)
        self.assertEqual(_simconnect.S_FALSE, 1)