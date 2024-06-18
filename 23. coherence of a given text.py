import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def evaluate_coherence(text):
    inputs = tokenizer.encode(text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(inputs, labels=inputs)
        loss = outputs.loss
    perplexity = torch.exp(loss).item()
    return perplexity
text = "Once upon a time in a land far, far away, there lived a wise old king who ruled with kindness and wisdom."
coherence_score = evaluate_coherence(text)
print(f"Text: {text}")
print(f"Coherence Score (Perplexity): {coherence_score}")