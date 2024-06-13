class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar

    def check_agreement(self, sentence):
        tokens = sentence.split()
        for token in tokens:
            if token in self.grammar:
                for rule in self.grammar[token]:
                    if all(term in tokens for term in rule):
                        return True
        return False

# Example usage:
grammar = {
    'NP': [['the', 'N'], ['a', 'N'], ['the', 'Adjective', 'N']],
    'N': ['man', 'woman', 'dog'],
    'Adjective': ['tall', 'short'],
    'VP': [['V'], ['V', 'NP']],
    'V': ['runs', 'walks', 'eats']
}

agreement_checker = AgreementChecker(grammar)
sentence1 = "the man runs"
sentence2 = "a tall woman walks"
sentence3 = "the dog eats"

print("Sentence 1 agreement:", agreement_checker.check_agreement(sentence1))
print("Sentence 2 agreement:", agreement_checker.check_agreement(sentence2))
print("Sentence 3 agreement:", agreement_checker.check_agreement(sentence3))
