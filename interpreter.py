#While Loop
def main():
    while True:
        #INPUT 
        # prompt the user to enter the expression   
        user_expression = (input("\nEnter Expression (X Y Z):\n "))

        #PROCESS

        # Validate the expression format 
        # use the split method to split the expression at the space " "
        expression = user_expression.split(" ")

        #PROCESS
        # Validate the expression format 
        # if the length of the resulting list is not 3 then invalid format 
        if len(expression) != 3:
            print("ERROR: Invalid Format")
            continue

        X_str = (expression[0])
        Y = expression [1]
        Z_str = (expression [2]) 

        # Validate that X and Z are intergers
            # Convert to int. 
            # if converting causes a exception, then invalid format 
        try:
            X = int(X_str)
            Z = int(Z_str)
        except:
            print(" USER ERROR: Enter a integer")
            continue

        # Validate that Y is an acceptable operator(+, -, *, /)
        # use and IF statement to determine if Y == + or - or * or /
        # invalid format if not
        valid_operators = ['+', '-', '*', '/']
        if Y not in valid_operators:
            print("USER ERROR: Invalid operator. Use +, -, *, or /")
            continue

        # Validate that when Y is "/"" Z is not 0
        # Use IF: if Y == "/" and Z == 0: divide by zero error
        if Y == '/' and Z == 0:
            print("MATH ERROR: Cannot divide by zero")
            continue

        # Do the math
        if Y == '+':
            answer = X + Z
        elif Y == '-':
            answer = X - Z
        elif Y == '*':
            answer = X * Z
        elif Y == '/':
            answer = X / Z
        
        #OUTPUT
        # Print the output to the user
        print(f"Answer: {answer:.2f}")
        cont = input("Continue? (y/n): \n")
        if cont == "y":
            continue
        if cont == "n":
            break
main ()









