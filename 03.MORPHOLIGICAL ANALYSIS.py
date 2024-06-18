import nltk
from nltk.corpus import wordnet as wn
word = "running"
stemmer = nltk.LancasterStemmer()
stemmed_word = stemmer.stem(word)
pos_tags = nltk.pos_tag([word])
synsets = wn.synsets(word)

print(f"Word: {word}")
print(f"Stemmed word: {stemmed_word}")
print(f"Part-of-speech tags: {pos_tags}")
print(f"Synsets: {synsets}")
