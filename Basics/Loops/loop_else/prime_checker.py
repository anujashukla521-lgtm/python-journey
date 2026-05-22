num = int(input("Enter a num: "))

if num<=1:
    print(f"{num} is not prime")

else:

    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime")
            break

    else:
        print(f"{num} is prime")