class FiniteStateAutomaton:
    def __init__(self):
        self.start_state = 'q0'
        self.accept_state = 'q2'
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q0'},
        }
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def process_input(self, input_string):
        self.reset()
        for char in input_string:
            if char in self.alphabet:
                self.current_state = self.transitions[self.current_state][char]
        return self.current_state == self.accept_state

fsa = FiniteStateAutomaton()
test_strings = ["a", "ab", "baba", "aab", "xyzab"]

for s in test_strings:
    result = fsa.process_input(s)
    if result:
        print(f"{s} is accepted")
    else:
        print(f"{s} is not accepted")
