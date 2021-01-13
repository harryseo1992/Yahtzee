from unittest import TestCase
from yahtzee import three_of_a_kind_checker


class Test(TestCase):
    def test_three_of_a_kind_checker_three_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '2', '3']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_three_of_a_kind_behind(self):
        rolled_dice = ['2', '3', '4', '4', '4']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_three_of_a_kind_middle(self):
        rolled_dice = ['1', '2', '2', '2', '3']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_yahtzee(self):
        rolled_dice = ['1', '1', '1', '1', '1']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_four_of_a_kind_start(self):
        rolled_dice = ['1', '1', '1', '1', '2']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_four_of_a_kind_behind(self):
        rolled_dice = ['2', '4', '4', '4', '4']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_full_house_three_then_two(self):
        rolled_dice = ['1', '1', '1', '2', '2']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_full_house_two_then_three(self):
        rolled_dice = ['1', '1', '2', '2', '2']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_three_of_a_kind_checker_face_value(self):
        rolled_dice = ['1', '1', '2', '2', '3']
        actual = three_of_a_kind_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)
