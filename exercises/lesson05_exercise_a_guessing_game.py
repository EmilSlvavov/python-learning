import random

secret = random.randint(1, 100)

attempts = 0
while True:
    if attempts == 10:
        break
    guess = input("Guess the number: ").strip().lower()
    if not guess:
        print("Attempt not counted")
        continue
    elif guess == "quit":
        print(f"The number was {secret}")
        attempts = -1
        break
    guess = int(guess)
    attempts += 1
    if guess > secret:
        print("Too high!")
    if guess < secret:
        print("Too low!")
    if guess == secret:
        print("Correct!")
        attempts += 1
        break

if attempts == -1:
    print("You gave up!")
elif attempts == 10:
    print(f"Game over! The number was {secret}.")
else:
    print(f"You got it in {attempts} attempts!")