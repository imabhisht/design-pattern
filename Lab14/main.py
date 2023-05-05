class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.observers = []

    def add_product(self, product):
        self.products.append(product)
        self.notify_observers()

    def remove_product(self, product):
        self.products.remove(product)
        self.notify_observers()

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.products)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, products):
        print(f"{self.name} received an update:")
        for product in products:
            print(f"\t- {product}")

store = Store("Laptop and Mobile Store")
customer1 = Observer("Customer 1")
customer2 = Observer("Customer 2")

store.attach_observer(customer1)
store.attach_observer(customer2)

while True:
    print("1. Add product")
    print("2. Remove product")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        store.add_product(product)
        input("Press Enter to Continue...")
    elif choice == 2:
        product = input("Enter product name: ")
        store.remove_product(product)
        input("Press Enter to Continue...")
    elif choice == 3:
        break
    else:
        print("Invalid choice")

store.detach_observer(customer1)
store.detach_observer(customer2)
