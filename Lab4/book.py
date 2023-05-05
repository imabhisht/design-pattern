import bookshop

class Book:
    def __init__(self):
        print("Book Object Created")
        self.title = None
        self.id = None

    def setTitle(self, title):
        self.title = title

    def setId(self, id):
        self.id = id

    def getId(self) -> int:
        return self.id

    def __str__(self):
        print(f"Book: {self.title} with id: {self.id}")




    