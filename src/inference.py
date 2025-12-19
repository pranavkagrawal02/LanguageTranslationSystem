from ..models.marian_translator import MarianTranslator


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
