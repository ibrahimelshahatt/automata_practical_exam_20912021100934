from automata.fa.dfa import DFA
from automata.regex.regex import Regex

class RegexToDFA:
    def __init__(self, regex):
        self.regex = regex
        self.dfa = self._create_dfa()

    def _create_dfa(self):
        nfa = Regex(self.regex).to_epsilon_nfa()
        dfa = DFA.from_nfa(nfa)
        return dfa

    def accepts(self, string):
        return self.dfa.accepts_input(string)