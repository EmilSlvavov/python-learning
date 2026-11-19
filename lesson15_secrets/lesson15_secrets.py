# Lesson 15: Secrets, environment variables and .env files
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Terminal commands are shown as comments: run them in PyCharm's Terminal, not here.
# Sections 4+ need python-dotenv (you install it in exercise A). Until then they print a hint.
# Running this file creates "demo.env" next to it with FAKE values only.

import os
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent


# ============================================================
# 1. Why: never write a key in your code
# ============================================================

# ❌ NEVER do this:
# api_key = "sk-proj-abc123..."
#
# - git keeps it in the history FOREVER, even if you delete the line later
# - bots scan GitHub for keys within minutes and spend your money
# - you can't share or publish your code without leaking it


# ============================================================
# 2. Environment variables: settings that live OUTSIDE the code
# ============================================================

print(os.environ["PATH"][:40])      # C:\...   <- every program gets a set of environment variables
print(os.getenv("USERNAME"))        # your Windows user name
print(os.getenv("NOT_SET_ANYWHERE"))            # None   <- missing -> None (no crash)
print(os.getenv("NOT_SET_ANYWHERE", "default")) # default

# print(os.environ["NOT_SET_ANYWHERE"])   # ❌ KeyError: 'NOT_SET_ANYWHERE'

# Setting one for THIS program only (the change disappears when it ends):
os.environ["LESSON_MODE"] = "demo"
print(os.getenv("LESSON_MODE"))     # demo

# Setting them outside Python (TERMINAL, PowerShell):
#   $env:MY_SETTING = "hello"        only for this terminal window
#   python my_script.py              -> os.getenv("MY_SETTING") == "hello"
#
# Or in PyCharm: Run -> Edit Configurations -> Environment variables


# ============================================================
# 3. Environment variables are ALWAYS strings
# ============================================================

os.environ["MAX_RETRIES"] = "3"
os.environ["DEBUG"] = "false"

retries = os.getenv("MAX_RETRIES")
print(type(retries), retries)        # <class 'str'> 3
print(int(retries) + 1)              # 4   <- convert it yourself

print(bool(os.getenv("DEBUG")))      # True  ❗ any non-empty string is truthy, even "false"
print(os.getenv("DEBUG").lower() in {"true", "1", "yes", "on"})   # False  <- the correct way


# ============================================================
# 4. .env files and python-dotenv
# ============================================================

# A .env file is a plain text file with KEY=value lines.
# python-dotenv reads it and puts the values into os.environ.

demo_env = HERE / "demo.env"
demo_env.write_text(
    "# lines starting with # are comments\n"
    "APP_NAME=Demo App\n"
    "DEMO_TOKEN=sk-fake-0000111122223333\n"
    "TIMEOUT=15\n",
    encoding="utf-8",
)

try:
    from dotenv import load_dotenv, dotenv_values

    load_dotenv(demo_env)                  # reads the file into os.environ
    print(os.getenv("APP_NAME"))           # Demo App
    print(os.getenv("TIMEOUT"))            # 15   (still a string!)

    # load_dotenv() with no argument looks for a file named ".env"
    # in the current folder and the folders above it.

    # It does NOT overwrite variables that already exist:
    os.environ["APP_NAME"] = "Set Before"
    load_dotenv(demo_env)
    print(os.getenv("APP_NAME"))           # Set Before
    load_dotenv(demo_env, override=True)   # ...unless you ask it to
    print(os.getenv("APP_NAME"))           # Demo App

    # Read the file into a dict WITHOUT touching os.environ:
    values = dotenv_values(demo_env)
    print(values)    # OrderedDict({'APP_NAME': 'Demo App', 'DEMO_TOKEN': 'sk-fake-...', 'TIMEOUT': '15'})  (a dict)

except ModuleNotFoundError:
    print("python-dotenv is not installed yet. Run: python -m pip install python-dotenv")


# ============================================================
# 5. Keep .env out of git: .gitignore
# ============================================================

# .gitignore is a text file in the project root. Every line is a pattern git will ignore:
#
#   .env
#   __pycache__/
#   *.pyc
#
# Check it works (TERMINAL):
#   git check-ignore -v .env     -> prints the .gitignore line that ignores it
#   git status                   -> .env must NOT be listed
#
# If a file was already added to git BEFORE you ignored it, git keeps tracking it.
# Stop tracking it (the file stays on your disk):
#   git rm --cached .env
#   git rm -r --cached lesson10_files/__pycache__


# ============================================================
# 6. .env.example: the template you DO commit
# ============================================================

# .env           real values, ignored by git, only on your machine
# .env.example   same keys, fake values, committed so others know what to fill in
#
#   APP_NAME=Python Learning
#   DEMO_API_KEY=your-key-here


# ============================================================
# 7. Never print a whole secret: mask it
# ============================================================

def mask(secret: str) -> str:
    """Shows only the start and the end of a secret."""
    if len(secret) < 8:
        return "****"
    return f"{secret[:4]}...{secret[-4:]}"


print(mask("sk-fake-0000111122223333"))    # sk-f...3333
print(mask("short"))                       # ****


# ============================================================
# 8. Fail fast: check required settings at startup
# ============================================================

def require(name: str) -> str:
    """Returns the environment variable, or raises a clear error if it's missing."""
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Missing required setting: {name}")
    return value


try:
    require("SOMETHING_I_FORGOT")
except RuntimeError as e:
    print(e)                               # Missing required setting: SOMETHING_I_FORGOT

# Much better than a confusing 401 error from an API ten minutes into the program.


# ============================================================
# 9. One config object, loaded once
# ============================================================

@dataclass
class Settings:
    app_name: str
    timeout: int
    token: str


def load_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "Unnamed App"),   # optional, with a default
        timeout=int(os.getenv("TIMEOUT", "10")),         # optional, converted to int
        token=require("DEMO_TOKEN"),                     # required
    )


try:
    settings = load_settings()
    print(settings.app_name, settings.timeout, mask(settings.token))   # Demo App 15 sk-f...3333
except RuntimeError as e:
    print(f"Config error: {e}")   # what you see BEFORE installing python-dotenv (demo.env was never loaded)


# ============================================================
# 10. If a key ever leaks
# ============================================================

# 1. Revoke it IMMEDIATELY in the provider's dashboard (OpenAI: API keys page -> delete).
# 2. Create a new key and put it in .env.
# 3. Deleting the commit is NOT enough: assume anyone may already have copied it.


# ============================================================
# 11. Preview: the openai library reads OPENAI_API_KEY by itself
# ============================================================

# .env:
#   OPENAI_API_KEY=sk-proj-...
#
# Python (Lesson 17):
#   from dotenv import load_dotenv
#   from openai import OpenAI
#
#   load_dotenv()
#   client = OpenAI()      # finds OPENAI_API_KEY in os.environ automatically
