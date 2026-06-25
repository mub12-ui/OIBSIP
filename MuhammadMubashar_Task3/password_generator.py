import random
import string


def get_choice(prompt):
    """Validate y/n user input."""
    choice = input(prompt).lower()

    if choice not in ["y", "n"]:
        print("Error: Please enter only 'y' or 'n'.")
        exit()

    return choice


def generate_password(length, characters):
    """Generate a random password."""
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Random Password Generator ===")

    # Validate password length
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Error: Password length must be greater than 0.")
            return

    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Character type selection
    include_letters = get_choice("Include letters? (y/n): ")
    include_numbers = get_choice("Include numbers? (y/n): ")
    include_symbols = get_choice("Include symbols? (y/n): ")

    characters = ""

    if include_letters == "y":
        characters += string.ascii_letters

    if include_numbers == "y":
        characters += string.digits

    if include_symbols == "y":
        characters += string.punctuation

    # Validate character pool
    if not characters:
        print("Error: At least one character type must be selected.")
        return

    # Generate and display password
    password = generate_password(length, characters)

    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()