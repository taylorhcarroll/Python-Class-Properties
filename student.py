# Define a Python class named Student. This class will have 5 properties.
# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student():
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for first_name')

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for last_name')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for age')

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError(
                'Please provide an integer value for cohort_number')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # this performs the same thing as ToString() and if specified in a class overrides the default of the __str__ method
    def __str__(self):
        return f'{self.full_name} is {self.age} and is in cohort {self.cohort_number}.'


taylor = Student()
taylor.first_name = "Taylor"
taylor.last_name = "Carroll"
taylor.age = 30
taylor.cohort_number = 37

print(taylor)
