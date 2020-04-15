# Define a Python class named Student. This class will have 5 properties.
class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0
# Full name (read-only string)

# Define getters for all properties.
    @property # gets first_name
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return ""
    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return ""
# Define a setter for all but the read only property.
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("First name must have letters!")

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Last name must have letters!")

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Age must be a number!")

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError("Cohort must be a number!")


    @property
    def full_name(self):
        try:  
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return ""

# Use the __str__ and __repr__ magic methods on your class to specify 
# what an object's string representation should be. It's just like the 
# toString() method in JavaScript.

    def __str__(self):
        return F"{self.full_name} is {self.age} years old and is in C{self.cohort_number} ..."

mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39

print(mike)