import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # male voice
engine.setProperty('volume', 1.0)

def speak(text): 
    print("Supru:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

engine.setProperty('rate', 170)

speak("Hello Sanjeev. I am Supru.")

while True:

    try:
        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)

        print("You:", command)

        command = command.lower()

        # Exit command
        if "exit" in command or "goodbye" in command:
            speak("Goodbye Sanjeev")
            break

        # Time command
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        # Greeting
        elif "hello" in command:
            speak("Hello Sanjeev")

        else:
            speak(f"I heard {command}")

    except sr.UnknownValueError:
        print("Could not understand.")

    except Exception as e:
        print("Error:", e)

