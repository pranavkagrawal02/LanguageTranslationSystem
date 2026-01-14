# --- Model 2 : MarianMT HI → EN (Reverse Direction) ---


from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-hi-en"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_hi_en(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Sample test
sample_text = "भारत एक विविध भाषाओं वाला देश है।"
print("Input :", sample_text)
print("Output:", translate_hi_en(sample_text))