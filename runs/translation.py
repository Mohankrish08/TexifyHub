from googletrans import Translator

words = input('Enter the words: ')

target_lang = print("Select target language", ["English (en)", "Tamil (ta)", "French (fr)", "Spanish (es)", "German (de)", "Japanese (ja)"])  # You can add more languages

    # Translator
translator = Translator()


words = trans

if translator:
    translation = translator.translate(words, dest=target_lang)
    print("Original Text:", trans)
    print("Translation:", translation.text)