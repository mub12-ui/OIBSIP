import json

COMMAND_FILE = "data/commands.json"


def load_commands():
    try:
        with open(COMMAND_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_commands(commands):
    with open(COMMAND_FILE, "w") as file:
        json.dump(commands, file, indent=4)


def add_custom_command(command, response):
    commands = load_commands()

    commands[command.lower()] = response

    save_commands(commands)

    return f"Custom command '{command}' added."


def execute_custom_command(command):
    commands = load_commands()

    return commands.get(command.lower())