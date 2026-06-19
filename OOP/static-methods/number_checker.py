# A utility class containing static methods to validate number properties such as even/odd and positive/negative checks.

class NumberChecker:
    
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False

    @staticmethod
    def is_odd(num):
        if num%2!=0:
            return True
        else:
            return False

    @staticmethod
    def is_positive(num):
        if num>0:
            return True
        else:
            return False

    @staticmethod
    def is_negative(num):
        if num<0:
            return True
        else:
            return False

print("Even:",NumberChecker.is_even(9))
print("Odd:",NumberChecker.is_odd(1))
print("Positive:",NumberChecker.is_positive(7))
print("Negative:",NumberChecker.is_negative(-5))
