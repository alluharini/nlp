class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        chart = [[] for _ in range(len(input_string) + 1)]
        chart[0].append(('S\'', [], 0))  # Start with the initial state

        for i in range(len(input_string) + 1):
            while True:
                added = False
                for state in chart[i]:
                    non_terminal, production, dot_pos = state
                    if dot_pos < len(production) and production[dot_pos] in self.grammar:
                        self.predict(chart, i, production[dot_pos])
                    elif dot_pos == len(production):
                        self.complete(chart, i, non_terminal, state)
                    elif i < len(input_string) and input_string[i] == production[dot_pos]:
                        self.scan(chart, i, state)
                if not added:
                    break

        if ('S\'', ['S'], len(input_string)) in chart[len(input_string)]:
            print("String successfully parsed!")
        else:
            print("Parsing failed.")

    def predict(self, chart, i, non_terminal):
        for production in self.grammar[non_terminal]:
            chart[i].append((non_terminal, production, 0))

    def scan(self, chart, i, state):
        non_terminal, production, dot_pos = state
        chart[i + 1].append((non_terminal, production, dot_pos + 1))

    def complete(self, chart, i, non_terminal, state):
        for st in chart[state[2]]:
            nt, prod, dot_pos = st
            if dot_pos < len(prod) and prod[dot_pos] == non_terminal:
                chart[i].append((nt, prod, dot_pos + 1))


# Example usage:
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['man', 'woman', 'dog'],
    'V': ['saw', 'ate', 'walked']
}

earley_parser = EarleyParser(grammar)
input_string = "the man saw a dog"
earley_parser.parse(input_string.split())
