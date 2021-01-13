from unittest import TestCase
from yahtzee import top_half_adder


class Test(TestCase):
    def test_top_half_adder_for_twos_from_none(self):
        scoreboard = {"username": "Harry", "1": -1, "2": -1, "3": -1}
        rolled_dice = ['1', '2', '2', '3', '4']
        user_input_for_face_value = '2'
        actual = top_half_adder(scoreboard, rolled_dice, user_input_for_face_value)
        expected = {"username": "Harry", "1": -1, "2": 4, "3": -1}
        self.assertEqual(expected, actual)

    def test_top_half_adder_from_some_value(self):
        scoreboard = {"username": "Harry", "1": -1, "2": 4, "3": -1}
        rolled_dice = ['1', '2', '2', '2', '2']
        user_input_for_face_value = '2'
        actual = top_half_adder(scoreboard, rolled_dice, user_input_for_face_value)

        # The point should not change as there already is a value inside that is greater than -1
        expected = {"username": "Harry", "1": -1, "2": 4, "3": -1}
        self.assertEqual(expected, actual)

    def test_top_half_adder_from_0_value(self):
        scoreboard = {"username": "Harry", "1": -1, "2": 0, "3": -1}
        rolled_dice = ['1', '2', '2', '3', '4']
        user_input_for_face_value = '2'
        actual = top_half_adder(scoreboard, rolled_dice, user_input_for_face_value)

        expected = {"username": "Harry", "1": -1, "2": 0, "3": -1}
        self.assertEqual(expected, actual)

    def test_top_half_adder_for_ones_from_none(self):
        scoreboard = {"username": "Harry", "1": -1, "2": -1, "3": -1}
        rolled_dice = ['1', '1', '1', '1', '1']
        user_input_for_face_value = '1'
        actual = top_half_adder(scoreboard, rolled_dice, user_input_for_face_value)
        expected = {"username": "Harry", "1": 5, "2": -1, "3": -1}
        self.assertEqual(expected, actual)

    def test_top_half_adder_for_threes_from_none(self):
        scoreboard = {"username": "Harry", "1": -1, "2": -1, "3": -1}
        rolled_dice = ['1', '1', '1', '1', '3']
        user_input_for_face_value = '3'
        actual = top_half_adder(scoreboard, rolled_dice, user_input_for_face_value)
        expected = {"username": "Harry", "1": -1, "2": -1, "3": 3}
        self.assertEqual(expected, actual)
