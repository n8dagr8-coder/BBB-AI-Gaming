import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 165)
engine.setProperty('volume', 1.0)

while True:
    text = input("AI Voice> ")

    if text.lower() == "exit":
        break

    engine.say(text)
    engine.runAndWait()
