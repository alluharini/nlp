import re

def main():
    # Sample text
    text = "The quick brown fox jumps over the lazy dog. 123-456-7890"

    # Define a regular expression pattern
    pattern = r'fox'

    # Using re.match() to find the pattern at the beginning of the text
    match = re.match(pattern, text)
    if match:
        print("Match found at the beginning of the text:", match.group())
    else:
        print("No match found at the beginning of the text.")

    # Using re.search() to find the pattern anywhere in the text
    search = re.search(pattern, text)
    if search:
        print("Pattern found anywhere in the text:", search.group())
    else:
        print("Pattern not found anywhere in the text.")

    # Using re.findall() to find all occurrences of the pattern in the text
    all_occurrences = re.findall(pattern, text)
    if all_occurrences:
        print("All occurrences of the pattern:", all_occurrences)
    else:
        print("Pattern not found anywhere in the text.")

    # Using re.sub() to replace occurrences of the pattern in the text
    replacement_text = re.sub(pattern, "cat", text)
    print("Text after replacement:", replacement_text)

if __name__ == "__main__":
    main()
