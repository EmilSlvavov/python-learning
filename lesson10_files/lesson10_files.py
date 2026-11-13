# Lesson 10: Working with files
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Running this file creates a "data" folder next to it with a few small text files.

from pathlib import Path


# ============================================================
# 1. Paths: where is the file?
# ============================================================

HERE = Path(__file__).parent        # the folder this .py file is in
DATA = HERE / "data"                # "/" joins path parts (works on Windows too)

print(HERE)                  # C:\Users\...\python-learning\lesson10_files
print(DATA / "notes.txt")    # C:\Users\...\python-learning\lesson10_files\data\notes.txt

print(Path.cwd())            # the current working directory (where relative paths start)


# ============================================================
# 2. Creating a folder
# ============================================================

DATA.mkdir(exist_ok=True)    # create it; no error if it already exists
print(DATA.exists())         # True


# ============================================================
# 3. Writing a file
# ============================================================

notes_path = DATA / "notes.txt"

with open(notes_path, "w", encoding="utf-8") as f:
    f.write("Buy milk\n")
    f.write("Learn Python\n")
    f.write("Call Sam\n")

# "w" creates the file, or EMPTIES it first if it already exists
# The file is closed automatically when the "with" block ends


# ============================================================
# 4. Reading a file
# ============================================================

# The whole file as one string
with open(notes_path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)
# Buy milk
# Learn Python
# Call Sam

print(repr(content))    # 'Buy milk\nLearn Python\nCall Sam\n'  ← repr shows the hidden \n

# Line by line (best for big files: only one line in memory at a time)
with open(notes_path, "r", encoding="utf-8") as f:
    for line in f:
        print(f"[{line.rstrip()}]")    # rstrip removes the "\n" at the end of each line
# [Buy milk]
# [Learn Python]
# [Call Sam]

# As a list of lines, without the "\n"
with open(notes_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
print(lines)            # ['Buy milk', 'Learn Python', 'Call Sam']


# ============================================================
# 5. Appending to a file
# ============================================================

with open(notes_path, "a", encoding="utf-8") as f:
    f.write("Water the plants\n")     # added to the END, nothing is deleted

with open(notes_path, "r", encoding="utf-8") as f:
    print(f.read().splitlines())      # ['Buy milk', 'Learn Python', 'Call Sam', 'Water the plants']

# Writing a list of lines in one go
tasks = ["Wash dishes", "Read a book"]
with open(DATA / "tasks.txt", "w", encoding="utf-8") as f:
    for task in tasks:
        f.write(task + "\n")


# ============================================================
# 6. pathlib shortcuts
# ============================================================

hello_path = DATA / "hello.txt"
hello_path.write_text("Hello, files!\n", encoding="utf-8")    # open + write + close in one line
print(hello_path.read_text(encoding="utf-8"))                  # open + read + close in one line

print(hello_path.exists())       # True
print(hello_path.is_file())      # True
print(DATA.is_dir())             # True
print(hello_path.name)           # hello.txt
print(hello_path.stem)           # hello
print(hello_path.suffix)         # .txt
print(hello_path.parent.name)    # data
print(hello_path.stat().st_size) # size in bytes, e.g. 15 (Windows may count \r\n as 2)


# ============================================================
# 7. Listing files in a folder
# ============================================================

for path in DATA.iterdir():                 # everything in the folder
    print(path.name)

for path in sorted(DATA.glob("*.txt")):     # only .txt files, sorted by name
    print(path.name)

all_python_files = list(HERE.parent.rglob("*.py"))   # rglob also searches subfolders
print(len(all_python_files) > 0)                     # True


# ============================================================
# 8. When the file isn't there
# ============================================================

# open(DATA / "missing.txt", "r", encoding="utf-8")   # ❌ FileNotFoundError

try:
    with open(DATA / "missing.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No such file yet.")

missing = DATA / "missing.txt"
if missing.exists():
    print(missing.read_text(encoding="utf-8"))
else:
    print("No such file yet.")


# ============================================================
# 9. Always say encoding="utf-8"
# ============================================================

greeting_path = DATA / "greeting.txt"
greeting_path.write_text("Здравей, свят! ✓\n", encoding="utf-8")
print(greeting_path.read_text(encoding="utf-8"))     # Здравей, свят! ✓

# Reading it with the wrong encoding garbles the text:
print(greeting_path.read_text(encoding="cp1252", errors="replace"))   # Ð—Ð´Ñ€Ð°Ð²... (garbage)


# ============================================================
# 10. Processing a document (a RAG preview)
# ============================================================

article = """Python is a popular programming language.
It is known for its simple syntax.

Python is used for web development, data science and AI.
Many AI libraries are written for Python.

Learning Python is a good first step into AI."""

article_path = DATA / "article.txt"
article_path.write_text(article, encoding="utf-8")

text = article_path.read_text(encoding="utf-8")
paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

print(f"Lines: {len(text.splitlines())}")    # Lines: 7
print(f"Words: {len(text.split())}")         # Words: 39
print(f"Paragraphs: {len(paragraphs)}")      # Paragraphs: 3

for i, paragraph in enumerate(paragraphs, start=1):
    print(f"--- Chunk {i} ---")
    print(paragraph)


# ============================================================
# 11. Deleting a file
# ============================================================

temp_path = DATA / "temp.txt"
temp_path.write_text("delete me", encoding="utf-8")
temp_path.unlink()                       # delete it
print(temp_path.exists())                # False
temp_path.unlink(missing_ok=True)        # no error even though it's already gone
