from nltk.corpus import wordnet

def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    
    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f"Synset: {synset.name()}")
            print(f"Definition: {synset.definition()}")
            print(f"Examples: {synset.examples()}")
            print()

        hypernyms = synsets[0].hypernyms()
        if hypernyms:
            print(f"Hypernyms of '{word}':")
            for hypernym in hypernyms:
                print(f"{hypernym.name()}: {hypernym.definition()}")
            print()

        hyponyms = synsets[0].hyponyms()
        if hyponyms:
            print(f"Hyponyms of '{word}':")
            for hyponym in hyponyms:
                print(f"{hyponym.name()}: {hyponym.definition()}")
            print()
    else:
        print(f"No synsets found for '{word}'.")

# Example usage:
word = "dog"
explore_word_meanings(word)
