import unittest
from Task_1 import longest_substring


class MyTestCase(unittest.TestCase):
    def test_invalid_input_type(self):  # Test - wrong type of input
        self.assertRaises(TypeError, longest_substring, {'a': 1, 'b': 2})

    def test_empty_string(self):  # Test - empty input string
        self.assertEqual(0, longest_substring(""))

    def test_one_character(self):  # Test - one character in input string
        self.assertEqual(1, longest_substring("aaaaa"))

    def test_all_characters_different(self):  # Test - all characters are different
        self.assertEqual(7, longest_substring("english"))

    def test_few_repetitions(self):  # Test - there are several repetitions
        self.assertEqual(4, longest_substring("abcabcddd"))

    def test_uperr_lower_cases(self):  # Test - recognition of letters of different sizes
        self.assertEqual(4, longest_substring("AabB"))


if __name__ == '__main__':
    unittest.main()