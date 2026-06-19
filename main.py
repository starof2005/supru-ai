import speech_recognition as sr
from datetime import datetime
import asyncio
import edge_tts
import pygame
import os

# Initialize recognizer

recognizer = sr.Recognizer()

# --------------------------

# SPEAK FUNCTION

# --------------------------

async def speak_async(text):


    filename = "voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )

    await communicate.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    if os.path.exists(filename):
        os.remove(filename)

def speak(text):
    print("Supru:", text)
    asyncio.run(speak_async(text))

# --------------------------

# STARTUP

# --------------------------

speak("Hello Sanjeev. I am Supru. How can I help you?")

# --------------------------

# MAIN LOOP

# --------------------------

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)

        print("You:", command)

        command = command.lower()

        # EXIT
        if "exit" in command or "goodbye" in command:

            speak("Goodbye Sanjeev")
            break

        # HELLO
        elif "hello" in command or "hi" in command:

            speak("Hello Sanjeev")

        # TIME
        elif "time" in command:

            current_time = datetime.now().strftime("%I:%M %p")

            speak(
                f"The current time is {current_time}"
            )

        # DATE
        elif "date" in command:

            today = datetime.now().strftime("%d %B %Y")

            speak(
                f"Today's date is {today}"
            )

        # HOW ARE YOU
        elif "how are you" in command:

            speak(
                "I am doing great. Thank you for asking."
            )

        elif "your name" in command:

            speak(
                "I am Supru.The AI Assistant of sanjeev"
            )

        elif "created you" in command or "who made you" in command or "who is your creator" in command:

            speak(
                "I am Supru. I was created by sanjeev."
            )

        elif "thank you" in command:
            speak("You are welcome Sanjeev")

#OPENING APPLICATIONS OF OS
        elif "open chrome" in command or "open google chrome" in command or "chrome" in command or "google chrome" in command or "open google" in command or "google" in command:

            speak("Opening Chrome")

            os.system("start chrome")

        elif "open notepad" in command or "notepad" in command:

            speak("Opening Notepad")

            os.system("notepad")

        elif "open calculator" in command or "calculator" in command or "calc" in command or "open calc" in command:

            speak("Opening Calculator")

            os.system("calc")

        elif "open file explorer" in command or "file explorer" in command or "explorer" in command or "open explorer" in command:

            speak("Opening File Explorer")

            os.system("explorer")


        # DEFAULT RESPONSE
        else:

            speak(
                f"I heard {command}"
            )

    except sr.UnknownValueError:

        print("Could not understand.")

    except Exception as e:

        print("Error:", e)

