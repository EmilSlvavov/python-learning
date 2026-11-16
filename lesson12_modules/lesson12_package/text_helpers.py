# A module inside the lesson12_package package.


def shout(text: str) -> str:
    """Returns the text in upper case with an exclamation mark."""
    return text.upper() + "!"


def whisper(text: str) -> str:
    """Returns the text in lower case with three dots."""
    return text.lower() + "..."
