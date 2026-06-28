class Order:
    def __init__(self,order_id,customer_name):
        self.order_id = order_id
        self.customer_name = customer_name


class OnlineOrder(Order):
    def __init__(self,order_id,customer_name,delivery_address,delivery_charge):
        super().__init__(order_id,customer_name)
        self.delivery_address = delivery_address
        self.delivery_charge = delivery_charge


    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Delivery Address: {self.delivery_address}")
        print(f"Delivery Charge: {self.delivery_charge}")

obj1 = OnlineOrder(101,"Mohan","121-Dome Colony,Varanasi",4000)
obj1.display_order()