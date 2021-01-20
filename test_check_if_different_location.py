import io
from unittest import TestCase
from unittest.mock import patch
from books import check_if_different_location


class TestCheckIfDifferentLocation(TestCase):

    def test_check_if_different_location_True(self):
        actual = check_if_different_location('12', '14')
        self.assertTrue(actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_different_location_False(self, mock_output):
        actual = check_if_different_location('12', '12')
        expected_output = "The book is already located at shelf 12.\n"
        actual_output = mock_output.getvalue()
        self.assertFalse(actual)
        self.assertEqual(expected_output, actual_output)
