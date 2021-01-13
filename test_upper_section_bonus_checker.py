from unittest import TestCase
from yahtzee import upper_section_bonus_checker


class Test(TestCase):

    # Should this return bool or return a scoreboard of added upper section bonus?
    def test_upper_section_bonus_checker_all_none_or_start_of_the_game(self):
        scoreboard = {"username": "Harry", "1": -1, "2": -1, "3": -1, "4": -1,
                      "5": -1, "6": -1}
        actual = upper_section_bonus_checker(scoreboard)

        expected = False
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_middle_of_the_game(self):
        scoreboard = {"username": "Harry", "1": 1, "2": 6, "3": 9, "4": -1,
                      "5": 0, "6": 0}
        actual = upper_section_bonus_checker(scoreboard)

        expected = False
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_middle_of_the_game_over_63(self):
        scoreboard = {"username": "Harry", "1": 5, "2": 12, "3": 9, "4": 20,
                      "5": 30, "6": -1}
        actual = upper_section_bonus_checker(scoreboard)

        expected = True
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_middle_of_the_game_is_63(self):
        scoreboard = {"username": "Harry", "1": 3, "2": 12, "3": 18, "4": 0,
                      "5": 30, "6": -1}
        actual = upper_section_bonus_checker(scoreboard)

        expected = True
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_end_of_the_game_over_63(self):
        scoreboard = {"username": "Harry", "1": 5, "2": 12, "3": 18, "4": 20,
                      "5": 30, "6": 0}
        actual = upper_section_bonus_checker(scoreboard)

        expected = True
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_end_of_the_game_is_63(self):
        scoreboard = {"username": "Harry", "1": 3, "2": 12, "3": 18, "4": 0,
                      "5": 30, "6": 0}
        actual = upper_section_bonus_checker(scoreboard)

        expected = True
        self.assertEqual(expected, actual)

    def test_upper_section_bonus_checker_end_of_the_game_not_63(self):
        scoreboard = {"username": "Harry", "1": 1, "2": 2, "3": 3, "4": 4,
                      "5": 5, "6": 6}
        actual = upper_section_bonus_checker(scoreboard)

        expected = False
        self.assertEqual(expected, actual)
