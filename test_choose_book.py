import io
from unittest import TestCase
from unittest.mock import patch
from books import choose_book


class TestChooseBook(TestCase):

    @patch('books.get_number_choice', return_value=1)
    def test_choose_book_choose_first_book(self, get_number):
        value = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                  'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli', 'shelf': '6',
                  'category': 'Architecture', 'subject': '20th Century'}]
        actual = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                  'category': 'Architecture', 'subject': '20th Century'}
        expected = choose_book(value)
        self.assertEqual(expected, actual)

    @patch('books.get_number_choice', return_value=3)
    def test_choose_book_choose_last_book(self, get_number):
        value = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                  'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}]
        actual = {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}
        expected = choose_book(value)
        self.assertEqual(expected, actual)

    @patch('books.get_number_choice', return_value=2)
    def test_choose_book_choose_middle_book(self, get_number):
        value = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                  'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}]
        actual = {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}
        expected = choose_book(value)
        self.assertEqual(expected, actual)

    @patch('books.get_number_choice', return_value=None)
    def test_choose_book_invalid_choice(self, get_number):
        value = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                  'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}]
        actual = choose_book(value)
        expected = None
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('books.get_number_choice', return_value=2)
    def test_choose_book_print(self, get_number, mock_output):
        value = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                  'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                 {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                  'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'}]
        choose_book(value)
        expected_output = "Choose a book to move. "
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
