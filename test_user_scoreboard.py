from unittest import TestCase
from yahtzee import user_scoreboard


class Test(TestCase):
    def test_user_scoreboard(self):
        username = 'Sam Vimes'
        actual = user_scoreboard(username)
        expected = {"username": "Sam Vimes", "1": -1, "2": -1, "3": -1, "4": -1,
                    "5": -1, "6": -1, "top half bonus": -1, "three of a kind": -1,
                    "four of a kind": -1, "full house": -1, "small straight": -1, "large straight": -1,
                    "yahtzee": -1, "yahtzee counter": -1, "chance": -1, "total": 0}
        self.assertEqual(expected, actual)
