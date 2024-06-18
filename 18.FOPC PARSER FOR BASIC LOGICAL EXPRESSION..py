class FOPCParser:
    def __init__(self):
        self.variables = set()
        self.constants = set()
        self.predicates = set()

    def parse(self, expression):
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token == '(':
                stack.append(token)
            elif token == ')':
                args = []
                while stack[-1] != '(':
                    args.append(stack.pop())
                stack.pop()  # Remove the '('
                predicate = stack.pop()
                self.predicates.add(predicate)
                stack.append((predicate, args))
            elif token.islower():
                self.variables.add(token)
                stack.append(token)
            else:
                self.constants.add(token)
                stack.append(token)
        return stack[0]

# Example usage:
parser = FOPCParser()
expression = "(P x y) & (Q a b)"
parsed_expression = parser.parse(expression)
print("Variables:", parser.variables)
print("Constants:", parser.constants)
print("Predicates:", parser.predicates)
print("Parsed expression:", parsed_expression)
