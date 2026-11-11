def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    user_message = input(prompt).strip().lower()
    return user_message


def ask_int(text: str) -> int:
    """Keeps asking until the user types something that is digits only and returns it as an int"""
    number = input(text)
    while not number.isdigit():
        number = input("Try again! ")
    return int(number)


def word_count(text: str) -> dict[str, int]:
    """Counts how many times a word has been said in a string. Returns a dictionary of the result"""
    counts = {}
    for word in text.split():
        word = word.strip(".,!?").lower()
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_words(counts: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Returns the n most common words with n = 5 by default"""
    top = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:n]
    return top

print(word_count("the cat and the dog"))
print(top_words(word_count("a b a c a b"), 2))
ask_int("Enter: ")
print(ask("Enter text: "))