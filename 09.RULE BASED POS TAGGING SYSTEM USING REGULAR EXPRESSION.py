import re

def pos_tag(sentence):
    tagged_words = []
    patterns = [
        (r'\b(?:the|a|an)\b', 'DET'),               
        (r'\b(?:is|am|are|was|were)\b', 'VERB'),     
        (r'\b(?:\w+ed|ing)\b', 'VERB'),              
        (r'\b(?:\w+ly)\b', 'ADV'),                   
        (r'\b(?:\w+est)\b', 'ADJ'),                  
        (r'\b(?:\w+\'s)\b', 'NOUN'),                 
        (r'\b(?:\w+s)\b', 'NOUN'),
        
        (r'\b(?:\w+)\b', 'NOUN')                    
    ]

    
    for word in sentence.split():
        for pattern, pos_tag in patterns:
            if re.match(pattern, word):
                tagged_words.append((word, pos_tag))
                break
        else:
            tagged_words.append((word, 'UNK'))  

    return tagged_words


sentence = "The quick brown fox jumps over the lazy dog"
tagged_sentence = pos_tag(sentence)
print(tagged_sentence)
