import unittest
from code_under_test.Alternating_Characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_no_deletion_needed(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_one_deletion(self):
        self.assertEqual(alternatingCharacters("AAB"), 1)

    def test_multiple_deletions(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_all_same(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

