import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

# Build the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            self.text = "how" in self.text and self.text.replace("how", "HAL")
            print("me --> ", self.text)
        except:
            print("me --> ERROR")
    
    def wake_up(self, text):
        return True if self.name in text else False

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")

        #mac
        os.system("afplay res.mp3")
        #windows
        # os.system("start res.mp3")

        os.remove("res.mp3")

# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="HAL")
    while True:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "I'm afraid I can't do that, Jesse."
        ai.text_to_speech(res)