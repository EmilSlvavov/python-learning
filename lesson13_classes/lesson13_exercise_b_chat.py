import json
from dataclasses import dataclass, field
from pathlib import Path

CHAT_FILE = Path(__file__).parent / "chat.json"


@dataclass
class Message:
    role: str
    content: str

    def __post_init__(self):
        if self.role not in {"user", "assistant"}:
            raise ValueError(f"Invalid role: {self.role}")

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"

    def to_dict(self) -> dict:
        return {"role": self.role, "content": self.content}


@dataclass
class Conversation:
    system_prompt: str
    messages: list[Message] = field(default_factory=list)

    def add_user(self, text: str) -> None:
        self.messages.append(Message("user", text))

    def add_assistant(self, text: str) -> None:
        self.messages.append(Message("assistant", text))

    def last_message(self) -> Message | None:
        try:
            return self.messages[-1]
        except IndexError:
            return None

    def __len__(self) -> int:
        return sum(1 for message in self.messages if message.role != "system")

    def to_api_format(self) -> list[dict]:
        message_list = [message.to_dict() for message in self.messages]
        system_prompt_dict = {"role": "system", "content": self.system_prompt}
        message_list.insert(0, system_prompt_dict)
        return message_list

    def save(self, path: Path) -> None:
        data = {
            "system_prompt" : self.system_prompt,
            "messages" : [message.to_dict() for message in self.messages]
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, path: Path) -> "Conversation":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        messages = [
            Message(item["role"], item["content"])
            for item in data["messages"]
        ]

        return cls(data["system_prompt"], messages)


def main() -> None:
    print("=== Chat ===")
    conv = Conversation("You are a helpful assistant.")
    print(f"Last: {conv.last_message()}")
    conv.add_user("What is JSON?")
    conv.add_assistant("A text format for structured data.")
    conv.add_user("Thanks!")
    print(f"Messages: {len(conv)}")
    print(f"Last: {conv.last_message()}")
    print("API format:")
    for message in conv.to_api_format():
        print(f"  {message['role']}: {message['content']}")
    conv.save(CHAT_FILE)
    print("Saved to chat.json")
    loaded = Conversation.load(CHAT_FILE)
    print(f"Loaded {len(loaded)} messages")
    print(f"Same conversation: {loaded == conv}")
    try:
        Message("robot", "beep")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()