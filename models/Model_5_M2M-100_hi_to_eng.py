# --- Model 5: M2M-100 Hindi → English ---

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model_name = "facebook/m2m100_418M"

tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# Set source language to Hindi
tokenizer.src_lang = "hi"

def translate_m2m_hi_en(text):
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id("en")
    )
    return tokenizer.decode(generated[0], skip_special_tokens=True)

# Sample test
sample_text = "कृत्रिम बुद्धि दुनिया को बदल रही है।"
print("Input :", sample_text)
print("Output:", translate_m2m_hi_en(sample_text))
