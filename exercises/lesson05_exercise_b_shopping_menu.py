shopping_list = ["milk", "egg", "banana", "chicken"]
print(shopping_list)
while True:
    print("1) Add item  2) Remove item  3) Show list  4) Quit")
    menu_input = input("Enter an option: ")
    match menu_input:
        case "1":
            item = input("Add an item to the shopping list: ").strip().lower()
            if not item:
                print("Skipped")
            elif item in shopping_list:
                print("Item already in list")
            else:
                shopping_list.append(item)
        case "2":
            remove_item = input("Choose an item to remove: ").strip().lower()
            if not remove_item:
                print("Skipped")
            elif remove_item not in shopping_list:
                print("Item not in list")
            else:
                shopping_list.remove(remove_item)
        case "3":
            shopping_list.sort()
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        case "4":
            break
        case _:
            print("Invalid input! Try again.")