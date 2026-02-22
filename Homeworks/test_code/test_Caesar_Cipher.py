import unittest
from code_under_test.Caesar_Cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_uppercase_shift(self):
        self.assertEqual(caesarCipher("ABC", 3), "DEF")

    def test_lowercase_shift(self):
        self.assertEqual(caesarCipher("abc", 2), "cde")

    def test_mixed_case(self):
        self.assertEqual(caesarCipher("AbC", 1), "BcD")

    def test_wrap_around(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_large_k(self):
        self.assertEqual(caesarCipher("abc", 29), "def")

    def test_non_alphabet(self):
        self.assertEqual(caesarCipher("a1!B", 2), "c1!D")

    def test_zero_shift(self):
        self.assertEqual(caesarCipher("Hello", 0), "Hello")
