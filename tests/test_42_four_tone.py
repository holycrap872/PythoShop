import unittest
import testBase


class Test(testBase.TestBase, unittest.TestCase):
    manip_func_name = "make_four_tone"
    test_weight = 33

    def __init__(self, test):
        super().__init__(test)
        self.__class__.test_parameters.update({"color": (255, 255, 255), "extra": "0, 0, 0"})
