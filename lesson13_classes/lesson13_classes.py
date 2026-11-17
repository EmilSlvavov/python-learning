# Lesson 13: Classes
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.

from dataclasses import dataclass, field, asdict


# ============================================================
# 1. The simplest class: __init__ and self
# ============================================================

class Dog:
    def __init__(self, name: str, age: int):    # the constructor
        self.name = name                         # attributes are created by assigning to self
        self.age = age


rex = Dog("Rex", 3)          # no "new" keyword
print(rex.name)              # Rex
print(rex.age)               # 3

rex.age = 4                  # attributes are public and changeable
print(rex.age)               # 4


# ============================================================
# 2. Methods: functions that belong to the class
# ============================================================

class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self) -> str:                       # self is ALWAYS the first parameter
        return f"{self.name} says woof!"

    def birthday(self) -> None:
        self.age += 1                            # changes THIS object's age


rex = Dog("Rex", 3)
print(rex.bark())            # Rex says woof!   <- Python passes rex as self automatically
rex.birthday()
print(rex.age)               # 4

print(Dog.bark(rex))         # Rex says woof!   <- what rex.bark() really does behind the scenes


# ============================================================
# 3. Printing objects: __str__ and __repr__ (like toString)
# ============================================================

print(rex)                   # <__main__.Dog object at 0x000001...>  <- not helpful


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:                    # for people: print(), f-strings, str()
        return f"{self.name} ({self.age})"

    def __repr__(self) -> str:                   # for developers: debugger, lists, console
        return f"Dog(name={self.name!r}, age={self.age})"


rex = Dog("Rex", 3)
print(rex)                   # Rex (3)
print(f"My dog: {rex}")      # My dog: Rex (3)
print([rex, Dog("Bella", 5)])   # [Dog(name='Rex', age=3), Dog(name='Bella', age=5)]  <- lists use __repr__


# ============================================================
# 4. Other special ("dunder") methods
# ============================================================

class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add(self, song: str) -> None:
        self.songs.append(song)

    def __len__(self) -> int:                    # makes len(playlist) work
        return len(self.songs)

    def __contains__(self, song: str) -> bool:   # makes "x in playlist" work
        return song in self.songs


playlist = Playlist("Road trip")
playlist.add("Song A")
playlist.add("Song B")
print(len(playlist))           # 2
print("Song A" in playlist)    # True
print("Song Z" in playlist)    # False


# ============================================================
# 5. Validation: raise in __init__
# ============================================================

class Temperature:
    def __init__(self, celsius: float):
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32


print(Temperature(100).to_fahrenheit())    # 212.0

try:
    Temperature(-300)
except ValueError as e:
    print(f"Error: {e}")                   # Error: Temperature below absolute zero


# ============================================================
# 6. Class attributes vs instance attributes
# ============================================================

class Counter:
    created = 0                          # CLASS attribute: shared by all objects (like static)

    def __init__(self):
        self.count = 0                   # INSTANCE attribute: each object has its own
        Counter.created += 1


a = Counter()
b = Counter()
a.count += 5
print(a.count, b.count)                  # 5 0
print(Counter.created)                   # 2


# ❌ Trap: a mutable class attribute is shared by EVERYONE
class BadCart:
    items = []                           # one list for all carts!

    def add(self, item: str) -> None:
        self.items.append(item)


cart1 = BadCart()
cart2 = BadCart()
cart1.add("apple")
print(cart2.items)                       # ['apple']  <- cart2 sees cart1's item

# ✅ Create lists/dicts in __init__ so each object gets its own (like Playlist above)


# ============================================================
# 7. "Private" attributes and @property (getters/setters)
# ============================================================

class Account:
    def __init__(self, owner: str):
        self.owner = owner
        self._balance = 0.0              # leading _ = "internal, don't touch from outside"

    @property
    def balance(self) -> float:          # read it like an attribute: account.balance
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount


acc = Account("Ana")
acc.deposit(50)
print(acc.balance)                       # 50.0   <- no parentheses, it's a property
# acc.balance = 1_000_000                # ❌ AttributeError: property 'balance' has no setter


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age                   # goes through the setter below, so it's validated too

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:   # runs on every "person.age = ..."
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


p = Person("Ana", 28)
p.age = 29
print(p.age)                             # 29
try:
    p.age = -1
except ValueError as e:
    print(f"Error: {e}")                 # Error: Age cannot be negative


# ============================================================
# 8. Objects are references (same as Java)
# ============================================================

