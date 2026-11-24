



class Product:

    def __init__(self,name,category,price,quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"The name of this product is: {self.name}")
        print(f"The category of this product is: {self.category}")
        print(f"The price of the product is: ${self.price: ,.2f}")
        print(f"The remaining amount of this product is: {self.quantity}")

    def inventory_value(self,price,quantity):
        value = self.price * self.quantity
        print(f"The inventory value of this is: ${value: ,.2f}")


product1 = input("Enter product name: ")
product2 = input("Enter a 2nd product name: ")


