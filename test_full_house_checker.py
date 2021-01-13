from unittest import TestCase
from yahtzee import full_house_checker


class Test(TestCase):
    def test_full_house_checker_first_three_then_two(self):
        rolled_dice = ['1', '1', '1', '2', '2']
        actual = full_house_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_full_house_checker_first_two_then_three(self):
        rolled_dice = ['1', '1', '2', '2', '2']
        actual = full_house_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_full_house_checker_straights(self):
        rolled_dice = ['1', '2', '3', '4', '5']
        actual = full_house_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_full_house_checker_three_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '4', '5']
        actual = full_house_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_full_house_checker_four_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '1', '5']
        actual = full_house_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_full_house_checker_yahtzee(self):
        rolled_dice = ['1', '1', '1', '1', '1']
        actual = full_house_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_full_house_checker_face_value(self):
        rolled_dice = ['1', '2', '2', '4', '4']
        actual = full_house_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)
