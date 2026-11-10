def make_message(role: str, content: str) -> dict[str, str]:
    msg = {"role": role, "content": content}
    return msg


def start_conversation(system_prompt: str) -> list[dict[str, str]]:
    return [make_message("system", system_prompt)]


def add_user_message(messages: list, text: str) -> None:
    messages.append(make_message("user", text))


def print_conversation(messages: list[dict[str, str]]) -> None:
    for msg in messages:
        print(f"[{msg['role']}] {msg['content']}")


conversation = start_conversation("You are a helpful assistant.")

while True:
    message = input("Please write a message: ")
    if message == "quit":
        break
    add_user_message(conversation, message)
    print_conversation(conversation)
