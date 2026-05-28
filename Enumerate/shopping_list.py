# Creates a numbered shopping list using enumerate().

shopping_list = ["Milk", "Bread" , "Eggs","Biscuits"]
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")
