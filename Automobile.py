import datetime
class Automobile():
    #define a constructor
    #the constructor is a function that is called to create
    # an automobile
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        #define class properties with the premeter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
        self.__color = color

    #Create getter and setter methods for class properties 
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.model
    
    def get_vin(self):
        return self.__vin

    def get_engine_size(self):
        return self.__engine_size

    def set_engine_size(self, new_size:float):
        self.__engine_size = new_size
        return

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner:str):
        self.__owner = new_owner
        return

    def get_year(self):
        return self.__year
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        self.__color = new_color
        return


    #create a method to print automobile data 
    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"VIN: {self.__vin}, Engine Size: {self.__engine_size}")
        print(f"Owner: {self.__owner}, Color:{self.__color}\n")
    
    #create a method to get a automobile's age 
    def get_age(self):
        #get the current year
        the_data = datetime.datetime.now()
        this_year = the_data.year

        #return the difference between the current year and the auto year as the age
        return this_year - self.__year
    