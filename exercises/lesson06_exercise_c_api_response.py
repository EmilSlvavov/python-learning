response = {
    "model": "gpt-demo",
    "output": [
        {"type": "message", "role": "assistant",
         "content": [{"type": "text", "text": "Paris is the capital of France."}]}
    ],
    "usage": {"input_tokens": 15, "output_tokens": 8, "total_tokens": 23},
}

print(response["model"])
print(response["output"][0]["content"][0]["text"])
print(f"Tokens used: {response['usage']['total_tokens']} ({response['usage']['input_tokens']} in, {response['usage']['output_tokens']} out)")
print(response.get("error", "No error"))
