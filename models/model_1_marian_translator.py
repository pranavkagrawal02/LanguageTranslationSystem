from transformers import MarianMTModel, MarianTokenizer

class MarianTranslator:
    def __init__(self, direction="en-hi"):
        if direction == "en-hi":
            model_name = "Helsinki-NLP/opus-mt-en-hi"
        elif direction == "hi-en":
            model_name = "Helsinki-NLP/opus-mt-hi-en"
        else:
            raise ValueError("direction must be 'en-hi' or 'hi-en'")

        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        if isinstance(text, str):
            text = [text]

        tokens = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        translated = self.model.generate(**tokens)
        return self.tokenizer.batch_decode(
            translated,
            skip_special_tokens=True
        )


"""
I’ll explain this **cleanly, line-by-line**, and then give you a **high-level summary** you can use in exams / viva / interviews.

---

# 🔹 1. Importing MarianMT components

```python
from transformers import MarianMTModel, MarianTokenizer
```

### What this does:

* Imports **pretrained Neural Machine Translation (NMT)** tools from Hugging Face
* `MarianMTModel` → the **actual translation neural network**
* `MarianTokenizer` → converts human language text into **numerical tokens** the model understands

These come from **Marian**, a well-known NMT framework.

---

# 🔹 2. Defining the `MarianTranslator` class

```python
class MarianTranslator:
```

This class is a **wrapper** around the Marian translation model.
It hides complexity and provides a **simple `translate()` function**.

---

# 🔹 3. Constructor (`__init__`) – Model selection logic

```python
def __init__(self, direction="en-hi"):
```

* Runs when an object is created
* `direction` tells which translation direction to use

---

## 🔹 Choosing the pretrained model

```python
if direction == "en-hi":
    model_name = "Helsinki-NLP/opus-mt-en-hi"
elif direction == "hi-en":
    model_name = "Helsinki-NLP/opus-mt-hi-en"
```

### What this does:

* Selects a **language-pair-specific pretrained model**
* These models are trained on **large bilingual corpora**
* No training required from your side

---

## 🔹 Error handling

```python
else:
    raise ValueError("direction must be 'en-hi' or 'hi-en'")
```

Prevents invalid input and ensures **safe usage**.

---

# 🔹 4. Loading tokenizer and model

```python
self.tokenizer = MarianTokenizer.from_pretrained(model_name)
self.model = MarianMTModel.from_pretrained(model_name)
```

### What happens here:

* Downloads model (first run only)
* Loads:

  * Vocabulary
  * Tokenization rules
  * Neural network weights

These are stored locally after download.

---

# 🔹 5. `translate()` method – Core logic

```python
def translate(self, text):
```

This function **takes text and returns translated text**.

---

## 🔹 Handling single or multiple sentences

```python
if isinstance(text, str):
    text = [text]
```

* Converts a single string into a list
* Makes the function compatible with **batch translation**

---

## 🔹 Tokenization step

```python
tokens = self.tokenizer(
    text,
    return_tensors="pt",
    padding=True,
    truncation=True
)
```

### What this does:

* Converts text → token IDs
* Pads sentences to same length
* Truncates long inputs
* Returns **PyTorch tensors**

---

# 🔹 6. Generating translation

```python
translated = self.model.generate(**tokens)
```

### Internally:

* Encoder processes source language
* Decoder generates target language tokens
* Uses beam search (by default)

This is **actual neural translation happening**.

---

# 🔹 7. Decoding tokens back to text

```python
return self.tokenizer.batch_decode(
    translated,
    skip_special_tokens=True
)
```

### Converts:

```
token IDs → human-readable translated sentences
```

* Removes `<pad>`, `<eos>`, etc.
* Returns a **list of translated strings**

---

# ✅ HIGH-LEVEL SUMMARY (VERY IMPORTANT)

> This class provides a simple interface for performing neural machine translation using pretrained MarianMT models. It dynamically selects the correct translation model based on language direction, tokenizes input text into numerical representations, uses a transformer-based encoder-decoder architecture to generate translations, and decodes the output back into readable language.

---

# 🧠 ONE-LINE INTERVIEW ANSWER

> “This code wraps a pretrained MarianMT transformer model to perform English–Hindi or Hindi–English translation by tokenizing input text, generating translations using a neural encoder-decoder, and decoding the output back into natural language.”

---

# 📌 WHY THIS CODE IS GOOD FOR YOUR PROJECT

✔ No training needed initially
✔ Production-grade translation quality
✔ Simple interface (`translate(text)`)
✔ Easily extensible for fine-tuning

---
"""