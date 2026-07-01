class Shopping:
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price

    def __add__(self,other):
        return self.price+other.price

cart1 = Shopping("Shirt",2000)
cart2 = Shopping("Kurti",500)

print(cart1.product_name, cart1.price)
print(cart2.product_name, cart2.price)
print(cart1+cart2)
