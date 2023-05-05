# Decorator design pattern example with a menu

# Component interface
class MenuItem:
    def get_description(self):
        pass

    def get_cost(self):
        pass

# Concrete Component
class BasicMenuItem(MenuItem):
    def get_description(self):
        return "Basic Item"

    def get_cost(self):
        return 5

# Decorator
class MenuItemDecorator(MenuItem):
    def __init__(self, item):
        self._item = item

    def get_description(self):
        return self._item.get_description()

    def get_cost(self):
        return self._item.get_cost()

# Concrete Decorator
class ExtraCheese(MenuItemDecorator):
    def __init__(self, item):
        super().__init__(item)

    def get_description(self):
        return self._item.get_description() + ", Extra Cheese"

    def get_cost(self):
        return self._item.get_cost() + 1

# Concrete Decorator
class ExtraBacon(MenuItemDecorator):
    def __init__(self, item):
        super().__init__(item)

    def get_description(self):
        return self._item.get_description() + ", Extra Bacon"

    def get_cost(self):
        return self._item.get_cost() + 1.5

# Client
def main():
    # Create a basic menu item
    item = BasicMenuItem()

    while True:
        print("1. Basic Item")
        print("2. Basic Item with Extra Cheese")
        print("3. Basic Item with Extra Bacon")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Item: ", item.get_description())
            print("Cost: $", item.get_cost())
        elif choice == '2':
            item = ExtraCheese(item)
            print("Item: ", item.get_description())
            print("Cost: $", item.get_cost())
        elif choice == '3':
            item = ExtraBacon(item)
            print("Item: ", item.get_description())
            print("Cost: $", item.get_cost())
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
