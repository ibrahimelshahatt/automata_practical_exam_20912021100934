import unittest
from regex_to_dfa_package.regex_to_dfa import RegexToDFA

class TestRegexToDFA(unittest.TestCase):
    def setUp(self):
        self.regex_to_dfa = RegexToDFA('(a|b)*abb')

    def test_accepts_valid_string(self):
        self.assertTrue(self.regex_to_dfa.accepts('aabb'))

    def test_rejects_invalid_string(self):
        self.assertFalse(self.regex_to_dfa.accepts('abab'))