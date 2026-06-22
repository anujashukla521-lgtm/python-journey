# A Python inventory management program that counts the total number of product objects using class variables and class methods.

class Product:
    total_products = 0
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price
        Product.total_products+=1

    @classmethod
    def show_total_products(cls):
        return f"Total products: {cls.total_products}"

    def show_details(self):
        print(f"Product name: {self.product_name}\nPrice: {self.price}")



p1 = Product("Pen",30)
p2 = Product("Notebook",80)
p3 = Product("Geometry Box",50)
p4 = Product("Eraser",15)

p1.show_details()
p2.show_details()
p3.show_details()
p4.show_details()

print(Product.show_total_products())
