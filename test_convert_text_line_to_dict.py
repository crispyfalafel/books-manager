from unittest import TestCase
from books import convert_text_line_to_dict


class TestConvertTextLineToDict(TestCase):
    def test_convert_text_line_to_dict_full_line(self):
        value = "Dupre\tSkyscrapers\tBD&L\t12\tArchitecture\t20th Century"
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = {'author': 'Dupre', 'title': 'Skyscrapers', 'publisher': 'BD&L', 'shelf': '12',
                    'category': 'Architecture', 'subject': '20th Century'}
        actual = convert_text_line_to_dict(value, keys)
        self.assertEqual(expected, actual)

    def test_convert_text_line_to_dict_single_none_value(self):
        value = "Eddings\tBelgarath the Sorcerer\t\t34\tFiction\tFantasy"
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = {'author': 'Eddings', 'title': 'Belgarath the Sorcerer', 'publisher': 'None', 'shelf': '34',
                    'category': 'Fiction', 'subject': 'Fantasy'}
        actual = convert_text_line_to_dict(value, keys)
        self.assertEqual(expected, actual)

    def test_convert_text_line_to_dict_multiple_none_values(self):
        value = "\tBelgarath the Sorcerer\t\t34\tFiction\tFantasy"
        keys = ["author", "title", "publisher", "shelf", "category", "subject"]
        expected = {'author': 'None', 'title': 'Belgarath the Sorcerer', 'publisher': 'None', 'shelf': '34',
                    'category': 'Fiction', 'subject': 'Fantasy'}
        actual = convert_text_line_to_dict(value, keys)
        self.assertEqual(expected, actual)
