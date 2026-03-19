import unittest
from calculator import Add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(Add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers_return_sum(self):
        self.assertEqual(Add("1,2"), 3)

    def test_three_numbers_return_sum(self):
        self.assertEqual(Add("1,2,3"), 6)

    def test_multiple_numbers_return_sum(self):
        self.assertEqual(Add("1,2,3,4"), 10)

    def test_invalid_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            Add("1,abc")

    def test_newline_delimiter(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_format_newline(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

if __name__ == '__calculator__':
    unittest.main()