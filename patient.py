# Create a class to represent a patient of a doctor's office. The Patient class will accept the following
# information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name should not be exposed as properties
# at all, but instead expose a calculated property of full_name. Address should have a getter and setter.
class Patient():
    def __init__(self, ssn, dob, account_number, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__account_number = account_number
        self.__full_name = f'{first_name} {last_name}'
        self.__address = address

        @property
        def ssn(self):
            return self.__ssn

        @property
        def dob(self):
            return self.__dob

        @property
        def full_name(self):
            return self.__full_name

        @property
        def address(self):
            try:
                return self.__address
            except AttributeError:
                return ""

        @address.setter
        def address(self, new_address):
            if type(new_address) is str:
                self.__address = new_address
            else:
                raise TypeError(
                    'Please provide a string value for the address')


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)


print(cashew.full_name)
print(cashew.ssn)
print(cashew.dob)
