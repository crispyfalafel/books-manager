from unittest import TestCase
from books import find_valid_shelves


class TestFindValidShelves(TestCase):
    def test_find_valid_shelves_numerical_sort(self):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '34',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '6', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '62', 'category': 'Architecture', 'subject': '20th Century'})
        expected = ['6', '34', '62']
        actual = find_valid_shelves(values)
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_alphabetical_sort(self):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'kitchen',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': 'bedroom', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': 'bathroom', 'category': 'Architecture', 'subject': '20th Century'})
        expected = ['bathroom', 'bedroom', 'kitchen']
        actual = find_valid_shelves(values)
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_with_duplicate_numbers(self):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '34',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': '34', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '8', 'category': 'Architecture', 'subject': '20th Century'})
        expected = ['8', '34']
        actual = find_valid_shelves(values)
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_with_duplicate_words(self):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': 'garden',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': 'bedroom', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': 'garden', 'category': 'Architecture', 'subject': '20th Century'})
        expected = ['bedroom', 'garden']
        actual = find_valid_shelves(values)
        self.assertEqual(expected, actual)

    def test_find_valid_shelves_numbers_and_words(self):
        values = ({'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '34',
                   'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Hollingsworth', 'title': 'Architecture of the 20th Century', 'publisher': 'Exeter',
                   'shelf': 'backyard', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': '8', 'category': 'Architecture', 'subject': '20th Century'},
                  {'author': 'Johnson Burgee', 'title': 'Architecture 1979-1985', 'publisher': 'Rizzoli',
                   'shelf': 'garden', 'category': 'Architecture', 'subject': '20th Century'})
        expected = ['8', '34', 'backyard', 'garden']
        actual = find_valid_shelves(values)
        self.assertEqual(expected, actual)
