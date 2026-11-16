import json
from pathlib import Path

RESPONSES_FILE = Path(__file__).parent / "api_responses.json"
SUMMARY_FILE = Path(__file__).parent / "summary.json"


def load_responses(path: Path) -> list[dict]:
    """Loads all responses"""
    return json.loads(path.read_text(encoding="utf-8"))


def get_text(response: dict) -> str:
    """Gets text from a response and returns it"""
    if response["status"] != "completed":
        return ""
    return response["output"][0]["content"][0]["text"]


def get_error(response: dict) -> str:
    """Gets error from a response if it exists"""
    error = response.get("error") or {}
    return error.get("message", "")


def get_total_tokens(response: dict) -> int:
    """Returns total tokens for a response"""
    return response.get("usage", {}).get("total_tokens", 0)


def summarize(responses: list[dict]) -> dict[str, int]:
    """Summarizes stats of a response and returns it"""
    completed = 0
    total_tokens = 0
    for response in responses:
        if response["status"] == "completed":
            completed += 1
        total_tokens += get_total_tokens(response)
    return {"count": len(responses), "completed": completed, "total_tokens": total_tokens}


def save_summary(path: Path, summary: dict) -> None:
    """Saves a summary of a response to a file"""
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

def main():
    """Main function of the program"""
    print("=== API Responses ===")
    try:
        responses = load_responses(RESPONSES_FILE)
    except FileNotFoundError:
        print("Error: api_responses.json not found.")
        return
    except json.JSONDecodeError:
        print("Error: api_responses.json is not valid JSON")
        return
    print(f"Loaded {len(responses)} responses.")
    print()
    for response in responses:
        if text:= get_text(response):
            shown = text
        else:
            shown = f"Error: {get_error(response)}"
        tokens = get_total_tokens(response)
        print(f"{response['id']} [{response['status']}] {shown} ({tokens} tokens)")
    print()
    summary = summarize(responses)
    print(f"Summary: {summary['count']} responses, {summary['completed']} completed, {summary['total_tokens']} tokens")
    save_summary(SUMMARY_FILE, summary)
    print("Summary saved to summary.json")


if __name__ == "__main__":
    main()