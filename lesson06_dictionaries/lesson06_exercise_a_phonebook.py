phonebook = {}
while True:
    print("1) Add  2) Look up  3) Delete  4) Show all  5) Quit")
    option = input("Choose an option: ").strip()

    match option:
        case "1":
            name = input("Enter name: ").strip().lower()
            if not name:
                continue
            if name in phonebook:
                answer = input("Do you wish to Overwrite phone number? (y/n)")
                if answer != "y":
                    continue
            phone_number = input("Enter phone number: ").strip()
            phonebook[name] = phone_number
        case "2":
            look_up = input("Enter a name: ").strip().lower()
            if look_up in phonebook:
                print(phonebook.get(look_up))
            else:
                print("This person doesn't exist.")
        case "3":
            name = input("Enter name: ").strip().lower()
            if name in phonebook:
                del phonebook[name]
                print("Deleted.")
            else:
                print("Not found.")
        case "4":
            for name, phone in sorted(phonebook.items()):
                print(f"{name.title()}: {phone}")
        case "5":
            break
        case _:
            print("Invalid input")


