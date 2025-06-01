import webbrowser
import os
import pyttsx3
import random

def speak(text):
    """Convert text to speech."""
    tts_engine = pyttsx3.init()
    tts_engine.say(text)
    tts_engine.runAndWait()

def run_action(command):
    """Execute actions based on the command."""
    command = command.lower()

    # Greetings
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
    if any(greet in command for greet in greetings):
        responses = [
            "Hello! How can I assist you today?",
            "Hi there! Ready to help.",
            "Hey! What can I do for you?",
            "Good day! How may I assist you?"
        ]
        speak(random.choice(responses))
        return

    # Responses to "How are you?"
    if "how are you" in command:
        responses = [
            "I'm functioning optimally, thank you!",
            "All systems go!",
            "I'm here to assist you."
        ]
        speak(random.choice(responses))
        return

    # Responses to "Thank you"
    if "thank you" in command or "thanks" in command:
        responses = [
            "You're welcome!",
            "No problem!",
            "Happy to help!",
            "Anytime!"
        ]
        speak(random.choice(responses))
        return

    # Open Google
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
        return

    # Open YouTube
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
        return

    # Launch VS Code
    if "launch code" in command:
        os.system("code")  # Assumes VS Code is in PATH
        speak("Launching Visual Studio Code.")
        return

    # Play Music
    if "play music" in command:
        # Replace 'path_to_music_file' with the actual file path
        os.system("start path_to_music_file")  # Windows-specific
        speak("Playing music.")
        return

    # Default response
    speak("I'm not sure how to help with that.")
