words = ["  Apple", "banana ", "", "     ", "  CHERRY  ", "", "date"]

cleaned = [word.strip().lower() for word in words if word.strip()]
print(cleaned)

length_of_cleaned = [len(word) for word in cleaned]
print(length_of_cleaned)