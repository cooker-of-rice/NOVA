import pyttsx3
import speech_recognition as sr
import webbrowser
import os
from actions import run_action

# Initialize the TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)

def speak(text):
    """Convert text to speech and print it."""
    print(f"SERENA: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for voice input and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return ""

def get_input_mode():
    """Prompt the user to select an input mode."""
    while True:
        mode = input("Choose input mode - Voice (v) or Text (t): ").strip().lower()
        if mode in ['v', 't']:
            return mode
        else:
            print("Invalid input. Please enter 'v' for Voice or 't' for Text.")

def main():
    """Main function to run the assistant."""
    speak("Hello, I am SERENA. How can I assist you today?")
    input_mode = get_input_mode()
    while True:
        if input_mode == 'v':
            command = listen()
        else:
            command = input("You: ").lower()

        if command in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        elif command:
            run_action(command)
        else:
            speak("Please provide a command.")

if __name__ == "__main__":
    main()
