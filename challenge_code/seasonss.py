
# Create a decision structure to determine the season:
# Seasons are Winter, Spring, Summer, Fall
# Prompt the user to enter the number of the month, Month must be anywhere from 1-12
# winter: 12, 1, 2 | spring: 3, 4, 5 | summer: 6, 7, 8 | Fall: 9, 10, 11
# Output the season 
#Enter month number
# Output: It is winter: 11
# Output is Fall 



def main():
    while True:
        month = input("Please Enter Month number: ")

        if month == "12" or "1" or "2":
            print ("It is winter")
            break
        if month == "3" or "4" or "5":
            print ("It is spring")
            break
        if month == "6" or "7" or "8":
            print ("It is summer")
            break
        if month == "9" or "10" or "11":
            print ("It is spring")
            break
        else:
            print("ERROR: enter a number between 1-12: ")
            continue
main()