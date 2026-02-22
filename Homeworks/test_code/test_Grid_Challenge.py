import unittest
from code_under_test.Grid_Challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_yes_case(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_no_case(self):
        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_row(self):
        grid = ["cba"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_single_column(self):
        grid = ["a", "b", "c"]
        self.assertEqual(gridChallenge(grid), "YES")

