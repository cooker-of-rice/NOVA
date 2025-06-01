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

def main():
    """Main function to run the assistant."""
    speak("Hello, I am SERENA. How can I assist you today?")
    while True:
        mode = input("Choose input mode - Voice (v) or Text (t): ").strip().lower()
        if mode == 'v':
            command = listen()
        elif mode == 't':
            command = input("You: ").lower()
        else:
            speak("Invalid input mode selected.")
            continue

        if command in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        elif command:
            run_action(command)
        else:
            speak("Please provide a command.")

if __name__ == "__main__":
    main()
