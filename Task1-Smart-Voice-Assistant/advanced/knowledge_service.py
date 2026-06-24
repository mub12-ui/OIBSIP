import wikipedia


def answer_question(question):
    """
    Answer a general knowledge question using Wikipedia.
    """

    try:
        result = wikipedia.summary(question, sentences=2)

        return result

    except wikipedia.exceptions.DisambiguationError:
        return "Your question is ambiguous. Please be more specific."

    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find information about that."

    except Exception:
        return "Unable to answer the question."