
class Flight:

    #   IT IS NOT THE CONSTRUCTOR
    #   IT INITIALIZES AN OBJECT THAT HAS ALREADY BEEN INITIALIZED
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No code")

        if not number[:2].isupper():
            raise ValueError("No valid code")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid route number")
        
        self._number = number

    
    def number(self):
        return self._number


A = (range(1, 10), "abcdefg"[:3])
