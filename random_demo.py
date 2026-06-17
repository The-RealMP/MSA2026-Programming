import random
def main():
    #create a random number generator
    random_generator = random.Random()
    random_number = random_generator.randint(0,100)
    print(f"Ramdom Value: {random_number}")
    #generate 20 random numbers
    print(f"\nGenerate 20 random numbers\n-------------------------------------------------------")
    #number of numbers generated
    for _ in range(20):
        #what numbers are beng generated
        print(random_generator.randint(0,100))

main()