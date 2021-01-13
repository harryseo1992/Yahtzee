from unittest import TestCase
from yahtzee import large_straight_checker


class Test(TestCase):
    def test_large_straight_checker_small_straight(self):
        rolled_dice = ['1', '2', '3', '4', '6']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)

    def test_large_straight_checker_full_house(self):
        rolled_dice = ['1', '1', '1', '4', '4']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)

    def test_large_straight_checker_three_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '4', '6']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)

    def test_large_straight_checker_four_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '1', '6']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)

    def test_large_straight_checker_face_value(self):
        rolled_dice = ['1', '2', '2', '4', '6']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)

    def test_large_straight_checker_yahtzee(self):
        rolled_dice = ['1', '1', '1', '1', '1']
        actual = large_straight_checker(rolled_dice)

        # False because it is not large straight
        expected = False
        self.assertEqual(expected, actual)
