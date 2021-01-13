from unittest import TestCase
from unittest.mock import patch
from yahtzee import dice_roll


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_dice_roll_1(self, random_number_generator):
        # MAKE SURE THE NUMBERS ARE WITHIN 1 AND 6
        list_of_dice = [3, 4, 5, 1, 2]
        actual = dice_roll(list_of_dice)
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_dice_roll_3(self, random_number_generator):
        # MAKE SURE THE NUMBERS ARE WITHIN 1 AND 6
        list_of_dice = [3, 4, 5, 1, 2]
        actual = dice_roll(list_of_dice)
        expected = [3, 3, 3, 3, 3]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=6)
    def test_dice_roll_6(self, random_number_generator):
        # MAKE SURE THE NUMBERS ARE WITHIN 1 AND 6
        list_of_dice = [3, 4, 5, 1, 2]
        actual = dice_roll(list_of_dice)
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(expected, actual)
