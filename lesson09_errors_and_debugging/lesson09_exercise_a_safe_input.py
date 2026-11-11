def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    user_message = input(prompt).strip().lower()
    return user_message

def ask_int(prompt: str, minimum: int, maximum: int) -> int:
    """Asks for an integer number and continues until it receives one
    that is also in the range between minimum and maximum"""
    while True:
        try:
            num = int(input(prompt))
            if num < minimum or num > maximum:
                print(f"Please enter a number between {minimum} and {maximum}")
                continue
            return num
        except ValueError:
            print("Please enter a whole number.")

def ask_float(prompt: str) -> float:
    """Asks for a float number and continues until it receives one"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

age = ask_int("Age: ", 0, 120)
height = ask_float("Height in meters: ")
print(f"Age: {age}, height: {height} m")