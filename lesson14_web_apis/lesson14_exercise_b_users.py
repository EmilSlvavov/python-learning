from dataclasses import dataclass

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


@dataclass
class User:
    id: int
    name: str
    email: str
    city: str

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(data["id"], data["name"], data["email"], data["address"]["city"])


def get_users() -> list[User]:
    response = requests.get(f"{BASE_URL}/users", timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    return [User.from_dict(user) for user in data]


def get_user(user_id: int) -> User | None:
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=TIMEOUT)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    data = response.json()
    return User.from_dict(data)


def count_completed(user_id: int) -> tuple[int, int]:
    response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id}, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    counter = 0
    for entry in data:
        if entry["completed"]:
            counter += 1
    return counter, len(data)


def create_todo(user_id: int, title: str) -> dict:
    response = requests.post(f"{BASE_URL}/todos", json={"userId": user_id, "title": title, "completed": False}, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def main() -> None:
    print("=== Users ===")
    try:
        users = get_users()
        print(f"{'ID':<4}{'Name':<26}{'City':<16}{'Done':>6}")
        print("-" * 52)
        for user in users:
            done, total = count_completed(user.id)
            done_text = f"{done}/{total}"
            print(f"{user.id:<4}{user.name:<26}{user.city:<16}{done_text:>6}")
        print()
        for user_id in [3, 999]:
            test_user = get_user(user_id)
            if test_user:
                print(f"User {test_user.id}: {test_user.name} ({test_user.email})")
            else:
                print(f"User {user_id}: not found")
        todo = create_todo(1, "Learn the requests library")
        print(f"Created todo {todo['id']}: {todo['title']}")
    except requests.RequestException as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    main()
