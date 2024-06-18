import re
text = "The quick brown fox jumps over the lazy dog."
pattern = r'\b[b|f]\w+'
matches = re.findall(pattern, text)
print("Matches found:")
for match in matches:
    print(match)
