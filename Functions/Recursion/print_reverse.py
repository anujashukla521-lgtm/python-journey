# A Python recursion program that prints numbers from N to 1 using recursive function calls while handling invalid inputs safely.

def print_reverse(num):
    if num<=0:
        return
    if num == 1:
        print(1)
    else:
        print(num)
        print_reverse(num-1)

n = int(input("Enter a num: "))
print_reverse(n)
