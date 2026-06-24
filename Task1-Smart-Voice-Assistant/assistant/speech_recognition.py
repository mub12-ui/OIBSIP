import speech_recognition as sr


def listen():
    """
    Listen to user's voice and convert it to text.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print(f"User: {command}")

            return command

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

    except Exception as e:
        print(f"Error: {e}")
        return ""