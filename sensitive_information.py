#  Create a class to represent a patient of a doctor's office. 
# The Patient class will accept the following information during 
# initialization

# 1. Social security number
# 2. Date of birth
# 3. Health insurance account number
# 4. First name
# 5. Last name
# 6. Address

class Patient:
    def __init__(self, SSN, DOB, insurance, first_name, last_name, address):
        self.__SSN = SSN
        self.__date_of_birth = DOB
        self.__insurance = insurance
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address


    @property 
    def SSN(self):
        try:
            return self.__SSN
        except AttributeError:
            return ""
    @property 
    def DOB(self):
        try:
            return self.__DOB
        except AttributeError:
            return ""
    @property 
    def insurance(self):
        try:
            return self.__insurance
        except AttributeError:
            return ""
    @property 
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
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""
    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Address must be a string")


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.SSN)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
