def average(numbers: list[int]) -> float:
    """Return the average of the numbers."""
    total = 0
    for i in range(0, len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def count_passed(scores: dict[str, int], pass_mark: int) -> int:
    """Return how many students scored at least pass_mark."""
    passed = 0
    for name, score in scores.items():
        if score >= pass_mark:
            passed += 1
    return passed


def best_student(scores: dict[str, int]) -> str:
    """Return the name of the student with the highest score."""
    best_name = ""
    best_score = 0
    for name, score in scores.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name


scores = {"alex": 72, "sam": 60, "jo": 91, "kim": 55}
print(average(list(scores.values())))   # expected: 69.5
print(count_passed(scores, 60))         # expected: 3   (60 counts as passing)
print(best_student(scores))             # expected: jo