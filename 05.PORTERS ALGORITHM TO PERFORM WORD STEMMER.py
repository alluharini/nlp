import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def main():
    words = ["running", "jumps", "swimming", "eating", "happier", "running", "easily"]
    stemmed_words = stem_words(words)
    print("Original words:", words)
    print("Stemmed words:", stemmed_words)

if __name__ == "__main__":
    main()
