import os

from main import speak

elif "open chrome" in command or "open google chrome" in command or "chrome" in command:

    speak("Opening Chrome")

    os.system("start chrome")

elif "open notepad" in command:

    speak("Opening Notepad")

    os.system("notepad")

elif "open calculator" in command:

    speak("Opening Calculator")

    os.system("calc")

elif "open file explorer" in command:

    speak("Opening File Explorer")

    os.system("explorer")

