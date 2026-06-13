def main ():
    my_name = "marshall"

    #capitalize a string 
    print(f"my name is capitlized: {my_name.capitalize()}")

    # make a string uppercase
    print(f"my name uppercased: {my_name.upper()}")

    #make a string lowerase
    last_name = "PHERIGO" 
    print(f"My full name lowercased: {my_name.lower()} {last_name.lower()}")

    #compare two strings
    my_name_tilted_case = "Marshall"
    if my_name.lower() == my_name_tilted_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal.")

    print("\nUsing the Startswith() method\n--------------------")
    #determine if a string starts with a set of characters
    print(f"{my_name} starts with a M or m: {my_name.startswith("M") or my_name.startswith("m")}")

    if (not my_name.startswith("Mars") and (not my_name.startswith("mars"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelt {my_name} correctly!")

    if ((not my_name.lower().startswith("Mars"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelt {my_name} correctly!")

    print("\nUsing the endswith() method\n--------------------")
    print(f"{my_name} ends with 'hall': {my_name.endswith('hall')}")

    print("\nUsing the Find() method\n--------------------")
    #find the h is Marshall 
    search_letter = "h"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
     print(f"The '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"Thered is no '{search_letter}' in {my_name}.")

    print("\nLooping through a string\n--------------------")
    for letter in my_name: 
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")
    #print the letters in a string along with the index positions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]} ")

    print("\n Search a string\n--------------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
     # Write code that counts the number of occurences of the word dog in the sentence 
     # expected output: 3 
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        #start at the beginning of the string
        # search for the occurence of the word "dog" starting at index 0 
        dog_index = sentence.find(search_word, start_index)
        
        #search until we dont find any more dogs: when find() returns -1
        if dog_index == -1:
            break
        else:
            #number_of_dogs = number_of_dogs +1
            # if we find dog, add 1 to some variable we use to use to keep track of the number of dogs we find 
            number_of_dogs += 1

            #update the starting index by 1
            # continue searching the string from the next index after the dog we just found
            start_index = dog_index + 1
        #do this until we dont find any more dogs: when find() returns -1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")
    
    # using the split() method 
    print("\nUsing the split() method\n--------------------")
    #format: make,model,year,price,engine_size
    car_info = "Ferrari,F-50,2025,500000,4.8\n"
    car_data = car_info.split(",")
    print(f"Car Data: {car_data}")

    #get the individual items from the list
    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price: ${price:,.2f} - Engine Size: {engine_size}l")

    print("\nSubstring Method\n--------------------")

    # find the first comma
    index_of_comma = car_info.find(",")
    start_index = 0
    
    #read all characters up to the first comma
    # list[start_index ; stop_index] 
    make_substring = car_info[start_index: index_of_comma]
    print(f"Make: {make}")
    


main ()