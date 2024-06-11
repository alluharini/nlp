class MorphologicalParser:
    def __init__(self):
        self.transitions = {
            'S': {'s': 'Plural', 'x': 'Plural', 'z': 'Plural', 'ch': 'Plural', 'sh': 'Plural'},
            'Plural': {}
        }

    def generate_plural(self, noun):
        current_state = 'S'
        suffix = ''
        if noun.endswith('y') and len(noun) > 1 and noun[-2] not in 'aeiou':
            suffix = 'ies'
            noun = noun[:-1]
        elif noun[-1] in 'sxz' or noun[-2:] in ['ch', 'sh']:
            suffix = 'es'
        else:
            suffix = 's'

        return noun + suffix

def main():
    parser = MorphologicalParser()
    nouns = ['cat', 'dog', 'fox', 'watch', 'bus', 'box', 'dish', 'city', 'party']
    
    for noun in nouns:
        print(f"{noun}: {parser.generate_plural(noun)}")

if __name__ == "__main__":
    main()
