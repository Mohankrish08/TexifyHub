import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.3)

        print('Speak now')

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('Speaker: ',text)

        except:
            pass
        