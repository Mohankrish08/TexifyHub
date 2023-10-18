import pyttsx3
text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)


text = input("Enter the prompt: ")

voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[1].id)

text_to_speech.say(text)

text_to_speech.save_to_file(text, 'test.mp3')

text_to_speech.runAndWait()