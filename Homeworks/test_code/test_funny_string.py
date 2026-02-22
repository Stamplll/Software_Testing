import unittest
from code_under_test.Funny_String import funnystring

class TestFunnyString(unittest.TestCase):

    def test_funny_case(self):
        self.assertEqual(funnystring("acxz"), "Funny")

    def test_not_funny_case(self):
        self.assertEqual(funnystring("bcxz"), "Not Funny")

    def test_length_two(self):
        self.assertEqual(funnystring("ab"), "Funny")

    def test_all_same(self):
        self.assertEqual(funnystring("aaa"), "Funny")

