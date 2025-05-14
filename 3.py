class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = 'q0'
        self.transitions = {
            'q0': {'0': ('X', 'R', 'q1'), 'Y': ('Y', 'R', 'q6'), '_': ('_', 'R', 'accept')},
            'q1': {'0': ('0', 'R', 'q1'), '1': ('Y', 'R', 'q2'), 'Y': ('Y', 'R', 'q1')},
            'q2': {'1': ('1', 'R', 'q2'), '0': ('Z', 'R', 'q3'), 'Z': ('Z', 'R', 'q2')},
            'q3': {'0': ('0', 'R', 'q3'), '1': ('W', 'L', 'q4'), 'W': ('W', 'R', 'q3')},
            'q4': {'0': ('0', 'L', 'q4'), 'Z': ('Z', 'L', 'q4'), 'Y': ('Y', 'L', 'q4'), 
                   'X': ('X', 'R', 'q0'), 'W': ('W', 'L', 'q4')},
            'q6': {'Y': ('Y', 'R', 'q6'), 'Z': ('Z', 'R', 'q6'), 'W': ('W', 'R', 'q6'),
                   '_': ('_', 'R', 'accept')}
        }
    
    def run(self, input_string):
        self.tape = list(input_string + '_')
        self.head = 0
        self.state = 'q0'
        
        while self.state not in ['accept', 'reject']:
            current_symbol = self.tape[self.head] if self.head < len(self.tape) else '_'
            
            if current_symbol not in self.transitions[self.state]:
                self.state = 'reject'
                break
            
            write_symbol, move, new_state = self.transitions[self.state][current_symbol]
            
            if write_symbol is not None:
                if self.head < len(self.tape):
                    self.tape[self.head] = write_symbol
                else:
                    self.tape.append(write_symbol)
            
            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1
                if self.head < 0:
                    self.state = 'reject'
                    break
            
            self.state = new_state
        
        return self.state == 'accept'

tm = TuringMachine()
test_cases = [
    ("", True),
    ("0101", True),
    ("00110011", True),
    ("000111000111", True),
    ("01", False),
    ("0011", False),
    ("000111", False),
    ("010101", False)
]

for test in test_cases:
    result = tm.run(test[0])
    print(f"'{test[0]}': {result} (متوقع: {test[1]})")