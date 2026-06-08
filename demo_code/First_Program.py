# Print (Hello World)
print("Hello World")

#create a variable to store my name
first_name = "Marshall"

#create a variable for last name
last_name = "Pherigo"

#write a python statement to display "My full name is Marshall Pherigo"
print("My full name is", first_name, last_name,sep="")

#print using the f string (strining interpolation)
print(f"My full name is {first_name}{last_name}. ")

# create variables to store age and weight
age = 16
weight = 128
half_age = age / 2

#print a sentence with name, age, and weight
print(f"My Name is {first_name} {last_name}.\nI am {age} years old and I weight {weight}Ibs")

#get and print the data type for age, weight, and half age
print("\nChecking Data Types\n-------------")
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 statements using string interpolation (f string) to print descriptive sentence for the data types
#print descriptive sentences for the data types
#"Variable age is an int"
print(f"Variable age is an {type(age)}")
print(f"Variable weight is an {type(weight)}")
print(f"Variable half_age is an {type(half_age)}")

number_1 = "5" 
number_2 ="7"
total = number_1 + number_2
print(f"Total: {total}")