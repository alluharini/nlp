from nltk.corpus import wordnet as wn

def get_word_meanings(word):
    synsets = wn.synsets(word)
    
    if not synsets:
        print(f"No meanings found for '{word}'")
    else:
        print(f"Meanings found for '{word}':")
        for synset in synsets:
            print(f"Synset: {synset.name()}")
            print(f"Definition: {synset.definition()}")
            print(f"Examples: {synset.examples()}")
            
            hypernyms = synset.hypernyms()
            if hypernyms:
                print(f"Hypernyms: {[hypernym.name().split('.')[0] for hypernym in hypernyms]}")
            
            hyponyms = synset.hyponyms()
            if hyponyms:
                print(f"Hyponyms: {[hyponym.name().split('.')[0] for hyponym in hyponyms]}")
            
            print()

# Example usage:
if __name__ == "__main__":
    word = "car"
    get_word_meanings(word)
