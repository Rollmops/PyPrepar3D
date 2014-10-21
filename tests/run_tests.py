from _internal.flightradar24 import TestCaseFlightradar24
from simconnect.constants import TestCaseSimconnectConstants
from unittest import TestLoader, TestSuite


def get_suite(test_modules):
    return TestSuite([TestLoader().loadTestsFromTestCase(test_module) for test_module in test_modules])

if __name__ == '__main__':
    get_suite([TestCaseSimconnectConstants, TestCaseFlightradar24]).run()