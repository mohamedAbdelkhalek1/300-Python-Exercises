"""
complex_assignment_21:

Write A Python Program To Make A English Dictionary App That Translate Into Arabic

"""
from translate import Translator

def translate_english_to_arabic(word):
    translator = Translator(to_lang="arabic")
    translation = translator.translate(word)
    return translation

# Get user input
word = input("Enter an English word to translate to Arabic: ")

# Translate the word
translated_word = translate_english_to_arabic(word)

# Print the translated word
print("Translated word:", translated_word)