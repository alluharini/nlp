import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Extract named entities and their labels
    named_entities = [(entity.text, entity.label_) for entity in doc.ents]
    
    return named_entities

# Example text
text = "Apple is looking at buying U.K. startup for $1 billion"

# Perform Named Entity Recognition
ner_results = perform_ner(text)

# Print the named entities and their labels
for entity, label in ner_results:
    print(f"Entity: {entity}, Label: {label}")
