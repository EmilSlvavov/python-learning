import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from lesson15_exercise_a_config import mask

ENV_FILE = Path(__file__).parent.parent / ".env"
BEARER_URL = "https://httpbin.org/bearer"
TIMEOUT = 10

def get_api_key(env_file: Path) -> str:
    load_dotenv(env_file)
    key = os.getenv("DEMO_API_KEY")
    if not key:
        raise RuntimeError("DEMO_API_KEY is not set. Add it your .env file")
    return key

def call_protected(api_key: str | None) -> dict:
    if api_key:
        headers = {"Authorization": f"Bearer {api_key}"}
    else:
        headers = {}
    response = requests.get(BEARER_URL, headers=headers, timeout=TIMEOUT)
    if response.status_code == 401:
        raise PermissionError("401 Unauthorized: missing or invalid API key")
    response.raise_for_status()
    return response.json()

def main() -> None:
    print("=== Protected API ===")
    try:
        key = get_api_key(ENV_FILE)
    except RuntimeError as e:
        print(f"Error: {e}")
        return
    print(f"Using key: {mask(key)}")
    try:
        data = call_protected(key)
        print(f"Authenticated: {data['authenticated']}")
        print(f"Server saw token: {mask(data['token'])}")
        print("Calling without a key...")
        try:
            call_protected(None)
        except PermissionError as e:
            print(f"Error: {e}")
    except requests.RequestException as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()



