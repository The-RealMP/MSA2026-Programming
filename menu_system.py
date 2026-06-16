def main():
    #print menu heading
    print("MENU")
    print("---------------------------------------")
    # menu directory
    # Item - price
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total = 0
    while True:
        # Get input from the user
        item = input("\nItem: ").capitalize()

        if item == "End":
            break

        # Check if the item exists in the menu and get the price
        if item not in menu:
            continue

        total += menu[item]
        print(f"Total: ${total:.2f}\n")

main()
