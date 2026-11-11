text = input("Give a small paragraph: ") #Every day is a new opportunity to learn something, explore the world, and become a better version of yourself. Life may bring challenges along the way, but with patience, determination, and a positive attitude, anything is possible. Remember to enjoy the little moments, appreciate the people around you, and never stop chasing your dreams.
counts = {}

for word in text.split():
    word = word.strip(".,!?").lower()
    counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]
for word, count in top:
    print(f"{word}: {count}")

print(f"There are {len(counts)} unique words in this text!")
