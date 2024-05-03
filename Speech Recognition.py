import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said:", recognized_text)
except sr.UnknownValueError:
    print("Could not understand audio.")
