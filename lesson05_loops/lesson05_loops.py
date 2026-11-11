fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

for ch in "Hi!":
    print(ch)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 20, 5):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")

numbers = [4, 8, 15, 16, 23, 42]

total = 0

for n in numbers:
    total += n

print(total)

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)

count = 3
while count > 0:
    print(count)
    count -= 1

for n in range(1,10):
    if n == 5:
        break
    print(n)

for n in range(1,6):
    if n == 3:
        continue
    print(n)

while True:
    text = input("You: ").strip()
    if text.lower() == "quit":
        print("Bye!")
        break
    if not text:
        continue
    print(f"You said: {text}")

people = [("Alex", 25), ("Sam", 31), ("Jo", 19)]

for name, age in people:
    print(f"{name} is {age}")

for row in range(1,4):
    for col in range(1,4):
        print(row*col, end="\t")
    print()


squares = [n * n for n in range(1,6)]
