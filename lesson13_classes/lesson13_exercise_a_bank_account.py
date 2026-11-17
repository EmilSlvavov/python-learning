class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = float(balance)
        self.owner = owner
        self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self.history.append(f"deposit {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.history.append(f"withdraw {amount:.2f}")

    def transfer(self, other: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self) -> str:
        return f"{self.owner}: {self._balance:.2f}"


def main() -> None:
    print("=== Bank ===")
    ana = BankAccount("Ana", 100)
    bob = BankAccount("Bob")
    print(ana)
    print(bob)
    ana.deposit(50)
    ana.withdraw(30)
    ana.transfer(bob, 20)
    print(ana)
    print(bob)
    try:
        ana.withdraw(500)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        ana.deposit(-5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        BankAccount("Zed", -10)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        ana.balance = 1000
    except AttributeError:
        print("Error: balance is read-only")
    print(f"Ana's balance: {ana.balance}")
    print("Ana's history: ")
    for transaction in ana.history:
        print(f"  {transaction}")

if __name__ == "__main__":
    main()