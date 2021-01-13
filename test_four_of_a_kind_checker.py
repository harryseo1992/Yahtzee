from unittest import TestCase
from yahtzee import four_of_a_kind_checker


class Test(TestCase):
    def test_four_of_a_kind_checker_straight_input(self):

        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['1', '2', '3', '4', '5']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_checker_random_input(self):
        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['1', '2', '2', '3', '6']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_checker_actually_four_of_a_kind(self):
        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['2', '2', '2', '2', '5']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_checker_yahtzee(self):
        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['1', '1', '1', '1', '1']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_checker_three_of_a_kind(self):
        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['1', '1', '1', '2', '3']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_four_of_a_kind_checker_full_house(self):
        # The list should have been converted by convert_and_sort_dice()
        rolled_dice = ['1', '1', '1', '2', '2']

        actual = four_of_a_kind_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)
