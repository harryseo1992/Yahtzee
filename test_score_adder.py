from unittest import TestCase
from unittest.mock import patch
from yahtzee import score_adder
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_score_adder_yahtzee(self, mock_stdout):
        score = {"username": "Sofia", "1": -1, "2": -1, "3": -1, "4": -1,
                 "5": -1, "6": -1, "top half bonus": -1, "three of a kind": -1,
                 "four of a kind": -1, "full house": -1, "small straight": -1,
                 "large straight": -1, "yahtzee": -1, "yahtzee counter": -1, "chance": -1,
                 "total": 0}
        rolled = ['1', '1', '1', '1', '1']
        category = 'yahtzee'
        score_adder(score, rolled, category)
        expected = "=================	Sofia	=======================\n" \
                   "One:	-1		Three of a kind:	-1	Chance:	-1\n" \
                   "Two:	-1		Four of a kind:		-1	Total:	50\n" \
                   "Three:	-1		Full House:			-1\n" \
                   "Four:	-1		Small Straight:		-1\n" \
                   "Five:	-1		Large Straight:		-1\n" \
                   "Six:	-1		YAHTZEE:			50\n" \
                   "Bonus:	-1		Yahtzee counter:	1\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_score_adder_ones(self, mock_stdout):
        score = {"username": "Garfield", "1": -1, "2": -1, "3": -1, "4": -1,
                 "5": -1, "6": -1, "top half bonus": -1, "three of a kind": -1,
                 "four of a kind": -1, "full house": -1, "small straight": -1,
                 "large straight": -1, "yahtzee": -1, "yahtzee counter": -1, "chance": -1,
                 "total": 0}
        rolled = ['1', '1', '1', '1', '1']
        category = '1'
        score_adder(score, rolled, category)
        expected = "=================	Garfield	=======================\n" \
                   "One:	5		Three of a kind:	-1	Chance:	-1\n" \
                   "Two:	-1		Four of a kind:		-1	Total:	5\n" \
                   "Three:	-1		Full House:			-1\n" \
                   "Four:	-1		Small Straight:		-1\n" \
                   "Five:	-1		Large Straight:		-1\n" \
                   "Six:	-1		YAHTZEE:			-1\n" \
                   "Bonus:	-1		Yahtzee counter:	-1\n"
        self.assertEqual(expected, mock_stdout.getvalue())
