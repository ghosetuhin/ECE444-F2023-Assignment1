import unittest
from utils import utils

class TestUtils(unittest.TestCase):
    def test_reversed_int(self):
        utils_obj = utils()
        self.assertEqual(utils_obj.reversed(123), 321)

    def test_reversed_float(self):
        utils_obj = utils()
        self.assertNotEqual(utils_obj.reversed(1.23), 3.21)

    def test_reversed_str(self):
        utils_obj = utils()
        self.assertRaises(TypeError, utils_obj.reversed, "123")

    def test_formatter_int(self):
        utils_obj = utils()
        self.assertEqual(utils_obj.formatter(123), ('0b1111011', '0o173'))

    def test_formatter_float(self):
        utils_obj = utils()
        self.assertRaises(TypeError, utils_obj.formatter, 1.23)

    def test_formatter_str(self):
        utils_obj = utils()
        self.assertRaises(TypeError, utils_obj.formatter, "123")      

if __name__ == "__main__":
    unittest.main()