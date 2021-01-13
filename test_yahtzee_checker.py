from unittest import TestCase
from yahtzee import yahtzee_checker


class Test(TestCase):
    def test_yahtzee_checker_yahtzee_1(self):
        rolled_dice = ['1', '1', '1', '1', '1']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_yahtzee_2(self):
        rolled_dice = ['2', '2', '2', '2', '2']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_yahtzee_3(self):
        rolled_dice = ['3', '3', '3', '3', '3']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_yahtzee_4(self):
        rolled_dice = ['4', '4', '4', '4', '4']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_yahtzee_5(self):
        rolled_dice = ['5', '5', '5', '5', '5']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_yahtzee_6(self):
        rolled_dice = ['6', '6', '6', '6', '6']
        actual = yahtzee_checker(rolled_dice)
        expected = True
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_three_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '2', '3']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_four_of_a_kind(self):
        rolled_dice = ['1', '1', '1', '1', '3']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_full_house(self):
        rolled_dice = ['1', '1', '1', '2', '2']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_full_house_reverse(self):
        rolled_dice = ['1', '1', '2', '2', '2']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_straights(self):
        rolled_dice = ['1', '2', '3', '4', '5']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)

    def test_yahtzee_checker_face_value(self):
        rolled_dice = ['1', '2', '2', '3', '4']
        actual = yahtzee_checker(rolled_dice)
        expected = False
        self.assertEqual(expected, actual)
