import webbrowser
import os
import pyttsx3

def speak(text):
    """Convert text to speech."""
    tts_engine = pyttsx3.init()
    tts_engine.say(text)
    tts_engine.runAndWait()

def run_action(command):
    """Execute actions based on the command."""
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "launch code" in command:
        os.system("code")  # Assumes VS Code is in PATH
        speak("Launching Visual Studio Code.")
    elif "play music" in command:
        # Replace 'path_to_music_file' with the actual file path
        os.system("start path_to_music_file")  # Windows-specific
        speak("Playing music.")
    else:
        speak("I'm not sure how to help with that.")
