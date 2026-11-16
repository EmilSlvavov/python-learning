import sys
from importlib.metadata import version, PackageNotFoundError

def get_python_version() -> str:
    """Returns python version"""
    python_version = sys.version_info
    return f"{python_version.major}.{python_version.minor}.{python_version.micro}"

def in_virtualenv() -> bool:
    """Returns true if we are in virtual env and false if we arent"""
    return sys.prefix != sys.base_prefix

def get_package_version(name: str) -> str | None:
    """Returns package version of the package or None if it doesn't exist on the machine"""
    try:
        return version(name)
    except PackageNotFoundError:
        return None

def main() -> None:
    """Main function of the program"""
    print("=== Environment ===")
    print(f"Python: {get_python_version()}")
    if in_virtualenv():
        print(f"Virtual env: yes ({sys.prefix})")
    else:
        print("Virtual env: NO - packages will install globally!")
    for name in ["pip", "requests"]:
        if v:= get_package_version(name):
            print(f"{name}: {v}")
        else:
            print(f"{name}: not installed (run: python -m pip install {name})")

if __name__ == "__main__":
    main()