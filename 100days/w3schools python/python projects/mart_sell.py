class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print(f"Product '{product.name}'  added to the inventory.")


    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product '{product.name}' removed from the  inventory. ")

        else:
            print(f"Product '{product.name}' not found in the inventory")


def display_inventory(self):
    if self.products:
        print("Inventory:")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity:{product.quantity}")


    else:
        print("The Inventory is empty.")




# Define sale class

class Sale:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    def add_item(self,product, quantity):

        if product.quantity >= quantity:
            self.items.append((product, quantity))
            self.total_amount += product.price * quantity
            product.quantity -= quantity
            print(f"{quantity} '{product.name}' addes to the sale. ")

        else:
            print(f"Not enough stock for '{product.name}' .")


    def remove_item(self,product,quantity):
        for item in self.items:
            if item[0] == product:
                if item[1] >= quantity:
                    self.items.remove(item)
                    self.total_amount -= product.price * quantity
                    product.quantity += quantity
                    print(f"{quantity} '{product.name}' removed from the sale")

                else:
                    print(f"Only  {item[1]} '{product.name}' in the sale.")

                return
            print(f"'{product.name}' not found the sale.")



    def display_sale(self):
        if self.items:
            print("Sale:")
            for item in self.items:
                print(f"Name: {item[0].name}, Price: {item[0].price}, Quantity: {item[1]}")
            print(f"Total Amount : {self.total_amount}")
        else:
            print("The sale is empty.")


# Create an instance of the Inventory class
inventory = Inventory()

# Create some product instanve and add them to the inventoty class

product1 = Product("Product 1 ", 10, 21)
product2 = Product("Product 2 ", 400, 20)

inventory.add_product(product1)
inventory.add_product(product2)


# Display the inventory

inventory.display_inventory()

# Create an instance of the Sale calss

sale = Sale()

# ADd items to the sale 

sale.add_item(product1, 5)
sale.add_item(product1, 10)


# Display the sale 

sale.display_sale()


# Remove items form the sale 

sale.remove_item(product1, 2)

# Display the updated sale 

sale.display_sale()


# Remove a product from the incentory 

inventory.remove_product(product1)

# Displayt the updated inventory

inventory.display_incentory()




