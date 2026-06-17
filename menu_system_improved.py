
#function to load data from a file and return a dictionary
#Input:filename
#Ouptut: Dictionary
def load_menu_items(filename:str) ->dict:
    #open menu.txt; create a file handler to open file in read mode 
    data_file = open(filename, "r")
    
    #create a empty dictionary 
    menu_items = {}

    #use a loop to read the contents of the file line by line
    for line_of_data in data_file: 
        #split the line at the comma
        item_name_and_price = line_of_data.split(",")
        
        
        #get the item and price from the list 
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])


        #create a entry in the dictionary for the item and price
        menu_items[item_name] = item_price

    #close the file 
    data_file.close()

    #return the dictionary of menu items 
    return menu_items

def main():
    #print menu heading
    print("MENU")
    print("---------------------------------------")
    # menu directory
    # Item, price

    menu_items = load_menu_items("menu.txt")
    total = 0
    while True:
        # Get input from the user
        item = input("\nItem: ").capitalize()

        if item == "End":
            break

        # Check if the item exists in the menu and get the price
        if item not in menu_items:
            continue

        total += menu_items[item]
        print(f"Total: ${total:.2f}\n")

main()