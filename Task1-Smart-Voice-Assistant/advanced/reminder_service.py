import json

REMINDER_FILE = "data/reminders.json"


def load_reminders():
    try:
        with open(REMINDER_FILE, "r") as file:
            reminders = json.load(file)
        return reminders

    except Exception:
        return []


def save_reminders(reminders):
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(task):
    reminders = load_reminders()

    reminders.append(task)

    save_reminders(reminders)

    return f"Reminder added: {task}"


def show_reminders():
    reminders = load_reminders()

    if not reminders:
        return "No reminders found."

    result = "Your reminders are:\n"

    for i, reminder in enumerate(reminders, start=1):
        result += f"{i}. {reminder}\n"

    return result