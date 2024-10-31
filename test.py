import unittest
import os
from io import StringIO
from unittest.mock import mock_open, patch
from main import count_digits, count_digits_in_file_and_replace_odds, replace_odd_digits_with_random_letter

class TestDigitReplacement(unittest.TestCase):
    
    def test_replace_odd_digits_with_random_letter(self):
        # Test with a string containing odd and even digits
        text = "a1b2c3d4e5"
        modified_text = replace_odd_digits_with_random_letter(text)
        
        # Ensure odd digits are replaced with letters, even digits are untouched
        for i, c in enumerate(text):
            if c.isdigit() and int(c) % 2 != 0:
                self.assertTrue(modified_text[i].isalpha())
            else:
                self.assertEqual(modified_text[i], c)

    def test_count_digits(self):
        # Test with a string containing digits and letters
        text = "abc123"
        digit_count = count_digits(text)
        self.assertEqual(digit_count, 3)  # Only '123' are digits
    
    @patch("builtins.open", new_callable=mock_open, read_data="123abc456")
    def test_count_digits_in_file_and_replace_odds(self, mock_file):
        file_path = 'test.txt'
        
        # Run the function with the mock file
        digit_count_before, digit_count_after = count_digits_in_file_and_replace_odds(file_path)
        
        # Check that the counts before and after are correct
        self.assertEqual(digit_count_before, 6)  # Initial digit count is 6 (123456)
        self.assertEqual(digit_count_after, 3)  # Only even digits (2, 4, 6) should remain

        # Verify the modified text by checking the file write calls
        handle = mock_file()
        handle.write.assert_called_once()
        written_text = handle.write.call_args[0][0]
        
        # Ensure that odd digits (1, 3, 5) are replaced with letters
        for i, c in enumerate("123abc456"):
            if c.isdigit() and int(c) % 2 != 0:
                self.assertTrue(written_text[i].isalpha())
            else:
                self.assertEqual(written_text[i], c)
        
if __name__ == '__main__':
    unittest.main()
