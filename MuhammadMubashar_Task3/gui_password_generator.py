import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate a password based on user selections
def generate_password():

    # Validate password length input
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror(
                "Invalid Length",
                "Password length must be greater than 0."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )
        return

    # Create character pool based on selected options
    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    # Ensure at least one character type is selected
    if not characters:
        messagebox.showerror(
            "Selection Error",
            "Select at least one character type."
        )
        return

    # Remove excluded characters
    excluded_chars = exclude_entry.get()

    for char in excluded_chars:
        characters = characters.replace(char, "")

    # Ensure character pool is not empty after exclusions
    if not characters:
        messagebox.showerror(
            "Character Pool Error",
            "No characters available after applying exclusions."
        )
        return

    # Count selected character types
    selected_types = 0

    if letters_var.get():
        selected_types += 1

    if numbers_var.get():
        selected_types += 1

    if symbols_var.get():
        selected_types += 1

    # Ensure password length can accommodate all selected types
    if length < selected_types:
        messagebox.showerror(
            "Invalid Length",
            f"Password length must be at least {selected_types}."
        )
        return

    # Generate strong password
    password = []

    # Ensure at least one character from each selected category
    if letters_var.get():
        available_letters = ''.join(
            char for char in string.ascii_letters
            if char not in excluded_chars
        )

        if available_letters:
            password.append(random.choice(available_letters))

    if numbers_var.get():
        available_numbers = ''.join(
            char for char in string.digits
            if char not in excluded_chars
        )

        if available_numbers:
            password.append(random.choice(available_numbers))

    if symbols_var.get():
        available_symbols = ''.join(
            char for char in string.punctuation
            if char not in excluded_chars
        )

        if available_symbols:
            password.append(random.choice(available_symbols))

    # Fill remaining characters
    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(random.choice(characters))

    # Shuffle password characters
    random.shuffle(password)

    # Convert list to string
    password = "".join(password)

    # Display generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Function to copy generated password to clipboard
def copy_password():

    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


# Create main application window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x420")
root.resizable(False, False)

# Application title
title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# Password length input
length_label = tk.Label(
    root,
    text="Password Length:"
)
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Variables for checkbox selections
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

# Character type checkboxes
letters_check = tk.Checkbutton(
    root,
    text="Include Letters",
    variable=letters_var
)
letters_check.pack()

numbers_check = tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var
)
numbers_check.pack()

symbols_check = tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var
)
symbols_check.pack()

# Exclude characters input
exclude_label = tk.Label(
    root,
    text="Exclude Characters:"
)
exclude_label.pack()

exclude_entry = tk.Entry(root, width=20)
exclude_entry.pack(pady=5)

# Generate password button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=10)

# Copy password button
copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=5)

# Password output section
password_label = tk.Label(
    root,
    text="Generated Password:"
)
password_label.pack()

password_entry = tk.Entry(
    root,
    width=35
)
password_entry.pack(pady=5)

# Run the application
root.mainloop()