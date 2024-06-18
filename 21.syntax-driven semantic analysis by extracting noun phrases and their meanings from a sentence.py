import nltk
from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize
def extract_noun_phrases(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    grammar = r"""
        NP: {<DT>?<JJ>*<NN>}  
            {<NNP>+}          
    """
    parser = RegexpParser(grammar)
    parsed_sentence = parser.parse(tagged_words)
    noun_phrases = []
    for subtree in parsed_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
        words_in_subtree = [word for word, tag in subtree.leaves()]
        noun_phrase = " ".join(words_in_subtree)
        noun_phrases.append(noun_phrase)
    return noun_phrases
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = extract_noun_phrases(sentence)
print(f"Original Sentence: {sentence}")
print("Extracted Noun Phrases:")
for np in noun_phrases:
    print(np)
