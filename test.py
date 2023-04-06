import numpy as np
import speech_recognition as sr

# Build the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listing...")
            audio = recognizer.listen(mic)
        try:
            self.test = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me --> ERROR")

# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="HAL")
    while True:
        ai.speech_to_text()