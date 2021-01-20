from unittest import TestCase
from unittest.mock import patch
from books import get_menu_input


class TestGetMenuInput(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_menu_input_choose_search(self, mock_input):
        expected = "search"
        actual = get_menu_input()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_get_menu_input_choose_move(self, mock_input):
        expected = "move"
        actual = get_menu_input()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_get_menu_input_choose_quit(self, mock_input):
        expected = "quit"
        actual = get_menu_input()
        self.assertEqual(actual, expected)
