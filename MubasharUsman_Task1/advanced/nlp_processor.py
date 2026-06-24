import nltk
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download("punkt")
nltk.download("punkt_tab")


def preprocess_command(command):
    """
    Convert a command into tokens.
    """
    command = command.lower()

    tokens = word_tokenize(command)

    return tokens