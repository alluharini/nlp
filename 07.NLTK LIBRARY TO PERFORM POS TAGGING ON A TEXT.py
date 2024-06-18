import nltk
from nltk import word_tokenize, pos_tag
text = "harini is a good girl."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("POS Tagged Text:")
print(pos_tags)
