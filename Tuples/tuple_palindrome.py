# Checked whether a tuple reads the same forward and backward using slicing.

tup = (1,2,3,2,1,5)
if tup== tup[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

