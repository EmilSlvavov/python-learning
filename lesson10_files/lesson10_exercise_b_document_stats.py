from pathlib import Path

DOCS_FOLDER = Path(__file__).parent / "docs"


def load_documents(folder: Path) -> dict[str, str]:
    """Loads all documents or raises FileNotFoundError"""
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    else:
        files = {}
        for item in sorted(folder.glob("*")):
            if item.is_file():
                files[item.name] = item.read_text(encoding="utf-8")
        return files


def split_paragraphs(text: str) -> list[str]:
    """Splits the paragraphs and returns a list of lines"""
    return [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.split()]


def document_stats(text: str) -> dict[str, int]:
    """Returns stats for the text which should derive from a document"""
    return {"lines": len(text.splitlines()),
            "words": len(text.split()),
            "characters": len(text),
            "paragraphs": len(split_paragraphs(text))}


def search(documents: dict[str, str], word: str) -> list[str]:
    """Searches for a word in all documents and returns a list with all
    documents' names containing the word"""
    files = []
    for name, text in documents.items():
        if word.lower() in text.lower():
            files.append(name)
    return files


def show_stats_table(documents: dict[str, str]) -> None:
    """Shows the stats for each document"""
    print(f"{'File':<16}{'Lines':>6}{'Words':>7}{'Chars':>7}{'Paragraphs':>12}")
    print("-" * 48)
    for name, text in documents.items():
        stats = document_stats(text)
        print(f"{name:<16}{stats['lines']:>6}{stats['words']:>7}{stats['characters']:>7}{stats['paragraphs']:>12}")


def main() -> None:
    """Runs the main program using all other functions"""
    print("=== Document Stats ===")
    print()
    try:
        docs = load_documents(DOCS_FOLDER)
        print(f"Loaded {len(docs)} documents")
        show_stats_table(docs)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    while True:
        word = input("Search for a word (or quit): ").strip().lower()
        match word:
            case "quit":
                print("Bye!")
                return
            case "":
                print("Try again!")
                continue
            case _:
                files = search(docs, word)
                if files:
                    print(", ".join(files))
                    continue
                print("Not found.")


if __name__ == "__main__":
    main()