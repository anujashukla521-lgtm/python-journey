# A simple billing program that calculates the total cost based on product quantity and price per item.

product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = price*quantity
print(f"Product name: {product_name}\nQuantity: {quantity}\nPrice per item: {price}\nTotal bill: {total}")
