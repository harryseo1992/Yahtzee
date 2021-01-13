from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import choose_dice_handler


class Test(TestCase):

    def test_choose_dice_handler(self):
        rolled_dice = [1, 2, 3, 4, 5]
        saved_dice = []
        chosen_dice = ''
        actual = choose_dice_handler(rolled_dice, saved_dice, chosen_dice)
        expected = ([1, 2, 3, 4, 5], [])
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_dice_handler_chosen_string_length_greater_than_4(self, mock_stdout):
        rolled_dice = [1, 2, 3, 4, 5]
        saved_dice = []
        chosen_dice = '12345'
        choose_dice_handler(rolled_dice, saved_dice, chosen_dice)
        expected = "You can't save more than 4 dice.\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_dice_handler_saved_list_already_has_4_elements(self, mock_stdout):
        rolled_dice = [1]
        saved_dice = [2, 3, 4, 5]
        chosen_dice = '1'
        choose_dice_handler(rolled_dice, saved_dice, chosen_dice)
        expected = "You have reached the maximum allotted capacity. Cannot save more than what you have.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
