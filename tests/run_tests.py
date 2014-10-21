from unittest import TestLoader, TestSuite
from simconnect.constants import TestCaseSimconnectConstants
from _internal.flightradar24 import TestCaseFlightradar24


def get_suite(test_modules):
    return TestSuite([TestLoader().loadTestsFromTestCase(test_module) for test_module in test_modules])

if __name__ == '__main__':
    get_suite([TestCaseSimconnectConstants, TestCaseFlightradar24]).run()