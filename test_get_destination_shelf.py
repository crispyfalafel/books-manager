import io
from unittest import TestCase
from unittest.mock import patch
from books import get_destination_shelf


class TestGetDestinationShelf(TestCase):

    @patch('books.check_if_different_location', return_value=True)
    @patch('books.get_number_choice', return_value=1)
    def test_get_destination_shelf_lowest_choice(self, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        expected = '8'
        actual = get_destination_shelf(values, current_location)

        self.assertEqual(expected, actual)

    @patch('books.check_if_different_location', return_value=True)
    @patch('books.get_number_choice', return_value=4)
    def test_get_destination_shelf_highest_choice(self, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        expected = 'garden'
        actual = get_destination_shelf(values, current_location)
        self.assertEqual(expected, actual)

    @patch('books.check_if_different_location', return_value=True)
    @patch('books.get_number_choice', return_value=3)
    def test_get_destination_shelf_middle_choice(self, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        expected = 'backyard'
        actual = get_destination_shelf(values, current_location)
        self.assertEqual(expected, actual)

    @patch('books.check_if_different_location', return_value=True)
    @patch('books.get_number_choice', return_value=None)
    def test_get_destination_shelf_invalid_shelf_choice(self, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        expected = None
        actual = get_destination_shelf(values, current_location)
        self.assertEqual(expected, actual)

    @patch('books.check_if_different_location', return_value=False)
    @patch('books.get_number_choice', return_value=2)
    def test_get_destination_shelf_invalid_same_location(self, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        expected = None
        actual = get_destination_shelf(values, current_location)
        self.assertEqual(expected, actual)

    @patch('books.check_if_different_location', return_value=True)
    @patch('books.get_number_choice', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_destination_shelf_print_choices(self, mock_output, get_choice, different_locations):
        values = ['8', '34', 'backyard', 'garden']
        current_location = '34'
        actual = get_destination_shelf(values, current_location)

        expected_output = "Select a destination shelf:\n" \
                          "1. 8\n2. 34\n3. backyard\n4. garden\n" \
                          "The book is currently located at shelf 34.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
