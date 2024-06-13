import random

class PCFGParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, sentence):
        tokens = sentence.split()
        parse_tree = self.parse_recursively(tokens, 'S')
        if parse_tree:
            return parse_tree
        else:
            return "Parsing failed"

    def parse_recursively(self, tokens, symbol):
        if symbol in self.grammar:
            productions = self.grammar[symbol]
            random.shuffle(productions)  # Shuffle to select productions randomly
            for production in productions:
                subtree = []
                success = True
                for token in production:
                    if token in self.grammar:
                        sub_tree = self.parse_recursively(tokens, token)
                        if sub_tree == "Parsing failed":
                            success = False
                            break
                        else:
                            subtree.append(sub_tree)
                    elif tokens and token == tokens[0]:
                        subtree.append(tokens.pop(0))
                    else:
                        success = False
                        break
                if success:
                    return [symbol] + subtree
        return "Parsing failed"


# Example usage:
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N'], ['N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['man', 'woman', 'dog'],
    'V': ['saw', 'ate', 'walked']
}

pcfg_parser = PCFGParser(grammar)
sentence = "the man saw a dog"
parse_tree = pcfg_parser.parse(sentence)
print(parse_tree)
