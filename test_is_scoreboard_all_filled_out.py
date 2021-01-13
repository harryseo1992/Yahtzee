from unittest import TestCase
from yahtzee import is_scoreboard_all_filled_out


class Test(TestCase):
    def test_is_scoreboard_all_filled_out_start_of_the_game(self):
        scoreboard = {"username": "Harry", "ones": -1, "twos": -1, "threes": -1}
        actual = is_scoreboard_all_filled_out(scoreboard)
        # USE -1 INSTEAD OF NONE AND CHECK FOR 0 OR GREATER INSTEAD OF NONE
        # Should be False because there are None values in there still
        expected = False
        self.assertEqual(expected, actual)

    def test_is_scoreboard_all_filled_out_mid_of_the_game(self):
        scoreboard = {"username": "Harry", "ones": -1, "twos": 4, "threes": -1}
        actual = is_scoreboard_all_filled_out(scoreboard)

        # Should be False because there are None values in there still
        expected = False
        self.assertEqual(expected, actual)

    def test_is_scoreboard_all_filled_out_end_of_the_game(self):
        scoreboard = {"username": "Harry", "ones": 1, "twos": 2, "threes": 3}
        actual = is_scoreboard_all_filled_out(scoreboard)

        # Should be True because there are no None values in the dictionary
        expected = True
        self.assertEqual(expected, actual)
