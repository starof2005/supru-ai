import speech_recognition as sr
from datetime import datetime
import asyncio
import edge_tts
import pygame
import os
import webbrowser

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

#SEARCHING ON YOUTUBE
        elif "search" in command and "youtube" in command:

            query = command

            query = query.replace("search", "")
            query = query.replace("youtube", "")
            query = query.replace("you tube", "")
            query = query.replace("on", "")
            query = query.replace("for", "")

            query = query.strip()

            speak(f"Searching YouTube for {query}")

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

#OPENING WEBSITES
        elif "open youtube" in command or "youtube" in command or "open you tube" in command or "you tube" in command or "u tube" in command:

            speak("Opening YouTube")

            webbrowser.open("https://www.youtube.com")


        elif "open facebook" in command or "facebook" in command or "open fb" in command or "fb" in command or "open face book" in command or "face book" in command:

            speak("Opening Facebook")

            webbrowser.open("https://www.facebook.com")

        elif "open twitter" in command or "twitter" in command:

            speak("Opening Twitter")

            webbrowser.open("https://www.twitter.com")

        elif "open instagram" in command or "instagram" in command or "open insta" in command or "insta" in command:

            speak("Opening Instagram")

            webbrowser.open("https://www.instagram.com")

        elif "open linkedin" in command or "linkedin" in command or "open linked" in command or "linked" in command or "open linked in" in command or "linked in" in command:

            speak("Opening LinkedIn")

            webbrowser.open("https://www.linkedin.com")

        elif "open github" in command or "github" in command or "open git hub" in command or "git hub" in command:

            speak("Opening GitHub")

            webbrowser.open("https://www.github.com")

        elif "open gmail" in command or "gmail" in command or "open mail" in command or "mail" in command or "open google mail" in command or "google mail" in command or "g mail" in command or "g mall" in command:

            speak("Opening Gmail")

            webbrowser.open("https://mail.google.com")

        elif "open chat g p t" in command or "open chatgpt" in command:

            speak("Opening ChatGPT")

            webbrowser.open("https://chatgpt.com")

#SEARCHING ON GOOGLE
        elif "search" in command:

            search_query = command.replace("search", "").strip()

            speak(f"Searching for {search_query}")

            webbrowser.open(
                f"https://www.google.com/search?q={search_query}"
            )


#SEARCHING ON WIKIPEDIA
        elif "wikipedia" in command:

            search_query = command.replace("wikipedia", "").strip()

            speak(f"Searching for {search_query} on Wikipedia")

            webbrowser.open(
                f"https://en.wikipedia.org/wiki/{search_query}"
            )


        # DEFAULT RESPONSE
        else:

            speak(
                f"I heard {command}"
            )

    except sr.UnknownValueError:

        print("Could not understand.")

    except Exception as e:

        print("Error:", e)

