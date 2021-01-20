import io
from unittest import TestCase
from unittest.mock import patch
from books import print_search_results


class TestPrintSearchResults(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_results_no_results(self, mock_output):
        results = []
        category = "author"
        search_input = "dupre"
        print_search_results(results, category, search_input)
        expected_output = 'Found 0 books with a(n) author containing "dupre".\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_results_one_result(self, mock_output):
        results = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                    'category': 'Architecture', 'subject': '20th Century'}]
        category = "title"
        search_input = "skyscraper"
        print_search_results(results, category, search_input)
        expected_output = 'Found 1 books with a(n) title containing "skyscraper":\n' \
                          '1. Author: Dupre, Title: Skyscrapers, Publisher: BD&L, Shelf: 12, ' \
                          'Category: Architecture, Subject: 20th Century\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_results_multiple_results(self, mock_output):
        results = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                    'category': 'Architecture', 'subject': '20th Century'},
                   {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                    'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                   {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli', 'shelf': '6',
                    'category': 'Architecture', 'subject': '20th Century'}]
        category = "subject"
        search_input = "20th"
        print_search_results(results, category, search_input)
        expected_output = 'Found 3 books with a(n) subject containing "20th":\n' \
                          '1. Author: Dupre, Title: Skyscrapers, Publisher: BD&L, Shelf: 12, ' \
                          'Category: Architecture, Subject: 20th Century\n' \
                          '2. Author: Hollingsworth, Title: Architecture of the 20th Century, Publisher: Exeter, ' \
                          'Shelf: 6, Category: Architecture, Subject: 20th Century\n' \
                          '3. Author: Johnson Burgee, Title: Architecture 1979-1985, Publisher: Rizzoli, ' \
                          'Shelf: 6, Category: Architecture, Subject: 20th Century\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_results_with_None(self, mock_output):
        results = [{'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'None', 'shelf': '12',
                    'category': 'Architecture', 'subject': '20th Century'}]
        category = "title"
        search_input = "skyscraper"
        print_search_results(results, category, search_input)
        expected_output = 'Found 1 books with a(n) title containing "skyscraper":\n' \
                          '1. Author: Dupre, Title: Skyscrapers, Publisher: None, Shelf: 12, ' \
                          'Category: Architecture, Subject: 20th Century\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
