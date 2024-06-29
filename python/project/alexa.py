import whisper
import pyaudio
import wave
import asyncio
import random
import edge_tts
import datetime
from edge_tts import VoicesManager
import numpy as np
from playsound import playsound
from fuzzywuzzy import fuzz
class VoiceAssistant:
    def __init__(self, model_size="medium", threshold=2500, silence_limit=1.5):
        self.model = whisper.load_model(model_size)
        self.THRESHOLD = threshold
        self.SILENCE_LIMIT = silence_limit
        #self.audio = pyaudio.PyAudio()

    def is_silent(self, data):
        return max(data) < self.THRESHOLD

    def listen(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

        print("Please speak:")

        frames = []
        silent_chunks = 0
        silence_threshold = int(self.SILENCE_LIMIT * 16000 / 1024)

        while True:
            data = np.frombuffer(stream.read(1024), dtype=np.int16)
            frames.append(data.tobytes())
            if self.is_silent(data):
                silent_chunks += 1
            else:
                silent_chunks = 0
            if silent_chunks > silence_threshold:
                break

        stream.stop_stream()
        stream.close()
        audio.terminate()

        wave_file = wave.open("audio.wav", "wb")
        wave_file.setnchannels(1)
        wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(16000)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

        result = self.model.transcribe("audio.wav")
        with open("result.txt", "w") as result_file:
            result_file.write(result["text"])
        print(result["text"])

    async def speak(self, text):
        OUTPUT_FILE = "response.mp3"
        voices = await VoicesManager.create()
        voice = voices.find(Gender="Female", Locale="ar-EG")
        communicate = edge_tts.Communicate(text, random.choice(voice)["Name"])
        await communicate.save(OUTPUT_FILE)
        playsound(OUTPUT_FILE)


def fuzzy_search(text, phrases):
    best_match = max(phrases, key=lambda phrase: fuzz.ratio(text, phrase))
    return best_match


if __name__ == "__main__":
    assistant = VoiceAssistant()
    asyncio.run(assistant.speak("اهلا انا اليكسا ازاي اقدر اساعدك النهاردة"))
    assistant.listen()
    with open("result.txt", "r") as f:
        text = f.read()
    # asyncio.run(assistant.speak("كله تمام يا كبير"))
    # assistant.listen()
    # asyncio.run(assistant.speak("يا عم غور من وشي "))
commands = ["الوقت ايه", "الساعة دلوقتي كام", "الساعة كام"]
best_match = fuzzy_search(text, commands)

if best_match in commands:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    asyncio.run(assistant.speak("الوقت الآن هو " + current_time))
else:
    asyncio.run(assistant.speak("عذراً، لا أستطيع مساعدتك في ذلك."))

