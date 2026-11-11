age = int(input("Your age? "))

if age >= 18:
    print("You are of age.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

print("This always runs.")

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")

if age < 12 or age > 65:
    print("Discount!")

if not has_ticket:
    print("Buy a ticket first.")

name = input("Name: ").strip()

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't type anything.")

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Empty input!")
else:
    words = sentence.split()
    print(f"First word: {words[0]}")

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Welcome, admin!")
    else:
        print("Wrong password")
else:
    print("Unknown user.")

age = 20
status = "adult" if age >= 18 else "minor"
print(status)

command = input("Command: ").lower()

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "help" | "?":
        print("Commands: start, stop, help")
    case _:
        print("Unknown command.")

