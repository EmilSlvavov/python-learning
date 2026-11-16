# Lesson 11: JSON
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Running this file creates a "data" folder next to it with a few small .json files.

import json
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)


# ============================================================
# 1. Python data -> JSON text (dumps = "dump string")
# ============================================================

person = {
    "name": "Ana",
    "age": 28,
    "is_student": False,
    "languages": ["Python", "Java"],
    "manager": None,
}

text = json.dumps(person)
print(text)          # {"name": "Ana", "age": 28, "is_student": false, "languages": ["Python", "Java"], "manager": null}
print(type(text))    # <class 'str'>  <- it's just a string now


# ============================================================
# 2. JSON text -> Python data (loads = "load string")
# ============================================================

raw = '{"name": "Bob", "age": 35, "is_student": true, "languages": [], "manager": null}'

data = json.loads(raw)
print(data)               # {'name': 'Bob', 'age': 35, 'is_student': True, 'languages': [], 'manager': None}
print(type(data))         # <class 'dict'>
print(data["name"])       # Bob
print(data["is_student"]) # True   <- JSON true became Python True


# ============================================================
# 3. Making it readable: indent, sort_keys, ensure_ascii
# ============================================================

print(json.dumps(person, indent=2))
# {
#   "name": "Ana",
#   "age": 28,
#   ...
# }

print(json.dumps(person, indent=2, sort_keys=True))   # keys in alphabetical order

city = {"city": "София"}
print(json.dumps(city))                       # {"city": "София"}  <- escaped
print(json.dumps(city, ensure_ascii=False))   # {"city": "София"}                          <- readable


# ============================================================
# 4. Writing and reading JSON FILES (dump / load, no "s")
# ============================================================

settings = {"theme": "dark", "font_size": 14, "recent_files": ["a.txt", "b.txt"]}
settings_path = DATA / "settings.json"

with open(settings_path, "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2, ensure_ascii=False)

with open(settings_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)                       # {'theme': 'dark', 'font_size': 14, 'recent_files': ['a.txt', 'b.txt']}
print(loaded == settings)           # True

# pathlib shortcut: combine json.dumps/json.loads with write_text/read_text
settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
loaded = json.loads(settings_path.read_text(encoding="utf-8"))
print(loaded["theme"])              # dark


# ============================================================
# 5. Type gotchas: what changes on the round trip
# ============================================================

before = {"point": (3, 4), 1: "one", "ok": True, "nothing": None}
after = json.loads(json.dumps(before))
print(after)    # {'point': [3, 4], '1': 'one', 'ok': True, 'nothing': None}
# - tuple (3, 4) came back as a LIST [3, 4]   (JSON has no tuples)
# - key 1 came back as the STRING '1'         (JSON keys are always strings)

print(after["1"])        # one
# print(after[1])        # ❌ KeyError: 1  (the key is now the string "1")

# Some types can't be turned into JSON at all:
# json.dumps({"tags": {"a", "b"}})    # ❌ TypeError: Object of type set is not JSON serializable

tags = {"python", "ai"}
print(json.dumps({"tags": sorted(tags)}))    # {"tags": ["ai", "python"]}  <- convert the set to a list first


# ============================================================
# 6. When things go wrong: missing file, broken JSON
# ============================================================

# json.loads('{"name": "Ana",}')     # ❌ json.JSONDecodeError (trailing comma is not allowed in JSON)
# json.loads("{'name': 'Ana'}")      # ❌ json.JSONDecodeError (JSON needs DOUBLE quotes)

try:
    json.loads('{"name": "Ana",}')
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")      # Invalid JSON: Illegal trailing comma before end of object: line 1 column 15 (char 14)


def load_json(path: Path, default):
    """Loads JSON from path, or returns default if the file doesn't exist."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


print(load_json(DATA / "missing.json", {}))     # {}
print(load_json(settings_path, {}))             # {'theme': 'dark', ...}


# ============================================================
# 7. The load -> change -> save pattern (persistent data)
# ============================================================

scores_path = DATA / "high_scores.json"

scores = load_json(scores_path, {})         # 1. load (or start empty)
scores["ana"] = max(scores.get("ana", 0), 4)  # 2. change it in memory
scores["bob"] = max(scores.get("bob", 0), 3)

with open(scores_path, "w", encoding="utf-8") as f:   # 3. save everything back
    json.dump(scores, f, indent=2)

print(load_json(scores_path, {}))    # {'ana': 4, 'bob': 3}  <- survives a restart


# ============================================================
# 8. API-shaped data: digging into nested JSON
# ============================================================

response_text = """
{
  "id": "resp_123",
  "status": "completed",
  "output": [
    {
      "type": "message",
      "role": "assistant",
      "content": [
        {"type": "output_text", "text": "Hello! How can I help?"}
      ]
    }
  ],
  "usage": {"input_tokens": 10, "output_tokens": 6, "total_tokens": 16},
  "error": null
}
"""

response = json.loads(response_text)

print(response["status"])                              # completed
print(response["output"][0]["content"][0]["text"])     # Hello! How can I help?
print(response["usage"]["total_tokens"])               # 16

# Safer access with .get() and defaults
print(response.get("metadata", {}))                    # {}  (key doesn't exist)

# "error": null exists but is None -> .get("error", {}) returns None, not {}
error = response.get("error") or {}                    # None or {}  ->  {}
print(error.get("message", "no error"))                # no error


# ============================================================
# 9. Lists of records: saving a conversation
# ============================================================

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is JSON?"},
    {"role": "assistant", "content": "A text format for structured data."},
]

chat_path = DATA / "conversation.json"
with open(chat_path, "w", encoding="utf-8") as f:
    json.dump(messages, f, indent=2, ensure_ascii=False)

with open(chat_path, "r", encoding="utf-8") as f:
    restored = json.load(f)

for message in restored:
    print(f"{message['role']:>9}: {message['content']}")
#    system: You are a helpful assistant.
#      user: What is JSON?
# assistant: A text format for structured data.


# ============================================================
# 10. JSON Lines (.jsonl): one JSON object per line
# ============================================================

chunks = [
    {"id": 1, "source": "cats.txt", "text": "Cats are small, independent animals."},
    {"id": 2, "source": "dogs.txt", "text": "Dogs are loyal and social animals."},
]

jsonl_path = DATA / "chunks.jsonl"
with open(jsonl_path, "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

with open(jsonl_path, "r", encoding="utf-8") as f:
    for line in f:
        chunk = json.loads(line)
        print(chunk["id"], chunk["source"])
# 1 cats.txt
# 2 dogs.txt


# ============================================================
# 11. Debugging tip: pretty-print anything
# ============================================================

print(json.dumps(response, indent=2))    # see the whole structure at a glance
