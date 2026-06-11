def main():
    a = 5
    b = 5
    
    if a > b:
        print(f"a = {a} is greater than b = {b}.")
    elif b > a:
        print(f"b = {b} is greater than a = {a}.")
    elif a == b:
        print(f"a = {a} is equal to b = {b}")

    # print the appropiate letter grade based on a test score 
    # A: 100-90, B: 89-80, C: 79-70, D: 69-60, F: Less than 60
    # Output: test_score = 83
    # 83 --> B
    print("Grade decision: 1\n-------------------------")
    test_score = 72
    if (test_score >= 90):
        print(f"{test_score} --> A")
    elif (test_score >=80):
                print(f"{test_score}% --> B")
    elif (test_score >=70):
                print(f"{test_score}% --> C")
    elif (test_score >=60):
                print(f"{test_score}% --> D")
    else:
           print(f"{test_score}% --> F ")
        
    print("\nGrade decision: 2\n-------------------------")
    if (test_score >= 90):
        print(f"{test_score} --> A")
    elif (test_score >=80):
                print(f"{test_score}% --> B")
    elif (test_score >=70):
                print(f"{test_score}% --> C")
    elif (test_score >=60):
                print(f"{test_score}% --> D")
    else:
           print(f"{test_score}% --> F ")
    c = 4 
    d = 10
    # OR statements only 1 needs to be true
    # AND statement needs all to be true
    if a == 4 or b == 5 or c ==5 or d ==9:
        print("The OR condition is true")
    else:
        print("The OR condition is false")
main()
    