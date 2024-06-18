import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_name = "j-hartmann/emotion-english-distilroberta-base"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
def recognize_dialog_act(dialog):
    inputs = tokenizer(dialog, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
    labels = model.config.id2label
    return labels[predicted_class_id]
dialogs = [
    "Hello, how can I help you today?",
    "Can you tell me more about your services?",
    "Thank you very much for your assistance.",
    "I'm sorry, I don't understand your question.",
]
for dialog in dialogs:
    dialog_act = recognize_dialog_act(dialog)
    print(f"Dialog: {dialog}")
    print(f"Recognized Dialog Act: {dialog_act}\n")