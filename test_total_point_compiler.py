from unittest import TestCase
from unittest.mock import patch
from yahtzee import total_point_compiler
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_total_point_compiler(self, mock_stdout):
        score = {"username": "Harry", "1": -1, "2": -1, "3": -1, "4": -1,
                 "5": -1, "6": -1, "top half bonus": -1, "three of a kind": -1,
                 "four of a kind": -1, "full house": -1, "small straight": -1,
                 "large straight": -1, "yahtzee": -1, "yahtzee counter": -1, "chance": -1,
                 "total": 0}
        total_point_compiler(score)
        expected = "=================	Harry	=======================\n" \
                   "One:	-1		Three of a kind:	-1	Chance:	-1\n" \
                   "Two:	-1		Four of a kind:		-1	Total:	0\n" \
                   "Three:	-1		Full House:			-1\n" \
                   "Four:	-1		Small Straight:		-1\n" \
                   "Five:	-1		Large Straight:		-1\n" \
                   "Six:	-1		YAHTZEE:			-1\n" \
                   "Bonus:	-1		Yahtzee counter:	-1\n"
        self.assertEqual(expected, mock_stdout.getvalue())
