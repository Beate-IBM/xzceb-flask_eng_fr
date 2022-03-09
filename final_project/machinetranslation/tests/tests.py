""" Unit tests """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ English to French """
    def test1(self):
        """ Tests for English to French """
        self.assertIsNotNone(english_to_french('Hello'))
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """ French to English """
    def test1(self):
        """ Tests for French to English """
        self.assertIsNotNone(french_to_english('Bonjour'))
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
