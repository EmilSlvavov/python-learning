# Lesson 7: Functions
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Section 9 asks for input when you run the file.


# ============================================================
# 1. Defining and calling a function
# ============================================================

def greet():
    print("Hello!")

greet()     # Hello!
greet()     # Hello!


# ============================================================
# 2. Parameters
# ============================================================

def greet(name):
    print(f"Hello, {name}!")

greet("Alex")     # Hello, Alex!
greet("Sam")      # Hello, Sam!

def add(a, b):
    print(a + b)

add(3, 4)         # 7


# ============================================================
# 3. return: sending a value back
# ============================================================

def add(a, b):
    return a + b

result = add(3, 4)
print(result)            # 7
print(add(10, 5) * 2)    # 30

# return also ends the function immediately
def check_age(age):
    if age < 0:
        return "Invalid"
    if age >= 18:
        return "Adult"
    return "Minor"

print(check_age(-1))     # Invalid
print(check_age(30))     # Adult
print(check_age(12))     # Minor

# A function without return gives back None
def say_hi():
    print("hi")

x = say_hi()
print(x)        # None


# ============================================================
# 4. Default values
# ============================================================

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alex"))               # Hello, Alex!
print(greet("Alex", "Welcome"))    # Welcome, Alex!


# ============================================================
# 5. Keyword arguments
# ============================================================

def make_profile(name, age, city="Unknown"):
    return f"{name}, {age}, from {city}"

print(make_profile("Alex", 25))
print(make_profile(age=25, name="Alex"))
print(make_profile("Alex", 25, city="Sofia"))

# This is how you'll call OpenAI later (no client exists yet, so it's commented out):
# client.responses.create(model="...", input="Hello", temperature=0.7)


# ============================================================
# 6. Returning several values
# ============================================================

def min_max(numbers):
    return min(numbers), max(numbers)    # this returns a tuple

low, high = min_max([4, 8, 1, 9])       # unpacking (Lesson 4)
print(low, high)                         # 1 9


# ============================================================
# 7. Scope: variables inside functions
# ============================================================

def make_total():
    total = 100       # exists only inside this function
    return total

make_total()
# print(total)        # ❌ NameError: total is not defined out here

# Exception: lists and dictionaries passed in CAN be changed by the function
def add_item(items, item):
    items.append(item)    # changes the caller's list

shopping = ["milk"]
add_item(shopping, "eggs")
print(shopping)           # ['milk', 'eggs']


# ============================================================
# 8. Docstrings and type hints
# ============================================================

def average(numbers: list[float]) -> float:
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4]))     # 2.5

def clean(text: str) -> str:
    """Strip spaces and lowercase the text."""
    return text.strip().lower()

def find_contact(book: dict[str, str], name: str) -> str | None:
    """Return the phone number, or None if not found."""
    return book.get(name)

print(clean("  HeLLo  "))                                  # hello
print(find_contact({"alex": "0888123456"}, "alex"))        # 0888123456
print(find_contact({"alex": "0888123456"}, "sam"))         # None


# ============================================================
# 9. Functions calling functions
# ============================================================

def clean(text: str) -> str:
    return text.strip().lower()

def ask(prompt: str) -> str:
    """Ask the user something and return the cleaned answer."""
    return clean(input(prompt))

name = ask("Name: ")
answer = ask("Continue? (y/n) ")
print(name, answer)


# ============================================================
# 10. Functions are values (bonus)
# ============================================================

words = ["banana", "Apple", "cherry"]
students = [
    {"name": "Alex", "grade": 85},
    {"name": "Sam", "grade": 92},
]

print(sorted(words, key=str.lower))                  # passing the str.lower function
print(max(students, key=lambda s: s["grade"]))       # passing a small lambda function

# A lambda is just a short function without a name
square = lambda x: x * x
print(square(4))     # 16

# is the same as
def square(x):
    return x * x

print(square(4))     # 16


# ============================================================
# 11. *args and **kwargs (just so you recognize them)
# ============================================================

def total(*numbers):          # collects any number of positional arguments into a tuple
    return sum(numbers)

print(total(1, 2, 3, 4))      # 10

def show(**options):          # collects keyword arguments into a dictionary
    for key, value in options.items():
        print(f"{key} = {value}")

show(model="gpt", temperature=0.7)


# ============================================================
# 11b. *args and **kwargs explained step by step
# ============================================================

# The problem: a normal function takes a FIXED number of arguments
def add_two(a, b):
    return a + b

print(add_two(1, 2))           # 3
# print(add_two(1, 2, 3))      # ❌ TypeError: takes 2 positional arguments but 3 were given

# *args: "collect ALL extra positional arguments into a TUPLE"
def add_all(*numbers):
    print(numbers, type(numbers))    # look at what you actually get
    return sum(numbers)

print(add_all(1, 2))           # (1, 2) <class 'tuple'>        → 3
print(add_all(1, 2, 3, 4))     # (1, 2, 3, 4) <class 'tuple'>  → 10
print(add_all())               # () <class 'tuple'>            → 0

# It's just a tuple, so you can loop over it
def shout(*words):
    for word in words:
        print(word.upper())

shout("hi", "there", "python")

# **kwargs: "collect ALL extra keyword arguments into a DICTIONARY"
def describe(**info):
    print(info, type(info))          # look at what you actually get

describe(name="Alex", age=25)
# {'name': 'Alex', 'age': 25} <class 'dict'>

describe(city="Sofia", job="dev", likes="python")
# {'city': 'Sofia', 'job': 'dev', 'likes': 'python'} <class 'dict'>

# Mixing normal parameters with them
def order(customer, *items, **details):
    print(f"Customer: {customer}")
    print(f"Items: {items}")
    print(f"Details: {details}")

order("Alex", "pizza", "cola", address="Main St 1", paid=True)
# Customer: Alex
# Items: ('pizza', 'cola')
# Details: {'address': 'Main St 1', 'paid': True}

# The reverse: * and ** when CALLING a function unpack a list / dict into arguments
def make_profile(name, age, city="Unknown"):
    return f"{name}, {age}, from {city}"

values = ["Alex", 25]
print(make_profile(*values))           # same as make_profile("Alex", 25)

settings = {"name": "Sam", "age": 31, "city": "Plovdiv"}
print(make_profile(**settings))        # same as make_profile(name="Sam", age=31, city="Plovdiv")

# Why this matters for OpenAI: you can keep request settings in a dictionary
# request = {"model": "...", "input": "Hello", "temperature": 0.7}
# client.responses.create(**request)
