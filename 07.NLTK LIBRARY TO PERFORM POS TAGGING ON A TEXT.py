import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    return tagged_tokens

def main():
    text = "The quick brown fox jumps over the lazy dog"
    tagged_text = pos_tagging(text)
    print("POS tagged text:")
    print(tagged_text)

if __name__ == "__main__":
    main()
