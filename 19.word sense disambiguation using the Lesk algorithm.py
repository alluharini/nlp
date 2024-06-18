from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(word, sentence):
    word_tokens = set(word_tokenize(sentence.lower()))
    context = word_tokens.difference(set(stopwords.words('english')))
    best_sense, max_overlap = None, 0
    
    for sense in wn.synsets(word):
        signature = set(word_tokenize(sense.definition().lower()))
        signature.update([word_tokenize(example.lower()) for example in sense.examples()])
        signature = signature.difference(set(stopwords.words('english')))
        
        overlap = len(context.intersection(signature))
        if overlap > max_overlap:
            max_overlap, best_sense = overlap, sense
    
    return best_sense

# Example usage
word, sentence = "bank", "He went to the bank to deposit his money."
sense = lesk_algorithm(word, sentence)

if sense:
    print(f"Word: {word}")
    print(f"Best Sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print(f"No suitable sense found for '{word}' in the context of '{sentence}'")
