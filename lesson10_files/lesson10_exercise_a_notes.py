from pathlib import Path

NOTES_FILE = Path(__file__).parent / "data" / "notes.txt"


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


def add_note(path: Path, text: str) -> None:
    """Adds note"""
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{text} \n")


def read_notes(path: Path) -> list[str]:
    """Reads all notes or returns [] if file doesn't exist"""
    try:
        text = path.read_text(encoding="utf-8")
        return [line.strip() for line in text.splitlines() if line.strip()]
    except FileNotFoundError:
        return []


def show_notes(notes: list[str]) -> None:
    """Shows all notes or No notes yet.
    depending on if there are notes or not"""
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")


def delete_note(path: Path, number: int) -> str:
    """Deletes a note and returns it"""
    lines = read_notes(path)
    note = lines.pop(number - 1)
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")
    return note


def main() -> None:
    """Runs the main program using all other functions"""
    print("=== Notes ===")
    while True:
        print()
        print("1) Add note  2) Show notes  3) Delete note  4) Quit")
        option = input("Choose: ")

        match option:
            case "1":
                text = input("Note: ").strip()
                if not text:
                    print("Empty note, skipped.")
                    continue
                add_note(NOTES_FILE, text)
            case "2":
                show_notes(read_notes(NOTES_FILE))
            case "3":
                if notes := read_notes(NOTES_FILE):
                    show_notes(notes)
                    note_to_delete = ask_int("Number to delete: ", 1, len(notes))
                    deleted = delete_note(NOTES_FILE, note_to_delete)
                    print(f"Deleted: {deleted}")
            case "4":
                print("Bye!")
                break
            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()
