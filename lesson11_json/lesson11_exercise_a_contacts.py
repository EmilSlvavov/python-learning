import json
from pathlib import Path

CONTACTS_FILE = Path(__file__).parent / "contacts.json"


def load_contacts(path: Path) -> dict[str, dict[str, str]]:
    """Loads all contacts from a file"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_contacts(path: Path, contacts: dict) -> None:
    """Saves contacts into a file"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def add_contact(contacts: dict, name: str, phone: str, email: str) -> None:
    """Adds a contact into a dictionary"""
    contacts[name.lower()] = {"phone": phone, "email": email}


def delete_contact(contacts: dict, name: str) -> bool:
    """Deletes a contact and returns boolean"""
    if name.lower() in contacts:
        del contacts[name.lower()]
        return True
    return False


def show_contacts(contacts: dict[str, dict[str, str]]) -> None:
    """Prints all contacts if there are existing ones"""
    if not contacts:
        print("No contacts yet.")
    else:
        for name, info in sorted(contacts.items()):
            print(f"{name.title():<12}{info['phone']:<14}{info['email']}")


def main() -> None:
    """Main function of the program"""
    print("=== Contacts ===")
    try:
        contacts = load_contacts(CONTACTS_FILE)
    except json.JSONDecodeError:
        print("Error: contacts.json is not valid JSON.")
        return
    while True:
        print()
        print("1) Add  2) Show  3) Delete  4) Quit")
        choice = input("Choose: ").strip()
        match choice:
            case "1":
                name = input("Name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                else:
                    phone = input("Phone: ").strip()
                    email = input("Email: ").strip()
                    if not phone or not email:
                        print("Cannot add empty details.")
                    else:
                        add_contact(contacts, name, phone, email)
                        save_contacts(CONTACTS_FILE, contacts)
            case "2":
                show_contacts(contacts)
            case "3":
                if contacts:
                    name = input("Name to delete: ").strip()
                    deleted = delete_contact(contacts, name)
                    if deleted:
                        save_contacts(CONTACTS_FILE, contacts)
                        print(f"Deleted: {name}")
                else:
                    print("No contacts yet.")
            case "4":
                print("Bye!")
                break
            case _:
                print("Invalid input!")


if __name__ == "__main__":
    main()
