import asyncio
import pyttsx3
import speech_recognition as sr

from datetime import datetime

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    async def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

    def fuzzy_search(self, text, phrases):
        best_match = max(phrases, key=lambda phrase: fuzz.ratio(text, phrase))
        return best_match

    async def tell_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await self.speak(f"الوقت الآن هو {current_time}")

    async def run(self):
        await self.speak("اهلا انا اليكسا ازاي اقدر اساعدك النهاردة")
        user_input = self.listen()

        if not user_input:
            await self.speak("لم أفهم ما قلته. من فضلك حاول مرة أخرى.")
            return

        commands = ["كم الساعة", "ما هو الوقت", "أخبرني بالوقت"]
        best_match = self.fuzzy_search(user_input, commands)

        if best_match in commands:
            await self.tell_time()
        else:
            await self.speak("عذراً، لا أستطيع مساعدتك في ذلك.")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    asyncio.run(assistant.run())
