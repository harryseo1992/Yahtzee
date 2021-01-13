from unittest import TestCase
from yahtzee import choose_dice


class Test(TestCase):

    def test_choose_dice_choose_one(self):
        given_dice_values = ['1', '2', '3', '4', '5', '6']
        rolled_dice = [1, 1, 6, 3, 5]
        saved_dice = []
        chosen_dice = '1'
        actual = choose_dice(given_dice_values, chosen_dice, rolled_dice, saved_dice)
        expected = ([1, 3, 5, 6], [1])
        self.assertEqual(expected, actual)

    def test_choose_dice_choose_two(self):
        given_dice_values = ['1', '2', '3', '4', '5', '6']
        rolled_dice = [1, 1, 6, 3, 5]
        saved_dice = []
        chosen_dice = '16'
        actual = choose_dice(given_dice_values, chosen_dice, rolled_dice, saved_dice)
        expected = ([1, 3, 5], [1, 6])
        self.assertEqual(expected, actual)

    def test_choose_dice_choose_three(self):
        given_dice_values = ['1', '2', '3', '4', '5', '6']
        rolled_dice = [1, 1, 6, 3, 5]
        saved_dice = []
        chosen_dice = '163'
        actual = choose_dice(given_dice_values, chosen_dice, rolled_dice, saved_dice)
        expected = ([1, 5], [1, 3, 6])
        self.assertEqual(expected, actual)

    def test_choose_dice_choose_four(self):
        given_dice_values = ['1', '2', '3', '4', '5', '6']
        rolled_dice = [1, 1, 6, 3, 5]
        saved_dice = []
        chosen_dice = '1631'
        actual = choose_dice(given_dice_values, chosen_dice, rolled_dice, saved_dice)
        expected = ([5], [1, 1, 3, 6])
        self.assertEqual(expected, actual)

    def test_choose_dice_choose_random(self):
        given_dice_values = ['1', '2', '3', '4', '5', '6']
        rolled_dice = [1, 2, 3, 4, 5]
        saved_dice = []
        chosen_dice = '145'
        actual = choose_dice(given_dice_values, chosen_dice, rolled_dice, saved_dice)
        expected = ([2, 3], [1, 4, 5])
        self.assertEqual(expected, actual)
