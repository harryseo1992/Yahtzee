from unittest import TestCase
from yahtzee import yahtzee_point_adder


class Test(TestCase):
    def test_yahtzee_point_adder_start_of_the_game(self):
        # If the scoreboard['yahtzee'] is None or if the counter is 0
        scoreboard = {"username": "Harry", "yahtzee": -1, "yahtzee counter": -1}
        actual = yahtzee_point_adder(scoreboard)
        expected = {"username": "Harry", "yahtzee": 50, "yahtzee counter": 1}
        self.assertEqual(expected, actual)

    def test_yahtzee_point_adder_1_yahtzee_already(self):
        scoreboard = {"username": "Harry", "yahtzee": 50, "yahtzee counter": 1}
        actual = yahtzee_point_adder(scoreboard)
        expected = {"username": "Harry", "yahtzee": 150, "yahtzee counter": 2}
        self.assertEqual(expected, actual)

    def test_yahtzee_point_adder_many_yahtzee_already(self):
        scoreboard = {"username": "Harry", "yahtzee": 350, "yahtzee counter": 4}
        actual = yahtzee_point_adder(scoreboard)
        expected = {"username": "Harry", "yahtzee": 450, "yahtzee counter": 5}
        self.assertEqual(expected, actual)

    def test_yahtzee_point_adder_already_gave_up_on_yahtzee(self):
        scoreboard = {"username": "Harry", "yahtzee": 0, "yahtzee counter": 0}
        actual = yahtzee_point_adder(scoreboard)
        # Because scoreboard['yahtzee'] is already 0
        # Would I need to put yahtzee checker for all the checkers or guide the score adder in a way
        # that if all regex fails, the value is turned into 0
        expected = {"username": "Harry", "yahtzee": 0, "yahtzee counter": 0}
        self.assertEqual(expected, actual)
