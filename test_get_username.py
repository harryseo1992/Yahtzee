from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_username


class Test(TestCase):

    @patch('builtins.input', side_effect=['Harry'])
    def test_get_username(self, mock_input):
        actual = get_username()
        expected = 'Harry'
        self.assertEqual(expected, actual)
