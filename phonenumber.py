import re
class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = re.sub('[^\d]',"",phone_number)
        if len(self.phone_number) == 11 and self.phone_number[0] == '1':
            self.phone_number = self.phone_number[1:]
        elif len(self.phone_number)<10 or (len(self.phone_number)>10 and self.phone_number[0]!=1) :
            self.phone_number ="0"* 10

    @property
    def number(self):
         return self.phone_number
        
    def area_code(self):
            return self.phone_number[0:3]

    def pretty(self):
             return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"


'''The rules are as follows:
If the phone number is less than 10 digits assume that it is bad number
If the phone number is 10 digits assume that it is good
If the phone number is 11 digits and the first number is 1, trim the 1 and use the last 10 digits
If the phone number is 11 digits and the first number is not 1, then it is a bad number
If the phone number is more than 11 digits assume that it is a bad number
You are provided with a class Phone which has following methods:
=========================================================================
number Returns the number that is initialized if the number is valid, following above rules
number = Phone("(123) 456-7890").number
"1234567890"
This should return "0000000000" if the number is invalid.
area_code
Returns an area code from the number. The area code will be 3 digits
===================================================================================
number = Phone("1234567890")
number.area_code()
"123"
This should be returned as a string.
pretty
Returns a neat format of the number with the area code in brackets.
number = Phone("1234567890")
number.pretty()
"(123) 456-7890" '''
