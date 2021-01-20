from unittest import TestCase
from books import convert_dict_to_text_line


class TestConvertDictToTextLine(TestCase):

    def test_convert_dict_to_text_line_full_dictionary(self):
        value = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                 'category': 'Architecture', 'subject': '20th Century'}
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = "Dupre\tSkyscrapers\tBD&L\t12\tArchitecture\t20th Century"
        actual = convert_dict_to_text_line(value, keys)
        self.assertEqual(expected, actual)

    def test_convert_dict_to_text_line_missing_information(self):
        value = {'author': 'Eddings', 'title': 'Belgarath the Sorcerer', 'publisher': 'None', 'shelf': '34',
                 'category': 'Fiction', 'subject': 'Fantasy'}
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = "Eddings\tBelgarath the Sorcerer\t\t34\tFiction\tFantasy"
        actual = convert_dict_to_text_line(value, keys)
        self.assertEqual(expected, actual)

    def test_convert_dict_to_text_line_missing_information_multiple(self):
        value = {'author': 'Eddings', 'title': 'None', 'publisher': 'None', 'shelf': '34',
                 'category': 'Fiction', 'subject': 'None'}
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = "Eddings\t\t\t34\tFiction\t"
        actual = convert_dict_to_text_line(value, keys)
        self.assertEqual(expected, actual)