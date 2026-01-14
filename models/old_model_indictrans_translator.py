from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class IndicTransTranslator:
    def __init__(self, direction="en-hi"):
        if direction == "en-hi":
            self.model_name = "ai4bharat/indictrans2-en-indic"
            self.src_lang = "eng_Latn"
            self.tgt_lang = "hin_Deva"
        elif direction == "hi-en":
            self.model_name = "ai4bharat/indictrans2-indic-en"
            self.src_lang = "hin_Deva"
            self.tgt_lang = "eng_Latn"
        else:
            raise ValueError("direction must be 'en-hi' or 'hi-en'")

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )

    def translate(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True
        )
        outputs = self.model.generate(**inputs, max_length=256)
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
