import random 

def user_difficulty(): 
    while True: 
        # Prompt the user to enter a difficulty 
        user_input = input("Enter level 1, 2, or 3: ") 
        
        # Validate that the input is 1, 2, or 3 
        try: 
            difficulty = int(user_input) 
            if difficulty in [1, 2, 3]:
                # Exit the loop if input is valid 
                break 
            else: 
                print("ERROR: Invalid Input!") 
                continue
        except: 
            print("ERROR: Invalid Input!") 

    if difficulty == 1: 
        # Create a random number generator 
        x_random_generator = random.Random() 
        x_value = x_random_generator.randint(0,9) 
        print(f"X-Value: {x_value}") 
        
        y_random_generator = random.Random() 
        y_value = y_random_generator.randint(0,9) 
        print(f"Y-Value: {y_value}") 
        
        user_answer = int(input(f"{x_value} + {y_value} = ")) 
        
        if user_answer != (x_value + y_value): 
            print("WRONG!!!")
            #reprompt 2 more times until correct 
        else:
            print("Correct!")
    if difficulty == 2: 
        # Create a random number generator 
        x_random_generator = random.Random() 
        x_value = x_random_generator.randint(10,99) 
        print(f"X-Value: {x_value}") 
        
        y_random_generator = random.Random() 
        y_value = y_random_generator.randint(10,99) 
        print(f"Y-Value: {y_value}") 
        
        user_answer = int(input(f"{x_value} + {y_value} = ")) 
        
        if user_answer != (x_value + y_value): 
            print("WRONG!!!") 
            #reprompt 2 more times until correct 
        else:
            print("Correct!")
    
    if difficulty == 3: 
        # Create a random number generator 
        x_random_generator = random.Random() 
        x_value = x_random_generator.randint(100,999) 
        print(f"X-Value: {x_value}") 
        
        y_random_generator = random.Random() 
        y_value = y_random_generator.randint(100,999) 
        print(f"Y-Value: {y_value}") 
        
        user_answer = int(input(f"{x_value} + {y_value} = ")) 
        
        if user_answer != (x_value + y_value): 
            print("WRONG!!!") 
            #reprompt 2 more times until correct 
        else:
            print("Correct!")

    
# Run the function
user_difficulty()


  
        






#def main ():
    #while True:
        

        #Prompt the user to enter a how many questions: 3-10: user_questions
            #validate user input: if user_questions != 3-10 reprompt
    #generate X and Y for questions 1-3 based off users diffculty chosen
        #1 - numbers 0-9
        #2 - numbers 10-99
        #3 - numbers 100-999
    #print questions
        #prompt user to answer questions
            #if answer is  correct
                #print "CORRECT!!!" and go to the next question
            #if answer is not correct
                #print "WRONG!!!" and reprompt
                #if after the 3rd time of answering the question print "Correct answer: X + Y = ans" then go to next question
        #calculate how many out of the questions they got right and print the percentage
            # (number_of_questions_right / total_number_of questions)*100 = percentage correct:.2f

#main()