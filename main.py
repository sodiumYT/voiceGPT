import speech_recognition as sr
import time, os
from g4f.client import Client
from colorama import Fore

client = Client()
r = sr.Recognizer()
mic = sr.Microphone()

lang = "ru-RU"
sr.LANGUAGE = lang

os.system("@echo off")
os.system("title voiceGPT")
os.system("cls")

while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            input("Press any key to ask assistant!")
            audio = r.listen(source)

        text = r.recognize_google(audio, language=lang)

        print(f"\nYou: {Fore.GREEN}{text}{Fore.RESET}\n")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistent!"},
                {"role": "user", "content": text}
            ],
        )
        print(f"AI: {Fore.YELLOW}{response.choices[0].message.content}{Fore.RESET}\n\n")
    except KeyboardInterrupt:
        print("\nExiting...")
        time.sleep(2)
