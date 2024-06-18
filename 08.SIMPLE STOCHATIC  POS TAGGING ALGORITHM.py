import random
def probabilistic_pos_tagging(words):
    pos_tags = ['NN', 'VB', 'JJ', 'RB'] 
    tagged_text = []
    for word in words:
        pos_tag = random.choice(pos_tags)
        tagged_text.append((word, pos_tag))
    return tagged_text

def main():
    text = "The quick brown fox jumps over the lazy dog"
    words = text.split()
    tagged_text = probabilistic_pos_tagging(words)
    print("Stochastic POS tagged text:")
    print(tagged_text)

if __name__ == "__main__":
    main()
