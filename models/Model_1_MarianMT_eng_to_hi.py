# --- Model 1: MarianMT English → Hindi ---

from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-hi"

marian_tokenizer = MarianTokenizer.from_pretrained(model_name)
marian_model = MarianMTModel.from_pretrained(model_name)

def translate_marian(text):
    inputs = marian_tokenizer(text, return_tensors="pt", padding=True)
    outputs = marian_model.generate(**inputs)
    return marian_tokenizer.decode(outputs[0], skip_special_tokens=True)

# Sample test
sample_text = "Machine learning enables computers to learn from data."
print("Input :", sample_text)
print("Output:", translate_marian(sample_text))


