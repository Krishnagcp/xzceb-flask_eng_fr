"""
Module tests
This module contains unit tests for the translator module.
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Test class for the translator module.
    """

    def test_e2f_assert_equal(self):
        """Test English to French translation using assertEqual."""
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_e2f_assert_not_equal(self):
        """Test English to French translation using assertNotEqual."""
        self.assertNotEqual(english_to_french("Hello"), "Hello")

    def test_f2e_assert_equal(self):
        """Test French to English translation using assertEqual."""
        self.assertEqual(french_to_english("Bonjour"), "Hi")

    def test_f2e_assert_not_equal(self):
        """Test French to English translation using assertNotEqual."""
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()