def ask(prompt: str) -> str:
    """Asks for input and returns it stripped and lowercased"""
    user_message = input(prompt).strip().lower()
    return user_message


def calculate(a: float, operator: str, b: float) -> float:
    """Takes two floats and an operator and depending on the operator
    and numbers either does the calculation or raises ValueError"""
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            raise ValueError(f"Unknown operator: {operator}")


def parse_expression(text: str) -> tuple[float, str, float]:
    """Parses from a string which contains 'number operator number'
    into float str float or raises ValueError if input is not valid"""
    holder = text.split()
    if len(holder) != 3:
        raise ValueError("Please use the format: number operator number")
    return float(holder[0]), holder[1], float(holder[2])


def main() -> None:
    """Main function of the program running it"""
    print("=== Calculator ===")
    print("Type an expression like 3 + 4, or quit to stop")
    while True:
        user_input = ask("Calc> ")
        if user_input == "quit":
            print("Bye!")
            return
        try:
            a, operator, b = parse_expression(user_input)
            result = calculate(a, operator, b)
            print(f"= {result}")
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
