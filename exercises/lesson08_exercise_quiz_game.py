import random

OPTION_LETTERS = ["a", "b", "c", "d"]
QUESTIONS_PER_GAME = 5

QUESTIONS = [
    {"question": "What is the capital of France?",
     "options": ["Paris", "Berlin", "Rome", "Madrid"], "answer": "a"},
    {"question": "Which planet is known as the Red Planet?",
     "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "b"},
    {"question": "How many legs does a spider have?",
     "options": ["6", "10", "8", "4"], "answer": "c"},
    {"question": "What does len('hello') return in Python?",
     "options": ["4", "5", "6", "An error"], "answer": "b"},
    {"question": "What is the largest ocean on Earth?",
     "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "d"},
    {"question": "Which keyword defines a function in Python?",
     "options": ["func", "function", "define", "def"], "answer": "d"},
    {"question": "At what temperature (°C) does water boil at sea level?",
     "options": ["100", "90", "110", "120"], "answer": "a"},
    {"question": "Who painted the Mona Lisa?",
     "options": ["Van Gogh", "Picasso", "Leonardo da Vinci", "Rembrandt"], "answer": "c"},
]


def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    user_message = input(prompt).strip().lower()
    return user_message


def ask_choice(prompt: str, valid: list[str]) -> str:
    """Keep asking until the answer is one of the valid choices, then return it."""
    choice = ask(prompt)
    while choice not in valid:
        print(f"Please choose one of: {', '.join(valid)}")
        choice = ask(prompt)
    return choice


def grade_for(percent: float) -> str:
    """Parses a percent to a grade"""
    if percent >= 90:
        grade = "A"
    elif percent >= 80:
        grade = "B"
    elif percent >= 70:
        grade = "C"
    elif percent >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


def show_question(number: int, total: int, question: dict) -> None:
    """Prints question with answers."""
    print()
    print(f"Question {number}/{total}: {question['question']}")
    for option, letter in zip(question["options"], OPTION_LETTERS):
        print(f"  {letter}) {option}")


def ask_question(number: int, total: int, question: dict) -> bool:
    """Decides if the answer you gave was right or not."""
    show_question(number, total, question)
    answer = ask_choice("Your answer: ", OPTION_LETTERS)
    if answer == question["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The answer was {question['answer']}) {question['options'][OPTION_LETTERS.index(question['answer'])]}")
        return False


def run_quiz(questions: list[dict], count: int) -> int:
    """Runs the quiz"""
    picked = random.sample(questions, count)
    score = 0
    for i, question in enumerate(picked, start=1):
        result = ask_question(i, count, question)
        if result:
            score += 1
    return score


def show_results(name: str, score: int, total: int) -> None:
    """Shows the results"""
    percent = score / total
    print(f"{name.title()}, you scored {score}/{total} ({percent:.0%}) - Grade: {grade_for(percent * 100)}")
    if percent == 1:
        print("Perfect score!")


def update_high_score(scores: dict[str, int], name: str, score: int) -> bool:
    """Updates the scores if they are higher than the previous one"""
    if name not in scores or score > scores[name]:
        scores[name] = score
        return True
    return False


def show_high_scores(scores: dict[str, int]) -> None:
    """Shows all high scores"""
    if not scores:
        print("No high scores yet.")
    else:
        print(f"{'Name':<10}{'Score':>5}")
        print("-" * 15)
        for name, score in sorted(scores.items(), key=lambda pair: pair[1], reverse=True):
            print(f"{name.title():<10}{score:>5}")


def main() -> None:
    """The main function of the program that runs the whole game"""
    print("=== Python Quiz ===")
    name = ask("What's your name? ")
    if not name:
        name = "player"
    print(f"Welcome {name.title()}!")
    high_scores = {}
    while True:
        print()
        print("1) Play  2) High scores  3) Change player  4) Quit")
        option = ask("Choose: ")
        match option:
            case "1":
                score = run_quiz(QUESTIONS, QUESTIONS_PER_GAME)
                show_results(name, score, QUESTIONS_PER_GAME)
                if update_high_score(high_scores, name, score):
                    print("New high score!")
            case "2":
                show_high_scores(high_scores)
            case "3":
                name = ask("What's your name? ")
                if not name:
                    name = "player"
                print(f"Welcome {name.title()}!")
            case "4":
                print(f"Bye, {name.title()}!")
                break
            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()
