from unittest import TestCase
from yahtzee import convert_and_sort_dice


class Test(TestCase):
    def test_convert_and_sort_dice_one_die_in_rolled_dice(self):
        list_of_rolled_dice = [4]
        list_of_saved_dice = [5, 4, 1, 6]
        actual = convert_and_sort_dice(list_of_rolled_dice, list_of_saved_dice)
        expected = ['1', '4', '4', '5', '6']
        self.assertEqual(expected, actual)

    def test_convert_and_sort_dice_two_dice_in_rolled_dice(self):
        list_of_rolled_dice = [6, 4]
        list_of_saved_dice = [5, 4, 2]
        actual = convert_and_sort_dice(list_of_rolled_dice, list_of_saved_dice)
        expected = ['2', '4', '4', '5', '6']
        self.assertEqual(expected, actual)

    def test_convert_and_sort_dice_three_dice_in_rolled_dice(self):
        list_of_rolled_dice = [6, 4, 6]
        list_of_saved_dice = [5, 2]
        actual = convert_and_sort_dice(list_of_rolled_dice, list_of_saved_dice)
        expected = ['2', '4', '5', '6', '6']
        self.assertEqual(expected, actual)

    def test_convert_and_sort_dice_four_dice_in_rolled_dice(self):
        list_of_rolled_dice = [6, 4, 6, 5]
        list_of_saved_dice = [2]
        actual = convert_and_sort_dice(list_of_rolled_dice, list_of_saved_dice)
        expected = ['2', '4', '5', '6', '6']
        self.assertEqual(expected, actual)

    def test_convert_and_sort_dice_five_dice_in_rolled_dice(self):
        list_of_rolled_dice = [6, 4, 6, 5, 1]
        list_of_saved_dice = []
        actual = convert_and_sort_dice(list_of_rolled_dice, list_of_saved_dice)
        expected = ['1', '4', '5', '6', '6']
        self.assertEqual(expected, actual)
