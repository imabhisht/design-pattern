# Model
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

# View
class ConsoleView:
    def display_products(self, products):
        if not products:
            print("No products found.")
            return

        print("Product List:")
        for product in products:
            print(f"\t- {product}")

    def get_menu_choice(self):
        print("1. Add product")
        print("2. Remove product")
        print("3. Exit")
        return int(input("Enter your choice: "))

# Controller
class InventoryController:
    def __init__(self, inventory, view):
        self.inventory = inventory
        self.view = view

    def add_product(self, product):
        self.inventory.add_product(product)
        self.view.display_products(self.inventory.get_products())

    def remove_product(self, product):
        self.inventory.remove_product(product)
        self.view.display_products(self.inventory.get_products())

# Main program loop
inventory = Inventory()
view = ConsoleView()
controller = InventoryController(inventory, view)

while True:
    choice = view.get_menu_choice()

    if choice == 1:
        product = input("Enter product name: ")
        controller.add_product(product)

    elif choice == 2:
        product = input("Enter product name: ")
        controller.remove_product(product)

    elif choice == 3:
        break

    else:
        print("Invalid choice. Try again.")

print("Goodbye!")
