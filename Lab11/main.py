## Iterator design pattern 
class Iterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class Menu:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return Iterator(self._items)

def main():
    # Create a menu
    menu = Menu()
    menu.add_item("Item 1")
    menu.add_item("Item 2")
    menu.add_item("Item 3")

    # Iterate through the menu items
    print("Menu Items:")
    for item in menu.create_iterator():
        print(item)

if __name__ == "__main__":
    main()




# # Iterator design pattern example with a menu

# # Concrete Iterator
# class MenuIterator:
#     def __init__(self, items):
#         self._items = items
#         self._index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._index < len(self._items):
#             item = self._items[self._index]
#             self._index += 1
#             return item
#         else:
#             raise StopIteration

# # Concrete Aggregate
# class Menu:
#     def __init__(self):
#         self._items = []

#     def add_item(self, item):
#         self._items.append(item)

#     def create_iterator(self):
#         return MenuIterator(self._items)

# # Client
# def main():
#     # Create a menu
#     menu = Menu()
#     menu.add_item("Item 1")
#     menu.add_item("Item 2")
#     menu.add_item("Item 3")

#     # Iterate through the menu items
#     print("Menu Items:")
#     for item in menu.create_iterator():
#         print(item)

# if __name__ == "__main__":
#     main()
