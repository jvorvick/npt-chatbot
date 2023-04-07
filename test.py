import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime

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
            self.text = self.text.replace("how", "HAL") if "how" in self.text else self.text 
            # self.text = self.text[:1].upper() + self.text[1:]
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
    
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime("%H:%M")

# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="HAL")
    while True:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello, I am HAL the AI, what can I do for you?"
        ## do any action
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(w in ai.text for w in ["thank", "thanks"]):
            res = np.random.choice(
                ["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "peace out!"])
        ai.text_to_speech(res)
