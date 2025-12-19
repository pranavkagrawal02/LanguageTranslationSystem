from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

class MBartTranslator:
    def __init__(self, direction="en-hi"):
        self.model_name = "facebook/mbart-large-50-many-to-many-mmt"
        self.tokenizer = MBart50TokenizerFast.from_pretrained(self.model_name)
        self.model = MBartForConditionalGeneration.from_pretrained(self.model_name)

        if direction == "en-hi":
            self.src_lang = "en_XX"
            self.tgt_lang = "hi_IN"
        elif direction == "hi-en":
            self.src_lang = "hi_IN"
            self.tgt_lang = "en_XX"
        else:
            raise ValueError("direction must be 'en-hi' or 'hi-en'")

        self.tokenizer.src_lang = self.src_lang

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        generated = self.model.generate(
            **inputs,
            forced_bos_token_id=self.tokenizer.lang_code_to_id[self.tgt_lang]
        )
        return self.tokenizer.batch_decode(generated, skip_special_tokens=True)
