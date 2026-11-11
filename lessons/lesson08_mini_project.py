# Lesson 8: Mini project - putting Lessons 1-7 together
# Every code snippet from the lesson, in order.
# Section 6 asks for input when you run the file.

import random


# ============================================================
# 1. Plan before you code
# ============================================================

# A plan written as comments, before any real code:
#
# 1. Show a welcome message and ask the player's name
# 2. Repeat until the player quits:
#      - show a menu
#      - Play: ask 5 random questions, count correct answers, show the result
#      - High scores: show the table
# 3. Say goodbye
#
# Each line of the plan usually becomes one function.


# ============================================================
# 2. Constants
# ============================================================

MAX_ATTEMPTS = 10
OPTION_LETTERS = ["a", "b", "c", "d"]

print(MAX_ATTEMPTS)
print(OPTION_LETTERS)


# ============================================================
# 3. zip(): walking through two lists side by side
# ============================================================

letters = ["a", "b", "c"]
options = ["Paris", "Rome", "Berlin"]

for letter, option in zip(letters, options):
    print(f"{letter}) {option}")
# a) Paris
# b) Rome
# c) Berlin

# A string works too, because zip goes through it one character at a time
for letter, option in zip("abc", options):
    print(f"{letter}) {option}")

# zip stops at the SHORTER list
print(list(zip([1, 2, 3], ["x", "y"])))       # [(1, 'x'), (2, 'y')]

# Turning two lists into a dictionary
names = ["alex", "sam"]
ages = [25, 31]
people = dict(zip(names, ages))
print(people)                                  # {'alex': 25, 'sam': 31}


# ============================================================
# 4. The random module
# ============================================================

colors = ["red", "green", "blue"]
print(random.choice(colors))       # one random item, e.g. green

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)               # shuffles IN PLACE and returns None
print(deck)                        # e.g. [3, 1, 5, 2, 4]

# deck = random.shuffle(deck)      # ❌ deck would become None (same trap as .sort())

questions = ["q1", "q2", "q3", "q4"]
picked = random.sample(questions, 2)   # 2 random items as a NEW list, no repeats
print(picked)                          # e.g. ['q3', 'q1']
print(questions)                       # unchanged: ['q1', 'q2', 'q3', 'q4']

print(random.randint(1, 6))            # a dice roll (from Lesson 5)


# ============================================================
# 5. Formatting output as a table
# ============================================================

scores = {"alex": 4, "sam": 5, "jo": 2}

print(f"{'Name':<10}{'Score':>5}")
print("-" * 15)
for name, score in sorted(scores.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{name.title():<10}{score:>5}")
# Name      Score
# ---------------
# Sam           5
# Alex          4
# Jo            2

ratio = 4 / 5
print(f"{ratio:.0%}")       # 80%   ← :.0% multiplies by 100 and adds the % sign
print(f"{ratio:.1%}")       # 80.0%


# ============================================================
# 6. A reusable input validator
# ============================================================

def ask(prompt: str) -> str:
    """Ask the user something and return the cleaned answer."""
    return input(prompt).strip().lower()


def ask_yes_no(prompt: str) -> bool:
    """Keep asking until the user types y or n. Return True for y, False for n."""
    while True:
        answer = ask(prompt)
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please type y or n.")


if ask_yes_no("Do you like Python? (y/n) "):
    print("Great!")
else:
    print("You will soon!")


# ============================================================
# 7. Functions that return True/False, and counting them
# ============================================================

def is_even(number: int) -> bool:
    """Return True if the number is even."""
    return number % 2 == 0


count = 0
for n in [3, 8, 10, 7, 4]:
    if is_even(n):
        count += 1
print(f"{count} even numbers")     # 3 even numbers


# ============================================================
# 8. Data-driven programs: content lives in data, not in code
# ============================================================

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "a",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "b",
    },
]

q = QUESTIONS[0]
print(q["question"])
for letter, option in zip(OPTION_LETTERS, q["options"]):
    print(f"  {letter}) {option}")

# Finding the text of the correct answer from its letter
index = OPTION_LETTERS.index(q["answer"])     # "a" → 0
print(q["options"][index])                    # Paris


# ============================================================
# 9. main() and if __name__ == "__main__":
# ============================================================

def main() -> None:
    """The program starts here."""
    print("Program starts here")


if __name__ == "__main__":
    main()
