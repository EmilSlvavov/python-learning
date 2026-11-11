shopping = ["milk", "eggs", "bread"]
print(f"Shopping list: {', '.join(shopping)}")
item = input("Add an item to the shopping list: ").strip().lower()

if not item:
    print("Skipped")
elif item in shopping:
    print("Item already in list")
else:
    shopping.append(item)

print(f"Shopping list: {', '.join(shopping)}")
remove_item = input("Choose an item to remove: ").strip().lower()
if not remove_item:
    print("Skipped")
elif remove_item not in shopping:
    print("Item not in list")
else:
    shopping.remove(remove_item)

shopping.sort()
print(", ".join(shopping))

print(len(shopping))


