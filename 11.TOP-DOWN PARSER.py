class CFG:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        self.current_token = self.input_string[self.index]
        if self.parse_symbol(self.grammar['start']):
            if self.index == len(self.input_string):
                print("String successfully parsed!")
            else:
                print("Parsing failed. Unexpected tokens remaining.")
        else:
            print("Parsing failed. Invalid string.")

    def parse_symbol(self, symbol):
        if symbol in self.grammar['terminals']:
            if self.current_token == symbol:
                self.index += 1
                if self.index < len(self.input_string):
                    self.current_token = self.input_string[self.index]
                return True
            else:
                return False
        else:
            for production in self.grammar['productions'][symbol]:
                if all(self.parse_symbol(s) for s in production):
                    return True
            return False


grammar = {
    'start': 'S',
    'terminals': {'a', 'b'},
    'productions': {
        'S': [['a', 'S', 'b'], ['a', 'b']]
    }
}

cfg = CFG(grammar)
input_string = "ABABA"
cfg.parse(input_string)
