class PDA:
    def __init__(self):
        self.stack = []
    
    def accepts(self, input_string):
        self.stack = []
        length = len(input_string)
        
        if length % 2 == 0:
            return False
        
        middle = length // 2
       
        for i in range(middle):
            self.stack.append(input_string[i])
        
        for i in range(middle + 1, length):
            if not self.stack:
                return False
            if input_string[i] != self.stack.pop():
                return False
        
        return len(self.stack) == 0

pda = PDA()
test_cases = [
    ("a", True),
    ("aba", True),
    ("abba", False),
    ("abcba", True),
    ("abaa", False),
    ("madam", True),
    ("racecar", True),
    ("hello", False)
]

for test in test_cases:
    print(f"'{test[0]}': {pda.accepts(test[0])} (متوقع: {test[1]})")