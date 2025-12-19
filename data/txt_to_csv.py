# preprocessing/txt_to_csv.py

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")

EN_FILE = "IITB.en-hi.en"
HI_FILE = "IITB.en-hi.hi"
OUTPUT_FILE = "parallel_en_hi.csv"

def main():
    en_path = os.path.join(RAW_DATA_PATH, EN_FILE)
    hi_path = os.path.join(RAW_DATA_PATH, HI_FILE)

    if not os.path.exists(en_path) or not os.path.exists(hi_path):
        raise FileNotFoundError("English or Hindi source file missing")

    with open(en_path, "r", encoding="utf-8") as f:
        en_lines = f.readlines()

    with open(hi_path, "r", encoding="utf-8") as f:
        hi_lines = f.readlines()

    if len(en_lines) != len(hi_lines):
        raise ValueError("Line count mismatch between EN and HI files")

    data = []
    for en, hi in zip(en_lines, hi_lines):
        en = en.strip()
        hi = hi.strip()
        if en and hi:
            data.append({"english": en, "hindi": hi})

    df = pd.DataFrame(data)
    output_path = os.path.join(RAW_DATA_PATH, OUTPUT_FILE)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"[✓] CSV created at: {output_path}")
    print(f"[✓] Total sentence pairs: {len(df)}")

if __name__ == "__main__":
    main()
