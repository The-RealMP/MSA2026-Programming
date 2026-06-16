def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    #print the names of the students with their scores 
    print("Students and Scores using the lists\n---------------------------------------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    # Create a dictionary of names and scores
    student_scores = {
        "Alice":55,
        "Bob":75,
        "Jerry":87,
        "Jane": 82,
        "Bill": 91
    }

    # print Bob and Janes scores
    print("\nPrint Bob and Jane's Scores\n---------------------------------------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])

    # print all the data in the student scores dictionary 
    print("\nPrint all student data\n---------------------------------------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    # create a dictionary to store car information 
    # make, model. year, value, engine size
    car_1 = {"Make": "Ferrari", "Model": 'F-50', "Year": 2024, "Value": 500000, "Engine": 4.4}
    # get all the the car information
    print("\nGet all car information\n")

    for key, value in car_1.items():
        print(f"{key}: {value}")

    # create a second car
    car_2 = {"Make": "Honda", "Model": 'Accord', "Year": 2024, "Value": 18000, "Engine": 2.4}

     # Add an entry to a dictionary
    car_1["Transmission"] = "manual"
    car_2["Transmission"] = "manual"

    # create a list of dictionaries
    dictionary_list = [car_1, car_2]

    # display information for all cars
    print("\nDisplay information for all cars\n---------------------------------------------")
    
    #loop over all the cars
    for car in dictionary_list:
        print("\nCar Information\n---------------------------------------------")
        
        #loop over the key value pairs in the dictionary
        for feature, value in car.items():
            print(f"{feature}: {value}")

    # Create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}

    # print all car information from the dictionary
    print("\nCar information from dictionaries\n---------------------------------------------")

    for make, car in car_dictionary.items():
        print(f"\n{make}\n---------------------------------------------")
        for feature, value in car.items():
            print(f"{feature}: {value}")

    # Getting a value from a dictionary when no key exists
    key = "Transmission"
    car_1.keys()
    print("Finding key using Try/Except")
    try:   
        print(f"{car_1[key]}")
    except:
        print(f"ERROR: Key '{key}' does not exist in the dictionary")

    print("\nFinding Key using dictionary.keys()\n---------------------------------------------")
    if key not in car_1.keys():
        print(f"ERROR: Key '{key}' does not exist in the dictionary")
    else:
        print(f"{car_1[key]}")
    
    













main()