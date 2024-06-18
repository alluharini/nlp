from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
def translate_text(text):
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

english_text = "Hello, how are you?"
french_translation = translate_text(english_text)
print(f"English: {english_text}")
print(f"French: {french_translation}")