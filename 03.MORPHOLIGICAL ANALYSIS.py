import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def perform_morphological_analysis(text):

    tokens = word_tokenize(text)
    print("Tokens:", tokens)

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in tokens]
    print("Stemmed words:", stemmed_words)


    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    print("Lemmatized words:", lemmatized_words)

def main():
    text = "The quick brown foxes are jumping over the lazy dogs"
    perform_morphological_analysis(text)

if __name__ == "__main__":
    main()
