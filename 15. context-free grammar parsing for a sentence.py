import nltk
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    NP -> Det N [0.6] | NP PP [0.4]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'man' [0.5] | 'dog' [0.5]
    V -> 'saw' [1.0]
    P -> 'with' [1.0]
""")
parser = nltk.ViterbiParser(grammar)
sentence = "the man saw a dog "
parsed_trees = parser.parse(sentence.split())
for tree in parsed_trees:
    print(tree)
    print(f"Probability: {tree.prob()}")
    break 
