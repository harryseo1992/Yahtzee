from unittest import TestCase
from yahtzee import release_dice
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_release_dice_empty_saved(self, mock_output):
        rolled_dice = [1, 3, 5, 6, 4]
        saved_dice = []
        chosen_dice = '3'
        release_dice(rolled_dice, saved_dice, chosen_dice)

        # A print statement telling the user that there are no die of that placement in saved list
        expected = "There is nothing to release.\n"
        self.assertEqual(expected, mock_output.getvalue())

    def test_release_dice_one_saved_release_one(self):
        rolled_dice = [3, 5, 6, 4]
        saved_dice = [1]
        chosen_dice = '1'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        # Should it release an empty saved list as well? I want it to!
        expected = ([1, 3, 4, 5, 6], [])
        self.assertEqual(expected, actual)

    def test_release_dice_two_saved_release_two(self):
        rolled_dice = [5, 6, 4]
        saved_dice = [1, 3]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        chosen_dice = '12'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([1, 4, 5, 6], [3])
        self.assertEqual(expected, actual)

    def test_release_dice_three_saved_release_three(self):
        rolled_dice = [5, 4]
        saved_dice = [1, 3, 6]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        chosen_dice = '136'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([1, 3, 4, 5, 6], [])
        self.assertEqual(expected, actual)

    def test_release_dice_four_saved_release_four(self):
        rolled_dice = [4]
        saved_dice = [1, 3, 6, 5]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        chosen_dice = '5613'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([1, 3, 4, 5, 6], [])
        self.assertEqual(expected, actual)

    def test_release_dice_four_saved_release_one(self):
        rolled_dice = [4]
        saved_dice = [1, 3, 5, 6]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        chosen_dice = '3'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([3, 4], [1, 5, 6])
        self.assertEqual(expected, actual)

    def test_release_dice_four_saved_release_two(self):
        rolled_dice = [4]
        saved_dice = [1, 3, 6, 5]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        chosen_dice = '13'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([1, 3, 4], [5, 6])
        self.assertEqual(expected, actual)

    def test_release_dice_four_saved_release_three(self):
        rolled_dice = [4]
        saved_dice = [1, 3, 6, 5]
        # The numbers do not correlate to the face of the die but their placements as 1st, 2nd, ...
        # Must be typed in ascending order
        chosen_dice = '165'
        actual = release_dice(rolled_dice, saved_dice, chosen_dice)

        expected = ([1, 4, 5, 6], [3])
        self.assertEqual(expected, actual)
