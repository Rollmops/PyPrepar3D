import unittest

from prepar3d._internal import id


class Test(unittest.TestCase):

    def test_id(self):
        self.assertEqual(len(set([id.Id().get() for _ in range(0, 10000)])), 10000)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
