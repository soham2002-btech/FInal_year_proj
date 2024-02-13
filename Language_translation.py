from googletrans import Translator

def translate_to_hindi(text):
    # Initialize translator
    translator = Translator()

    # Translate text to Hindi
    translated_text = translator.translate(text, dest='hi')

    return translated_text.text

def translate_to_german(text):
    # Initialize translator
    translator = Translator()

    # Translate text to Hindi
    translated_text = translator.translate(text, dest='de')

    return translated_text.text

def translate_to_french(text):
    # Initialize translator
    translator = Translator()

    # Translate text to Hindi
    translated_text = translator.translate(text, dest='fr')

    return translated_text.text

# Example usage:
english_text = "Hello, how are you?"
translated_text = translate_to_hindi(english_text)
print("Translated text (Hindi):", translated_text)
