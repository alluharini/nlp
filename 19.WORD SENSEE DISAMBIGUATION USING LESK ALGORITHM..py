from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def lesk(word, sentence):
    best_sense = None
    max_overlap = 0
    word = word.lower()
    sentence = set(word_tokenize(sentence.lower()))
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    for sense in wordnet.synsets(word):
        definition = set(word_tokenize(sense.definition().lower()))
        examples = set(word_tokenize(" ".join(sense.examples()).lower()))
        signature = definition.union(examples)
        signature = signature.difference(stop_words)
        signature = signature.difference(punctuation)

        overlap = len(signature.intersection(sentence))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage:
word = "bank"
sentence = "I went to the bank to deposit my money."

sense = lesk(word, sentence)
if sense:
    print(f"The most appropriate sense of '{word}' in the context of the sentence:")
    print(f"'{sentence}'")
    print(f"is:")
    print(f"{sense.name()}: {sense.definition()}")
else:
    print(f"No sense found for '{word}'")
