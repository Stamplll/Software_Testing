from FizzBuzz.FizzBuzz_utils import fizzbuzz
import unittest
class FizzBuzzTest(unittest.TestCase):
    def test_give_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(60), "FizzBuzz")   