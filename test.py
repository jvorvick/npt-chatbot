# for speech-to-text
import speech_recognition as sr
# for text-to-speech
from gtts import gTTS
# for language model
import transformers
# for data
import datetime
import time
import numpy as np
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
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            # self.text = self.text.replace("how", "HAL") if "how" in self.text else self.text 
            # self.text = self.text[:1].upper() + self.text[1:]
            print("me --> ", self.text)
        except:
            print("me --> ERROR")

    @staticmethod
    def text_to_speech(text):
        print("Dev --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        statbuf = os.stat("res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200

        #mac
        os.system("afplay res.mp3")
        #windows
        # os.system("start res.mp3")

        time.sleep(int(50 * duration))
        os.remove("res.mp3")
    
    def wake_up(self, text):
        return True if self.name in text else False
    
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime("%H:%M")

# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="Dev")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex = True
    while ex:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello, I am Dev the AI, what can I do for you?"
        ## do any action
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(w in ai.text for w in ["thank", "thanks"]):
            res = np.random.choice(
                ["you're welcome!", "anytime!", "no problem!", "of course!", "I'm here if you need me!", "don't mention it!"])
        elif any(w in ai.text for w in ["exit", "close"]):
            res = np.random.choice(["See you later!", "Have a good day!", "Bye!", "Goodbye!", "Hope to meet again soon!", "Until next time!"])
            ex = False
        ## conversation
        else:
            if ai.text == "ERROR":
                res = "Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res=str(chat)
                res=res[res.find("bot >> ")+6:].strip()
        ai.text_to_speech(res)
    print("----- Closing down Dev -----")
