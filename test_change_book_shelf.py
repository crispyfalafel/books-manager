import io
from unittest import TestCase
from unittest.mock import patch
from books import change_book_shelf


class TestChangeBookShelf(TestCase):

    def test_change_book_shelf_numeric_shelf(self):
        value = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                 'category': 'Architecture', 'subject': '20th Century'}
        destination = '1'
        expected = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                    'category': 'Architecture', 'subject': '20th Century'}
        change_book_shelf(value, destination)
        self.assertEqual(expected, value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_book_shelf_numeric_shelf_print(self, mock_output):
        value = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                 'category': 'Architecture', 'subject': '20th Century'}
        destination = '1'
        change_book_shelf(value, destination)

        expected_output = '"Skyscrapers" was successfully moved to shelf 1.\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    def test_change_book_shelf_word_shelf(self):
        value = {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                 'shelf': 'island', 'category': 'Architecture', 'subject': '20th Century'}
        destination = 'garden'
        expected = {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                    'shelf': 'garden', 'category': 'Architecture', 'subject': '20th Century'}

        change_book_shelf(value, destination)
        self.assertEqual(expected, value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_change_book_shelf_word_shelf_print(self, mock_output):
        value = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                 'category': 'Architecture', 'subject': '20th Century'}
        destination = 'Island'
        change_book_shelf(value, destination)

        expected_output = '"Skyscrapers" was successfully moved to shelf Island.\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
