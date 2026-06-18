import random

def get_game_level(): 
    # Prompts the user to choose a difficulty level: 1, 2, or 3.
    while True:
        try:
            level = int(input("Enter Level 1, 2, 3: ")) 
            if level in [1, 2 ,3]:
                return level
            else:
                print("Error: Invalid input!") 
        except:
            print("Error: Invalid input!") 
def get_number_of_questions():
    # Prompts the user for the number of questions to ask (3 to 10)
    while True:
        try:
            num_questions = int(input("Enter number of questions to ask (3 to 10): ")) 
            if 3 <= num_questions <= 10:
                return num_questions
            else:
                print("ERROR: Please enter an number between 3 and 10!") 
        except:
            print("ERROR: Please enter an number between 3 and 10!") 

def main():
    # Get Game Settings
    level = get_game_level()
    total_questions = get_number_of_questions()
    
    # Determine digit ranges based on level
    if level == 1:
        min_val, max_val = 0, 9
    elif level == 2:
        min_val, max_val = 10, 99
    else:
        min_val, max_val = 100, 999
        
    correct_count = 0
    
    # Ask questions
    for i in range(total_questions):
        x = random.randint(min_val, max_val)
        y = random.randint(min_val, max_val)
        correct_answer = x + y
        
        max_attempts = 3
        # Handle up to 3 attempts per question
        for attempt in range(max_attempts):
            user_input = input(f"{x} + {y} = ") 
            try:
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    print("CORRECT!!!") 
                    correct_count += 1
                    break
                else:
                    print("WRONG!!!") 
            except:
                print("WRONG!!!") 
                
            # if run out of attempts print the answer
            if attempt == max_attempts - 1:
                print(f"Correct Answer: {x} + {y} = {correct_answer}") 
                
    # Calculate and print percentage
    percentage = (correct_count / total_questions) * 100
    print(f"You got {correct_count} out of {total_questions} questions correct: {percentage:.2f}%")

if __name__ == "__main__":
    main()
