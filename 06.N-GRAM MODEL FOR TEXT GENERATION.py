import random

def create_bigram_model(text):
    words = text.split()
    bigrams = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in bigrams:
            bigrams[current_word] = []
        bigrams[current_word].append(next_word)
    return bigrams

def generate_text(bigrams, num_words=50):
    current_word = random.choice(list(bigrams.keys()))
    generated_text = [current_word]
    for _ in range(num_words - 1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(generated_text)

def main():
    text = "The quick brown fox jumps over the lazy dog"
    bigram_model = create_bigram_model(text)
    generated_text = generate_text(bigram_model)
    print("Generated text:")
    print(generated_text)

if __name__ == "__main__":
    main()
