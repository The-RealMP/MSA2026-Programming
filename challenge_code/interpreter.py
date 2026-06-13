#While Loop
def main():
    while True:
    #INPUT 
    # prompt the user to enter the expression   
        user_expression = (input("Enter Expression (X Y Z):\n "))
     #PROCESS
        # Validate the expression format 
        # use the split method to split the expression at the space " "
        expression = user_expression.split(" ")
        X = int(expression[0])
        Y = expression [1]
        Z = int(expression [2]) 
        # if the length of the resulting list is not 3 then invalid format 
        
        
    #PROCESS
    # Validate the expression format 
    
        # if the length of the resulting list is not 3 then invalid format 

    # Validate that X and Z are intergers
        # Convert to int. 
        # if converting causes a exception, then invalid format 
# Validate that Y is an acceptable operator(+, -, *, /)
    # use and IF statement to determine if Y == + or - or * or /
    # invalid format if not 
    







main ()






# Validate that when Y is "/"" Z is not 0
    # Use IF: if Y == "/" and Z == 0: divide by zero error

# Do the math

#OUTPUT
# Print the output to the user
