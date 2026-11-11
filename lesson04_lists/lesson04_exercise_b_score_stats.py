text = input("Give scores separated by a comma: ") #23,12,56,34,78,45
scores = [int(s) for s in text.split(",")]

print(max(scores))
print(min(scores))
print(f"Average: {sum(scores) / len(scores):.2f}")

scores.sort(reverse=True)

print(scores)

print(f"Top 3: {scores[:3]}")
