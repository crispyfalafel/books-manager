import io
from unittest import TestCase
from unittest.mock import patch
from books import search_book


class TestSearchBook(TestCase):

    @patch('books.get_search_input', return_value='du')
    @patch('books.get_search_category', return_value='author')
    def test_search_book_partial_search(self, search_category, search_input):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '34',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '34', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '8', 'category': 'Architecture', 'subject': '20th Century'})
        expected = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '34',
                     'category': 'Architecture', 'subject': '20th Century'},
                    {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                     'shelf': '34', 'category': 'Architecture', 'subject': '20th Century'}]
        actual = search_book(values)
        self.assertEqual(expected, actual)

    @patch('books.get_search_input', return_value='1')
    @patch('books.get_search_category', return_value='shelf')
    def test_search_book_search_by_exact_shelf_numeric(self, search_category, search_input):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '21', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '11', 'category': 'Architecture', 'subject': '20th Century'})
        expected = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                     'category': 'Architecture', 'subject': '20th Century'}]
        actual = search_book(values)
        self.assertEqual(expected, actual)

    @patch('books.get_search_input', return_value='island')
    @patch('books.get_search_category', return_value='shelf')
    def test_search_book_search_by_partial_shelf_word(self, search_category, search_input):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'Island',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '21', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': 'My Island', 'category': 'Architecture', 'subject': '20th Century'})
        expected = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'Island',
                     'category': 'Architecture', 'subject': '20th Century'},
                    {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                     'shelf': 'My Island', 'category': 'Architecture', 'subject': '20th Century'}]
        actual = search_book(values)
        self.assertEqual(expected, actual)

    @patch('books.get_search_input', return_value='1')
    @patch('books.get_search_category', return_value=None)
    def test_search_book_invalid_search_category(self, search_category, search_input):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '1',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '21', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '11', 'category': 'Architecture', 'subject': '20th Century'})
        expected = None
        actual = search_book(values)
        self.assertEqual(expected, actual)

    @patch('books.get_search_input', return_value='')
    @patch('books.get_search_category', return_value='shelf')
    def test_search_book_invalid_search_input(self, search_category, search_input):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Du', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '21', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '11', 'category': 'Architecture', 'subject': '20th Century'})
        expected = None
        actual = search_book(values)
        self.assertEqual(expected, actual)