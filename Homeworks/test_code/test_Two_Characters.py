import unittest
from code_under_test.Two_Characters import alternate

class TestTwoCharacters(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_no_valid_pair(self):
        self.assertEqual(alternate("aaaa"), 0)

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)

    def test_two_characters_valid(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_two_characters_invalid(self):
        self.assertEqual(alternate("aabb"), 0)

