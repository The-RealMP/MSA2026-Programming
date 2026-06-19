class Student():
    #define consctructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        #define class properties with premeter values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id

    #create getter and setter methods
    def get_first_name(self) ->str:
        return self.__first_name
    
    def set_first_name(self, new_first_name:str):
        self.__first_name = new_first_name
        return
    
    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
        return
    
    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        self.__major = new_major
        return
    
    def get_credit_hours(self:int):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours:int):
        self.__credit_hours = new_credit_hours
        return
    
    def get_gpa(self)->float:
        return self.__gpa
    
    def set_gpa (self, new_gpa:float):
        self.__gpa = new_gpa
        return
    
    def get_student_id(self)-> str:
        return self.__student_id
    
    def update_credit_hours(self, additional_hours)->str:
        self.__credit_hours += additional_hours

    def get_class_level(self)->str:
        if self.__credit_hours >= 90:
            return "Senior"
        elif self.__credit_hours >= 61:
            return "Junior"
        elif self.__credit_hours >= 31:
            return "Sophomore"
        else:
            return "Freshman"
    
    #create a method to print student data
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()} | Major: {self.__major}")
        print(f"GPA: {self.__gpa} | ID: {self.__student_id}")

   