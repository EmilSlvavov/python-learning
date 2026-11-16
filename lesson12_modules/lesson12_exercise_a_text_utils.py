from collections import Counter

STOP_WORDS = {"a", "an", "the", "is", "are", "and", "of", "to", "in", "it", "for"}


def clean_words(text: str) -> list[str]:
    """Returns clean words from text"""
    return [word.strip(".,!?;:").lower()
            for word in text.split()
            if word.strip(".,!?;:")]


def word_count(text: str) -> int:
    """Returns word count of text"""
    return len(text.split())



def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Returns all the top words which arent part of STOP_WORDS"""
    filtered_words = [word for word in clean_words(text) if word not in STOP_WORDS]
    counts = Counter(filtered_words)
    return counts.most_common(n)

if __name__ == "__main__":
    print("Self-test:")
    print(clean_words("The cat sat. The cat ran! A dog sat."))
    print(word_count("Hello big world"))
    print(top_words("The cat sat. The cat ran! A dog sat.", 2))
    print(top_words("", 3))