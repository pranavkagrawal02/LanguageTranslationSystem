import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from models.old_model_marian_translator import MarianTranslator


def main():
    print("Language Translation System")
    print("1. English → Hindi")
    print("2. Hindi → English")

    choice = input("Select option (1/2): ").strip()

    if choice == "1":
        translator = MarianTranslator(direction="en-hi")
    elif choice == "2":
        translator = MarianTranslator(direction="hi-en")
    else:
        print("Invalid choice")
        return

    while True:
        text = input("\nEnter text (or type 'exit'): ")
        if text.lower() == "exit":
            break

        output = translator.translate(text)
        print("Translation:", output[0])


if __name__ == "__main__":
    main()


""" 
Yes — I’ll explain this **line-by-line**, **clearly**, and in **plain engineering terms**, so you can also explain it confidently in an interview or viva.

---

# 🔹 1. Importing system and OS utilities

```python
import sys
import os
```

### What this does:

* `os` → lets Python work with **file paths**, directories, and OS-level info
* `sys` → lets Python interact with the **Python runtime itself** (like module search paths)

You need these to **control how Python finds your project files**.

---

# 🔹 2. Adding the project root to PYTHONPATH

```python
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
```

### Step-by-step explanation:

#### 🔸 `__file__`

* Refers to the **current file** (`inference.py`)
* Example:

  ```
  C:\LanguageTranslationSystem\src\inference.py
  ```

#### 🔸 `os.path.dirname(__file__)`

* Gives the folder containing the file:

  ```
  C:\LanguageTranslationSystem\src
  ```

#### 🔸 `os.path.join(..., "..")`

* Moves **one level up**:

  ```
  C:\LanguageTranslationSystem
  ```

#### 🔸 `os.path.abspath(...)`

* Converts it into a **full absolute path**

So finally:

```python
PROJECT_ROOT = "C:\\LanguageTranslationSystem"
```

---

### 🔹 `sys.path.insert(0, PROJECT_ROOT)`

Python searches for imports in a list called `sys.path`.

This line:

* Adds the **project root** at the **highest priority**
* So Python can now find:

  ```
  models/
  preprocessing/
  src/
  ```

👉 **Without this**, Python would not find `models.marian_translator`.

---

# 🔹 3. Importing your translation model

```python
from models.marian_translator import MarianTranslator
```

### What this does:

* Imports your **custom wrapper class** around MarianMT
* This class internally loads:

  * Tokenizer
  * Pretrained translation model

This is the **core translation engine** of your project.

---

# 🔹 4. `main()` function — CLI Interface

```python
def main():
```

Defines the main entry point of your application.

---

## 🔹 5. Printing menu options

```python
print("Language Translation System")
print("1. English → Hindi")
print("2. Hindi → English")
```

Simple **command-line UI** so the user can choose translation direction.

---

## 🔹 6. Taking user input

```python
choice = input("Select option (1/2): ").strip()
```

* Takes user input
* `.strip()` removes extra spaces
* Ensures clean comparison

---

## 🔹 7. Creating the translator object

```python
if choice == "1":
    translator = MarianTranslator(direction="en-hi")
elif choice == "2":
    translator = MarianTranslator(direction="hi-en")
```

### What happens internally:

* Loads **pretrained MarianMT model**
* Chooses model:

  * `opus-mt-en-hi` or
  * `opus-mt-hi-en`

This is **dynamic model selection**.

---

## 🔹 8. Continuous translation loop

```python
while True:
```

Keeps the program running until the user exits.

---

### Taking text input

```python
text = input("\nEnter text (or type 'exit'): ")s
```

---

### Exit condition

```python
if text.lower() == "exit":
    break
```

Allows clean termination of the program.

---

### Translating text

```python
output = translator.translate(text)
print("Translation:", output[0])
```

What happens:

* Input text → tokenizer
* Tokens → MarianMT model
* Generated tokens → decoded text
* Output is a list → we print first element

---

# 🔹 9. Script entry-point guard

```python
if __name__ == "__main__":
    main()
```

### Why this is important:

* Ensures `main()` runs **only when the file is executed directly**
* Prevents accidental execution when imported as a module

This is **standard Python best practice**.

---

# ✅ HIGH-LEVEL SUMMARY (ONE PARAGRAPH)

> This script is a command-line interface for a language translation system. It dynamically loads a pretrained MarianMT model for English–Hindi or Hindi–English translation based on user input. The script ensures proper module resolution by explicitly adding the project root to Python’s import path, allowing clean separation between model logic and inference logic. The system continuously accepts user input, translates it using a pretrained neural machine translation model, and displays the translated output until the user exits.

---

# 🧠 INTERVIEW-READY ONE-LINE EXPLANATION

> “This script acts as the inference layer of my translation system. It sets up the project import path, loads a pretrained MarianMT model dynamically based on user choice, and provides a command-line interface for real-time English–Hindi and Hindi–English translation.”

---


"""