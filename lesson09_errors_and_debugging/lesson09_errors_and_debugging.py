# Lesson 9: Errors and debugging
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Sections 6 and 7 ask for input when you run the file.


# ============================================================
# 1. Reading a traceback
# ============================================================

def get_age(text):
    return int(text)

# get_age("abc")     # ❌ uncomment to see the traceback below

# Traceback (most recent call last):
#   File "C:\...\lesson09_errors_and_debugging.py", line 14, in <module>
#     get_age("abc")
#   File "C:\...\lesson09_errors_and_debugging.py", line 12, in get_age
#     return int(text)
#            ^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'abc'
#
# Read it from the BOTTOM up:
#   last line          → WHAT went wrong (error type + message)
#   the lines above it → WHERE: file, line number, function, the code itself
#   the top            → how the program got there (who called whom)


# ============================================================
# 2. The errors you'll see most
# ============================================================

# print("hi"                  # ❌ SyntaxError: '(' was never closed
# undefined_name + 1          # ❌ NameError: name 'undefined_name' is not defined
# "age: " + 25                # ❌ TypeError: can only concatenate str (not "int") to str
# int("abc")                  # ❌ ValueError: invalid literal for int() with base 10: 'abc'
# {"a": 1}["b"]               # ❌ KeyError: 'b'
# [1, 2, 3][10]               # ❌ IndexError: list index out of range
# 10 / 0                      # ❌ ZeroDivisionError: division by zero
# "hello".push("!")           # ❌ AttributeError: 'str' object has no attribute 'push'
# open("missing.txt")         # ❌ FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'


# ============================================================
# 3. try / except: catching an error
# ============================================================

try:
    number = int("abc")
    print("This line is skipped")
except ValueError:
    print("That was not a number!")

print("The program keeps running")


# ============================================================
# 4. Catch SPECIFIC errors
# ============================================================

def safe_divide(a: float, b: float) -> float | None:
    """Divide a by b, or return None if that's impossible."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except TypeError:
        print("Both values must be numbers.")
        return None

print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Cannot divide by zero. / None
print(safe_divide(10, "x"))    # Both values must be numbers. / None

# Several error types handled the same way
data = {"a": [1, 2]}
try:
    value = data["b"][5]
except (KeyError, IndexError):
    print("That data doesn't exist.")

# ❌ Don't do this: it hides EVERY error, including your own typos
# try:
#     total = sum(numbrs)       # typo → NameError, silently swallowed
# except:
#     print("Something went wrong")


# ============================================================
# 5. Getting the error message with "as"
# ============================================================

try:
    int("12abc")
except ValueError as e:
    print(f"Error: {e}")        # Error: invalid literal for int() with base 10: '12abc'
    print(type(e).__name__)     # ValueError


# ============================================================
# 6. else and finally
# ============================================================

text = input("Enter a number: ")
try:
    number = int(text)
except ValueError:
    print("Not a number.")
else:
    print(f"Double: {number * 2}")    # runs only if NO error happened
finally:
    print("Done.")                    # ALWAYS runs, error or not


# ============================================================
# 7. try inside a loop: asking until the input is valid
# ============================================================

def ask_int(prompt: str) -> int:
    """Keep asking until the user types a whole number, then return it."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

age = ask_int("Your age? ")
print(f"Next year you'll be {age + 1}")

# Why this is better than .isdigit():
print("-5".isdigit())     # False, but int("-5") works
print(" 7 ".isdigit())    # False, but int(" 7 ") works (int ignores outer spaces)
print(int("-5"), int(" 7 "))


# ============================================================
# 8. Raising your own errors
# ============================================================

def set_age(age: int) -> int:
    """Return the age if it is valid, otherwise raise ValueError."""
    if age < 0 or age > 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    return age

print(set_age(30))     # 30

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")    # Error: Age must be between 0 and 120, got 200


# ============================================================
# 9. Check first, or try first?
# ============================================================

phonebook = {"alex": "0888123456"}

# "Look before you leap": check first
if "sam" in phonebook:
    print(phonebook["sam"])
else:
    print("Not found.")

# "Easier to ask forgiveness than permission": try first
try:
    print(phonebook["sam"])
except KeyError:
    print("Not found.")

# For dictionaries, .get() is usually the simplest of all
print(phonebook.get("sam", "Not found."))


# ============================================================
# 10. The PyCharm debugger
# ============================================================

def total_price(prices: list[float], discount: float) -> float:
    total = 0
    for price in prices:
        total += price
    total = total - total * discount
    return total

# 1. Click in the gutter (left of the line number) next to "total += price" → red dot
# 2. Right-click the file → Debug (or Shift+F9)
# 3. F8 = step over, F7 = step into a function, F9 = resume to the next breakpoint
# 4. Watch "total" and "price" change in the Variables panel
print(total_price([10.0, 20.0, 30.0], 0.1))    # 54.0


# ============================================================
# 11. Why this matters for OpenAI (preview, needs the openai package: Lesson 16)
# ============================================================

# import openai
#
# try:
#     response = client.responses.create(model="...", input="Hello")
# except openai.RateLimitError:
#     print("Too many requests, wait a moment and try again.")
# except openai.APIConnectionError:
#     print("Could not reach OpenAI. Check your internet connection.")
# except openai.APIError as e:
#     print(f"OpenAI returned an error: {e}")
