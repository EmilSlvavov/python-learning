# A small module used by lesson12_modules.py.
# A module is just a .py file: everything defined here can be imported elsewhere.

import math

print(f"[lesson12_shapes] loading, __name__ = {__name__!r}")   # shows what __name__ is

DEFAULT_PRECISION = 2


def circle_area(radius: float) -> float:
    """Returns the area of a circle, rounded to DEFAULT_PRECISION."""
    return round(math.pi * radius ** 2, DEFAULT_PRECISION)


def rectangle_area(width: float, height: float) -> float:
    """Returns the area of a rectangle."""
    return width * height


def _helper() -> str:
    """The leading underscore means "internal, please don't use from outside"."""
    return "internal"


if __name__ == "__main__":
    # Runs ONLY when you run this file directly (green arrow on THIS file),
    # NOT when another file does "import lesson12_shapes".
    print("Self-test:")
    print(circle_area(1))         # 3.14
    print(rectangle_area(2, 3))   # 6
