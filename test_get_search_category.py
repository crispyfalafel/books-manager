import io
from unittest import TestCase
from unittest.mock import patch
from books import get_search_category


class TestGetSearchCategory(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_author(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "author"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_title(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "title"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_publisher(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "publisher"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_shelf(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "shelf"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['5'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_category(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "category"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['6'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_search_category_subject(self, book_keys, mock_input):
        actual = get_search_category()
        expected = "subject"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['None'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    def test_get_search_category_invalid_choice(self, book_keys, mock_input):
        actual = get_search_category()
        expected = None
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['6'])
    @patch('books.BOOK_KEYS', return_value=["author", "title", "publisher", "shelf", "category", "subject"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_search_category_subject(self, mock_output, book_keys, mock_input):
        get_search_category()
        function_printed_this = mock_output.getvalue()
        expected_print = "How would you like to search for the book?\n" \
                         "1. Author\n2. Title\n3. Publisher\n4. Shelf\n5. Category\n6. Subject\n"

        self.assertEqual(expected_print, function_printed_this)