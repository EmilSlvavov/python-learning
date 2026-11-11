def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    user_message = input(prompt).strip().lower()
    return user_message


def add_contact(book: dict[str, str]) -> None:
    name = ask("Enter name: ")
    if not name:
        return
    if name in book:
        answer = ask("Do you wish to Overwrite phone number? (y/n)")
        if answer != "y":
            return
    phone_number = ask("Enter phone number: ")
    book[name] = phone_number


def look_up(book: dict[str, str]) -> None:
    search = ask("Enter name: ")
    if search in book:
        print(book.get(search))
    else:
        print("This person doesn't exist.")


def delete_contact(book: dict[str, str]) -> None:
    name = ask("Enter name: ")
    if name in book:
        del book[name]
        print("Deleted.")
    else:
        print("Not found.")


def show_all(book: dict[str, str]) -> None:
    for name, phone in sorted(book.items()):
        print(f"{name.title()}: {phone}")


phonebook = {}
while True:
    print("1) Add  2) Look up  3) Delete  4) Show all  5) Quit")
    option = input("Choose an option: ").strip()

    match option:
        case "1":
            add_contact(phonebook)
        case "2":
            look_up(phonebook)
        case "3":
            delete_contact(phonebook)
        case "4":
            show_all(phonebook)
        case "5":
            break
        case _:
            print("Invalid input")