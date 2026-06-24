from datetime import datetime
import webbrowser


def get_time():
    """
    Return current system time.
    """
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}."


def get_date():
    """
    Return today's date.
    """
    current_date = datetime.now().strftime("%B %d, %Y")
    return f"Today is {current_date}."


def search_web(query):
    """
    Search the web using the default browser.
    """
    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)

    return f"Searching for {query}"