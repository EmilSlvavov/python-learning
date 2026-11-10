def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    return prompt.strip().lower()


def ask_int(text: str) -> int:
    """Keeps asking until the user types something that is digits only and returns it as an int"""
    while not text.isdigit():
        text = input("Try again!")
    return int(text)


def word_count(text: str) -> dict[str, int]:
    """Counts how many times a word has been said in a string. Returns a dictionary of the result"""
    counts = {}
    for word in text.split():
        word = word.strip(".,!?").lower()
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_words(counts: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Returns the n most common words with n = 5 by default"""
    top = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]
    return list(top)
