import unittest
from translator import english_to_french
from translator import french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        #Test for null input
        self.assertNotEqual(english_to_french("Null"), '')
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        #Test for null input
        self.assertNotEqual(french_to_english("Null"), '')
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
