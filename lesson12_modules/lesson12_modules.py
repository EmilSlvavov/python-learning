# Lesson 12: Modules, packages, pip and virtual environments
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Terminal commands (pip, venv) are shown as comments: run them in PyCharm's Terminal, not here.
# This file imports lesson12_shapes.py and the lesson12_package folder next to it.


# ============================================================
# 1. A module is just a .py file
# ============================================================

import lesson12_shapes                      # runs lesson12_shapes.py once, top to bottom
# prints: [lesson12_shapes] loading, __name__ = 'lesson12_shapes'

print(lesson12_shapes.circle_area(2))       # 12.57
print(lesson12_shapes.rectangle_area(3, 4)) # 12
print(lesson12_shapes.DEFAULT_PRECISION)    # 2

import lesson12_shapes                      # second import: NOTHING printed, modules load only once


# ============================================================
# 2. Different ways to import
# ============================================================

import lesson12_shapes as shapes            # alias: shorter name
print(shapes.circle_area(1))                # 3.14

from lesson12_shapes import circle_area, rectangle_area   # pull names in directly
print(circle_area(1))                       # 3.14  (no "shapes." prefix needed)

from lesson12_shapes import circle_area as area   # alias for a single name
print(area(3))                              # 28.27

# from lesson12_shapes import *             # works, but AVOID: you can't see where names come from

print(shapes._helper())                     # internal  <- works, but the _ says "please don't"


# ============================================================
# 3. __name__: "am I being run, or imported?"
# ============================================================

print(__name__)              # __main__   <- this file was run directly
print(shapes.__name__)       # lesson12_shapes   <- that file was imported

# That's why every program ends with:
#
# if __name__ == "__main__":
#     main()
#
# Run directly -> main() starts. Imported -> only the functions are defined, nothing runs.
# (Run lesson12_shapes.py on its own and you'll see its "Self-test:" lines; here you don't.)


# ============================================================
# 4. The standard library: modules that come with Python
# ============================================================

import math
print(math.sqrt(16))         # 4.0
print(math.ceil(2.1))        # 3
print(math.pi)               # 3.141592653589793

from datetime import date, datetime, timedelta
today = date.today()
print(today)                             # e.g. 2026-11-16
print(today + timedelta(days=7))         # one week later
print(datetime.now().strftime("%H:%M"))  # e.g. 14:05

from collections import Counter
words = "the cat and the dog and the bird".split()
counts = Counter(words)
print(counts)                    # Counter({'the': 3, 'and': 2, 'cat': 1, 'dog': 1, 'bird': 1})
print(counts["the"])             # 3
print(counts["fish"])            # 0   <- no KeyError for missing words
print(counts.most_common(2))     # [('the', 3), ('and', 2)]   <- list of (word, count) tuples

import statistics
print(statistics.mean([2, 4, 9]))     # 5
print(statistics.median([2, 4, 9]))   # 4

import sys
print(sys.version)               # 3.15.2 (tags/...) ...
print(sys.version_info.major)    # 3


# ============================================================
# 5. Packages: a folder of modules
# ============================================================

# lesson12_modules/
#     lesson12_package/
#         __init__.py          <- marks the folder as a package (can be empty)
#         text_helpers.py

from lesson12_package import text_helpers
print(text_helpers.shout("hello"))       # HELLO!

from lesson12_package.text_helpers import whisper
print(whisper("HELLO"))                  # hello...


# ============================================================
# 6. Where Python looks for modules (and a classic trap)
# ============================================================

for folder in sys.path[:3]:
    print(folder)        # FIRST: the folder of the script you ran, then the standard library...

# ❌ Trap: never name your own file like a module you use.
# A file called json.py or random.py in your folder is found FIRST,
# so "import json" would import YOUR file and json.dumps would "not exist".

# import this_module_does_not_exist      # ❌ ModuleNotFoundError: No module named '...'


# ============================================================
# 7. Third-party packages (installed with pip)
# ============================================================

try:
    import requests                      # NOT part of Python, must be installed
    print(f"requests {requests.__version__} is installed")
except ModuleNotFoundError:
    print("requests is not installed yet. Run: python -m pip install requests")

# Asking for a package's version WITHOUT importing it:
from importlib.metadata import version, PackageNotFoundError

print(version("pip"))                    # e.g. 26.0.1
try:
    print(version("requests"))
except PackageNotFoundError:
    print("requests: not installed")


# ============================================================
# 8. Virtual environments: am I inside one?
# ============================================================

print(sys.executable)                    # ...\python-learning\.venv\Scripts\python.exe
print(sys.prefix)                        # ...\python-learning\.venv   (the active environment)
print(sys.base_prefix)                   # ...\pythoncore-3.15-64      (the "real" Python install)
print(sys.prefix != sys.base_prefix)     # True  -> running inside a venv


# ============================================================
# 9. pip and requirements.txt (TERMINAL commands, not Python)
# ============================================================

# In PyCharm: View -> Tool Windows -> Terminal. The prompt should start with (.venv).
#
# python -m pip install requests          install a package (from PyPI, like Maven Central)
# python -m pip install requests==2.32.3  install an exact version
# python -m pip list                      everything installed in this venv
# python -m pip show requests             details: version, location, dependencies
# python -m pip uninstall requests        remove it
#
# python -m pip freeze > requirements.txt     save exact versions (like dependencies in pom.xml)
# python -m pip install -r requirements.txt   install everything listed (e.g. on a new machine)
#
# Making a venv by hand (PyCharm already did this for you):
# python -m venv .venv
# .venv\Scripts\activate                  (Windows; the prompt then shows (.venv))
# deactivate
