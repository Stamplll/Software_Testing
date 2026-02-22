import unittest
from Cat_and_Mouse.cat_and_mouse import cat_and_mouse
class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_closer(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")

    def test_cat_b_closer(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_both_cats_same_distance(self):
        self.assertEqual(cat_and_mouse(1, 5, 3), "Mouse C")