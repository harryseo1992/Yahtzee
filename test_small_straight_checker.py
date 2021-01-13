from unittest import TestCase
from yahtzee import small_straight_checker


class Test(TestCase):
    def test_small_straight_checker_small_straight(self):
        rolled_dice = ['1', '2', '3', '4', '6']
        actual = small_straight_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_small_straight_checker_small_straight_one_extra_at_start(self):
        rolled_dice = ['1', '1', '2', '3', '4']
        actual = small_straight_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_small_straight_checker_small_straight_one_extra_in_middle(self):
        rolled_dice = ['1', '2', '3', '3', '4']
        actual = small_straight_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_small_straight_checker_large_straight_start_from_one(self):
        rolled_dice = ['1', '2', '3', '4', '5']
        actual = small_straight_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_small_straight_checker_large_straight_start_from_two(self):
        rolled_dice = ['2', '3', '4', '5', '6']
        actual = small_straight_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_small_straight_checker_full_house(self):
        rolled_dice = ['1', '1', '1', '6', '6']
        actual = small_straight_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_small_straight_checker_three_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '4', '6']
        actual = small_straight_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_small_straight_checker_four_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '1', '6']
        actual = small_straight_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_small_straight_checker_face_value(self):
        rolled_dice = ['1', '1', '2', '4', '6']
        actual = small_straight_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_small_straight_checker_yahtzee(self):
        rolled_dice = ['1', '1', '1', '1', '1']
        actual = small_straight_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)
