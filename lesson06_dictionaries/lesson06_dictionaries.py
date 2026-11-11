person = {
    "name": "Alex",
    "age": 25,
    "city": "Sofia",
}

print(person["name"])  # Alex
print(len(person))  # 3

# print(person["email"])              # KeyError: the key doesn't exist

print(person.get("email"))  # None   (no crash)
print(person.get("email", "N/A"))  # N/A    (your default value)

if "email" in person:  # `in` checks KEYS
    print(person["email"])

person["email"] = "alex@mail.com"  # add a new key
person["age"] = 26  # change an existing one (same syntax)

del person["city"]  # remove (KeyError if missing)
email = person.pop("email")  # remove AND return the value
person.pop("phone", None)  # remove if present, no crash otherwise

person.update({"age": 27, "job": "dev"})  # change or add several at once

scores = {"Alex": 85, "Sam": 92, "Jo": 78}

for name in scores:  # loops over the KEYS
    print(name)

for score in scores.values():  # just the values
    print(score)

for name, score in scores.items():  # keys AND values, the most used one
    print(f"{name}: {score}")

print(list(scores.keys()))  # ['Alex', 'Sam', 'Jo']
print(sum(scores.values()))  # 255
print(max(scores, key=scores.get))  # Sam  (the key with the highest value)

text = "the cat and the dog and the bird"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}

students = [
    {"name": "Alex", "grade": 85},
    {"name": "Sam", "grade": 92},
    {"name": "Jo", "grade": 78},
]

for s in students:
    print(f"{s['name']} got {s['grade']}")

best = max(students, key=lambda s: s["grade"])
print(best["name"])  # Sam

messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is Python?"},
            {"role": "assistant", "content": "Python is a programming language..."},
            {"role": "user", "content": "Is it hard to learn?"}, {"role": "user", "content": "Thanks!"}]

for msg in messages:
    print(f"[{msg['role']}] {msg['content']}")

response = {
    "id": "resp_123",
    "output": [
        {"type": "message", "content": [{"type": "text", "text": "Hello there!"}]}
    ],
    "usage": {"input_tokens": 12, "output_tokens": 4},
}

print(response["output"][0]["content"][0]["text"])    # Hello there!
print(response["usage"]["output_tokens"])             # 4

names = ["alex", "sam", "jo"]
lengths = {name: len(name) for name in names}       # {'alex': 4, 'sam': 3, 'jo': 2}

prices = {"apple": 1.2, "banana": 0.5, "cherry": 3.0}
cheap = {k: v for k, v in prices.items() if v < 2}  # {'apple': 1.2, 'banana': 0.5}

tags = {"python", "ai", "python", "rag"}
print(tags)                    # {'python', 'ai', 'rag'}  ← duplicate removed

unique = list(set([1, 2, 2, 3, 3, 3]))    # [1, 2, 3]
print("ai" in tags)            # True, and very fast to check