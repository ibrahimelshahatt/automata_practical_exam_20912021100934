import unittest
from pda_palindrome_package.pda_palindrome import PDA

class TestPDA(unittest.TestCase):
    def setUp(self):
        self.pda = PDA()

    def test_accepts_palindrome(self):
        self.assertTrue(self.pda.accepts('racecar'))

    def test_rejects_non_palindrome(self):
        self.assertFalse(self.pda.accepts('hello'))

    def test_rejects_even_length(self):
        self.assertFalse(self.pda.accepts('abba'))