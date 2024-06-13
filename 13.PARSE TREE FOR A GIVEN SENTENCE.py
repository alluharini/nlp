class ParseTree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = "\t" * level + self.label + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

def generate_parse_tree(grammar, input_string):
    tokens = input_string.split()
    parse_table = [[None for _ in range(len(tokens) + 1)] for _ in range(len(tokens))]
    for i in range(len(tokens)):
        if tokens[i] in grammar:
            parse_table[i][i + 1] = [(grammar[tokens[i]], tokens[i])]
    for span in range(2, len(tokens) + 1):
        for start in range(len(tokens) - span + 1):
            end = start + span
            for mid in range(start + 1, end):
                for rule in grammar:
                    if len(grammar[rule]) == 2:
                        left, right = grammar[rule]
                        if parse_table[start][mid] and parse_table[mid][end]:
                            for ltree in parse_table[start][mid]:
                                for rtree in parse_table[mid][end]:
                                    if ltree[0] == left and rtree[0] == right:
                                        parse_table[start][end] = [(rule, ltree[1], rtree[1])]
    return ParseTree('S', build_tree(parse_table, 0, len(tokens)))

def build_tree(parse_table, start, end):
    if parse_table[start][end]:
        return [ParseTree(rule[0], [ParseTree(symbol) for symbol in rule[1:]]) for rule in parse_table[start][end]]
    else:
        return [ParseTree('')]

# Example usage:
grammar = {
    'S': [('NP', 'VP')],
    'NP': [('Det', 'N')],
    'VP': [('V', 'NP')],
    'Det': ['the', 'a'],
    'N': ['man', 'woman', 'dog'],
    'V': ['saw', 'ate', 'walked']
}

input_string = "the man saw a dog"
parse_tree = generate_parse_tree(grammar, input_string)
print(parse_tree)
