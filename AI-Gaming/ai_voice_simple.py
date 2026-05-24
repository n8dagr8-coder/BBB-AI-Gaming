import os

while True:
    text = input("AI Voice> ")

    if text.lower() == "exit":
        break

    os.system(f'espeak "{text}"')
