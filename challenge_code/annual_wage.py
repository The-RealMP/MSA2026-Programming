# Program to calculate total wages for a year, if a person works 350 days per year and 12% in taxes are deducted.
# INPUT (daily hours & hourly wage)
# Prompt user to enter in hours worked daily and hourly wage

while(True):
    #Validate input: hourly wage
    try:
        # Prompt user to enter hourly wages
        user_hourly_wage = float(input("Enter hourly wage: "))
        # check if the users hourly wage is greater than 0
        if user_hourly_wage <= 0:
            print('ERROR: Please enter a number greater than 0\n')
            continue
        break
         
    except:
        print("ERROR: Please enter a number.\n")
        continue
    # If the input is invalid then reprompt the user until the input is


while(True):
    #Validate input: daily hours
    try:
        #Prompt user to enter daily hours
        user_daily_hours = float(input("Enter daily hours: "))
        # check if the users daily hours are less than or equal to 24 and reprompt the user
        if user_daily_hours > 24:
            print("ERROR: Please enter a number less than or equal to 24.\n")
            continue
        if user_daily_hours <=0:
            print('ERROR: Please enter a number greater than 0.\n')    
            continue
        break

    except:
        print("ERROR: Please enter a number.\n")
        continue
    #If the input is invalid then reprompt the user until the input is


#PROCESSING
# Use a multiplication factor to calculate daily wage
user_daily_wage = user_daily_hours * user_hourly_wage
# Use a multiplication factor to calculate before taxes wage
user_pre_tax_annual_wage = user_daily_wage * 350
# Use a multiplication factor to calculate user annual wage
user_annual_wage = user_pre_tax_annual_wage * 0.88
# Use a multiplication factor to calculate taxes paid 
user_taxes_paid = user_pre_tax_annual_wage * 0.12


#OUTPUT
#Print the output to the user
print(f"Pay Advice \n-------------------------------------")
print(f"Hours Worked Daily: {user_daily_hours:.2f} ")
print(f"Hourly Wage: ${user_hourly_wage:.2f}:")
print(f"Wages Before Taxes: ${user_pre_tax_annual_wage:.2f}")
print(f"Tax Amount: ${user_taxes_paid:.2f}")
print(f"Annual Wage After Taxes: ${user_annual_wage:.2f}")