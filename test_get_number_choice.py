import io
from unittest import TestCase
from unittest.mock import patch
from books import get_number_choice


class TestGetNumberChoice(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_number_choice_only_one_choice(self, mock_input):
        value = 1
        actual = get_number_choice(value)
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_get_number_choice_lowest_choice(self, mock_input):
        value = 10
        actual = get_number_choice(value)
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['10'])
    def test_get_number_choice_highest_choice(self, mock_input):
        value = 10
        actual = get_number_choice(value)
        expected = 10
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['10'])
    def test_get_number_choice_middle_choice(self, mock_input):
        value = 20
        actual = get_number_choice(value)
        expected = 10
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['11'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_number_choice_invalid_too_high(self, mock_output, mock_input):
        value = 10
        actual = get_number_choice(value)
        expected = None
        actual_output = mock_output.getvalue()
        expected_output = "Number out of range.\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_number_choice_invalid_too_low(self, mock_output, mock_input):
        value = 20
        actual = get_number_choice(value)
        expected = None
        actual_output = mock_output.getvalue()
        expected_output = "Number out of range.\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['dfs3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_number_choice_invalid_not_a_number(self, mock_output, mock_input):
        value = 20
        actual = get_number_choice(value)
        expected = None
        actual_output = mock_output.getvalue()
        expected_output = "Please enter a number.\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_output, actual_output)
