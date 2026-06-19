#  A utility class that calculates simple interest and GST using static methods.

class BankCharges:

    @staticmethod
    def calculate_interest(principal,rate,time):
        return (principal*rate*time)/100

    @staticmethod
    def calculate_gst(amount):
        return (amount*18)/100

print("Interest rate:",BankCharges.calculate_interest(1000,2,1))
print("GST:",BankCharges.calculate_gst(1000))
