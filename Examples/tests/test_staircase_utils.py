import unittest
from Staircase.staircase_utils import staircase


class TestStaircase(unittest.TestCase):

    def test_basic_case(self):
        # Arrange
        n = 4
        ch = "#"
        expected = "   #\n  ##\n ###\n####"

        # Act
        result = staircase(n, ch)

        # Assert
        self.assertEqual(result, expected)


    def test_invalid_n(self):
        # Arrange
        n = 0
        ch = "#"

        # Act / Assert
        with self.assertRaises(ValueError):
            staircase(n, ch)


    def test_custom_character(self):
        # Arrange
        n = 3
        ch = "*"
        expected = "  *\n **\n***"

        # Act
        result = staircase(n, ch)

        # Assert
        self.assertEqual(result, expected)

    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = '#'
        expected_output = \
        " #\n" + "##"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_invalid_length_of_character(self):
        # arrange
        n = 3
        pattern = '##'
        # act / assert
        with self.assertRaises(ValueError):
            staircase(n, pattern)

