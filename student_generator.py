from Student import Student

def main(self):
    #opeen student.csv; create a file handler to open file in read mode
    data_file = open("students.csv", "r")
    print(data_file)
    
    #create a empty dictionary
    student_info = {}

    #read the contents of the file line by line
    for line_of_data in data_file:
        #split the line at the comma
        student_data = line_of_data.split(",")
        print(student_data)

        #get the student info from the list
        self.__first_name = student_info[0]
        self.__last_name = student_info[1]
        self.__major = student_info[2]
        self.__credit_hours = student_info[3]
        self.__gpa = student_info[4]
        self.__student_id = student_info[5]
        
        print(student_info)
main()