from assistant.actions import get_time, get_date, search_web

from advanced.weather_service import get_weather
from advanced.knowledge_service import answer_question
from advanced.reminder_service import add_reminder, show_reminders
from advanced.smart_home import turn_on, turn_off
from advanced.custom_commands import execute_custom_command
from advanced.email_service import send_email

from config.secrets import TEST_RECEIVER


def process_command(command):
    """
    Process user commands and return a response.
    """

    command = command.lower()

    # Greeting
    if "hello" in command:
        return "Hello! How can I help you?"

    # Time
    elif "time" in command:
        return get_time()

    # Date
    elif "date" in command:
        return get_date()

    # Web search
    elif "search" in command:
        query = command.replace("search", "").strip()

        if query:
            return search_web(query)

        return "Please tell me what to search for."

    # Weather
    elif "weather" in command:
        city = command.replace("weather in", "").strip()

        if city:
            return get_weather(city)

        return "Please specify a city."

    # General knowledge
    elif "who is" in command or "what is" in command:
        query = (
            command.replace("who is", "")
            .replace("what is", "")
            .strip()
        )

        return answer_question(query)

    # Add reminder
    elif "remind me" in command:
        task = command.replace("remind me", "").strip()

        if task:
            return add_reminder(task)

        return "Please tell me what to remind you about."

    # Show reminders
    elif "show reminders" in command:
        return show_reminders()

    # Smart home controls
    elif "turn on" in command:
        device = command.replace("turn on", "").strip()

        return turn_on(device)

    elif "turn off" in command:
        device = command.replace("turn off", "").strip()

        return turn_off(device)

    # Email
    elif "send email" in command:
        success = send_email(
            TEST_RECEIVER,
            "Test Email",
            "Hello! This email was sent from my Smart Voice Assistant."
        )

        if success:
            return "Email sent successfully."

        return "Failed to send email."

    # Custom commands
    custom_response = execute_custom_command(command)

    if custom_response:
        return custom_response

    # Unknown command
    return "Sorry, I don't understand that command."