d1 = Dog("Rex", 3)
d2 = d1                       # NOT a copy: both names point to the same object
d2.age = 10
print(d1.age)                 # 10

d3 = Dog("Rex", 10)
print(d1 == d3)               # False  <- by default == compares identity (like Java's ==)
print(d1 is d2)               # True   <- "is" is always identity


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:          # like overriding equals() in Java
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


print(Point(1, 2) == Point(1, 2))   # True


# ============================================================
# 9. Inheritance
# ============================================================

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def introduce(self) -> str:
        return f"I am {self.name} and I say {self.speak()}"


class Cat(Animal):                            # Cat extends Animal
    def speak(self) -> str:                   # override
        return "meow"


class Parrot(Animal):
    def __init__(self, name: str, words: list[str]):
        super().__init__(name)                # call the parent constructor
        self.words = words

    def speak(self) -> str:
        return ", ".join(self.words)


animals = [Cat("Tom"), Parrot("Polly", ["hello", "cracker"])]
for animal in animals:
    print(animal.introduce())
# I am Tom and I say meow
# I am Polly and I say hello, cracker

print(isinstance(animals[0], Cat))       # True
print(isinstance(animals[0], Animal))    # True  (a Cat IS an Animal)


# ============================================================
# 10. @dataclass: less boilerplate (like a Java record / Lombok)
# ============================================================

@dataclass
class Book:
    title: str
    author: str
    pages: int = 0                       # default value


book = Book("Dune", "Frank Herbert", 412)
print(book)                              # Book(title='Dune', author='Frank Herbert', pages=412)  <- free __repr__
print(book == Book("Dune", "Frank Herbert", 412))   # True  <- free __eq__ (compares fields)
print(Book("Notes", "Me"))               # Book(title='Notes', author='Me', pages=0)

book.pages = 500                         # still a normal, changeable object


@dataclass
class Library:
    name: str
    books: list[Book] = field(default_factory=list)   # ✅ a NEW list for every Library
    # books: list[Book] = []                          # ❌ ValueError: mutable default not allowed


lib = Library("Home")
lib.books.append(book)
print(len(lib.books))                    # 1


@dataclass
class Message:
    role: str
    content: str

    def __post_init__(self):             # runs right after the generated __init__: validate here
        if self.role not in {"system", "user", "assistant"}:
            raise ValueError(f"Invalid role: {self.role}")

    def __str__(self) -> str:            # you can still write your own methods
        return f"{self.role}: {self.content}"


print(Message("user", "Hi"))             # user: Hi
try:
    Message("robot", "beep")
except ValueError as e:
    print(f"Error: {e}")                 # Error: Invalid role: robot


# ============================================================
# 11. @classmethod: alternative constructors (like a static factory)
# ============================================================

@dataclass
class User:
    name: str
    email: str

    @classmethod
    def from_dict(cls, data: dict) -> "User":    # cls is the class itself (here: User)
        return cls(data["name"], data["email"])

    @staticmethod
    def is_valid_email(email: str) -> bool:      # no self, no cls: just a function inside the class
        return "@" in email


user = User.from_dict({"name": "Ana", "email": "ana@example.com"})
print(user)                              # User(name='Ana', email='ana@example.com')
print(User.is_valid_email("nope"))       # False

print(asdict(user))                      # {'name': 'Ana', 'email': 'ana@example.com'}  <- ready for json.dump
print(User(**{"name": "Bob", "email": "bob@example.com"}))   # ** unpacking from Lesson 7 also works


# ============================================================
# 12. Lists of objects: sorting and filtering by attribute
# ============================================================

books = [
    Book("Dune", "Frank Herbert", 412),
    Book("Hobbit", "J.R.R. Tolkien", 310),
    Book("Neuromancer", "William Gibson", 271),
]

for b in sorted(books, key=lambda b: b.pages):
    print(f"{b.title:<12}{b.pages:>5}")
# Neuromancer   271
# Hobbit        310
# Dune          412

long_books = [b.title for b in books if b.pages > 300]
print(long_books)                        # ['Dune', 'Hobbit']


# ============================================================
# 13. Why this matters for OpenAI: objects instead of dicts
# ============================================================

# With plain JSON (Lesson 11) you write:   response["output"][0]["content"][0]["text"]
# The openai library returns OBJECTS, so you write:   response.output_text
#                                                      response.usage.total_tokens
# Same data, accessed with dots instead of ["..."].
