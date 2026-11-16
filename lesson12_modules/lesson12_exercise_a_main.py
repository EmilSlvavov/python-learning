from pathlib import Path

import lesson12_exercise_a_text_utils as tu

DOCS_FOLDER = Path(__file__).parent.parent / "lesson10_files" / "docs"

def main() -> None:
    """Main function of the program"""
    print("=== Top Words ===")
    for file in sorted(DOCS_FOLDER.glob("*.txt")):
        text = file.read_text(encoding="utf-8")
        print(f"{file.name}: {tu.word_count(text)} words")
        for word, count in tu.top_words(text, 3):
            print(f"  {word}: {count}")
        print()


if __name__ == "__main__":
    main()