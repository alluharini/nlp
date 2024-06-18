import openai
def generate_text(prompt, max_tokens=100):
    openai.api_key = "your-api-key-here"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

prompt = "Once upon a time in a land far, far away,"
generated_text = generate_text(prompt)
print(f"Prompt: {prompt}")
print(f"Generated Text: {generated_text}")