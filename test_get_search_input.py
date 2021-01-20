import io
from unittest import TestCase
from unittest.mock import patch
from books import get_search_input


class TestGetSearchInput(TestCase):
    @patch('builtins.input', side_effect=['a'])
    def test_get_search_input_one_lowercase_char(self, mock_input):
        actual = get_search_input()
        expected = "a"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['TsDFTsd'])
    def test_get_search_input_mixed_case_word(self, mock_input):
        actual = get_search_input()
        expected = "tsdftsd"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['This is a patch test'])
    def test_get_search_input_mixed_case_many_words(self, mock_input):
        actual = get_search_input()
        expected = "this is a patch test"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['Test 123'])
    def test_get_search_input_string_with_numbers(self, mock_input):
        actual = get_search_input()
        expected = "test 123"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_get_search_input_empty_string(self, mock_input, mock_output):
        actual = get_search_input()
        expected = ""
        expected_output = "Enter a search input.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(actual, expected)
        self.assertEqual(expected_output, actual_output)




