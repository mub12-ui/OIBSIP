from assistant.speech_recognition import listen
from assistant.command_processor import process_command
from assistant.text_to_speech import speak


def main():
    """
    Main loop for the voice assistant.
    """

    speak("Hello! I am your Smart Voice Assistant.")

    while True:
        command = listen()

        if not command:
            speak("Sorry, I could not understand.")
            continue

        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        response = process_command(command)

        speak(response)


if __name__ == "__main__":
    main()