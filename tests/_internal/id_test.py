import unittest

from prepar3d._internal import id


class Test(unittest.TestCase):

    def setUp(self):
        self.ids = [id.Id().get() for _ in range(0, 10000)]

    def test_id(self):
        
        self.assertEqual(len(set(self.ids)), 10000)
        self.assertEqual(min(self.ids), 1)
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
