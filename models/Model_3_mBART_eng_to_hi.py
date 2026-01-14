# --- Model 3: mBART English → Hindi (SAFE VERSION) ---

from transformers import MBartForConditionalGeneration, MBart50Tokenizer

mbart_model_name = "facebook/mbart-large-50-many-to-many-mmt"

mbart_tokenizer = MBart50Tokenizer.from_pretrained(mbart_model_name)
mbart_model = MBartForConditionalGeneration.from_pretrained(mbart_model_name)

mbart_tokenizer.src_lang = "en_XX"

def translate_mbart(text):
    encoded = mbart_tokenizer(text, return_tensors="pt")
    generated = mbart_model.generate(
        **encoded,
        forced_bos_token_id=mbart_tokenizer.lang_code_to_id["hi_IN"]
    )
    return mbart_tokenizer.decode(generated[0], skip_special_tokens=True)

# Test
sample_text = "Artificial intelligence is changing the world."
print("Input :", sample_text)
print("Output:", translate_mbart(sample_text))
