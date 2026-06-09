# Program to Convert lbs to kgs
# INPUT (getting the data that will be processed)
# Loop
while(True):
     # Validate input: ensure the data is a numberic type
    try:
        # Prompt user to enter weight in lbs 
        user_weight = float(input("Enter weight in lbs: "))
        # check if weight is less than or equal to 0 output error message and reprompt the user
        if user_weight <= 0:
            print("ERROR: Enter a number greater than 0.\n-")
            continue
        break
    except: 
        print("ERROR: Please enter a number.\n")
        continue
    # If the input is invalid then reprompt the user until the input is a valid

# PROCESSING
# Use a conversion factor to convert lbs to kgs (2.205lbs = 1kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT
# Print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kgs.")
