# Calculates discount eligibility based on purchase amount.

discount = 200
purchase = int(input("Enter purchase amount: "))
print("Discount price", purchase-discount) if purchase>1000 else print("Purchase price", purchase)
