fruits = ["apple", "banan", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["Alex", 25, True, 1.78]
empty = []

print(fruits)
print(len(fruits))

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[::-1])

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

fruits.insert(0, "mango")
print(fruits)

fruits.extend(["kiwi", "lime"])
print(fruits)

fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
print(fruits)

last = fruits.pop()
print(last)

first = fruits.pop(0)
print(first)

del fruits[0]
fruits.clear()

if "grape" in fruits:
    fruits.remove("grape")

nums = [3, 1, 4, 1, 5, 9]

print(4 in nums)
print(nums.index(5))
print(nums.count(1))

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

original = [3, 1, 2]
new = sorted(original)
print(original is new)
print(original, new)

words = ["banana", "Apple", "cherry"]
words.sort(key=str.lower)
print(words)

scores = [85, 92, 78, 95, 88]

print(len(scores))
print(sum(scores))
print(min(scores))
print(max(scores))
print(sum(scores) / len(scores))

grid = [
    [1, 2, 3],
    [4, 5, 6]
]

print(grid[1])
print(grid[1][2])

a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a)

tags = "python,ai,reg".split(",")
print(", ".join(tags))

point = (10, 20)
print(point[0])

x, y = point
print(x, y)
