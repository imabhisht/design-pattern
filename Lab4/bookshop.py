from book import Book

class BookShop:
    def __init__(self, name: str):
        self.__booklist = []
        self.__total = 0
        self.name = name

    def editBookById(self, id: int, title: str):
        index = 0
        flag = False
        for book in self.__booklist:
            index += 1
            if book.id == id:
                book.setTitle(title)
                book.setId(id)
                flag = True
                return flag

        return flag

    def addBook(self, book: Book):
        self.__booklist.append(book)
        self.__total += 1
    
    def addBooks(self, books: list):
        self.__booklist.extend(books)
        self.__total += len(books)

    def getBook(self, index: int) -> Book:
        return self.__booklist[index]

    def getBooks(self) -> list:
        return self.__booklist # List of Books

    def getBookById(self) -> Book:
        tempBook = None
        for book in self.__booklist:
            if book.id == id:
                tempBook = book
        
        return tempBook


    def removeBookById(self, id: int):
        for book in self.__booklist:
            if book.id == id:
                self.__booklist.remove(book)
                self.__total -= 1
                return

    def printBooks(self):
        print("Store Name: ", self.name)
        print("Total Books: ", self.__total)
        for book in self.__booklist:
            # print(book.__str__())
            print(f"Book - Id: {book.id} with Title: {book.title}")

