# --- Model 3: M2M-100 English → Hindi ---

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model_name = "facebook/m2m100_418M"

tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

tokenizer.src_lang = "en"

def translate_m2m(text):
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("hi")
    )
    return tokenizer.decode(generated[0], skip_special_tokens=True)


sample_text = "Artificial intelligence is changing the world."
print("Input :", sample_text)
print("Output:", translate_m2m(sample_text))
# --- Model 3: M2M-100 English → Hindi ---

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model_name = "facebook/m2m100_418M"

tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

tokenizer.src_lang = "en"

def translate_m2m(text):
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("hi")
    )
    return tokenizer.decode(generated[0], skip_special_tokens=True)


sample_text = "Artificial intelligence is changing the world."
print("Input :", sample_text)
print("Output:", translate_m2m(sample_text))
