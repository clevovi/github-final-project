import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Goodbye'),'Au revoir')
        self.assertNotEqual(english_to_french("None"),'')
        self.assertNotEqual(english_to_french(0),0)
        


class TestF2E(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Au revoir'),'Goodbye')
        self.assertNotEqual(french_to_english("None"),'')
        self.assertNotEqual(french_to_english(0),0)

unittest.main()