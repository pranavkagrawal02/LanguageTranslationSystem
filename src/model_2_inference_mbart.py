import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from models.mbart_translator import MBartTranslator

def main():
    print("mBART Translation System")
    print("1. English → Hindi")
    print("2. Hindi → English")

    choice = input("Select option (1/2): ").strip()

    if choice == "1":
        translator = MBartTranslator("en-hi")
    elif choice == "2":
        translator = MBartTranslator("hi-en")
    else:
        print("Invalid choice")
        return

    while True:
        text = input("\nEnter text (or exit): ")
        if text.lower() == "exit":
            break
        print("Translation:", translator.translate(text)[0])

if __name__ == "__main__":
    main()
