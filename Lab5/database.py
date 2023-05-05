from databaseConnection import User

class Bank:
    def __init__(self):
        self.name = "Kotak Mahindra Bank"
        self._users = []

    def addUser(self):
        name = input("Enter Name: ")
        bankBalance = int(input("Enter Bank Balance: "))
        self._users.append(User(name, bankBalance))

    def getAllUser(self):
        for user in self._users:
            print(f"Id: {user.id} \nName: {user.name} \nBank Balance: {user.bankBalance} \n-----------------")

    def credit(self, userId, amount):
        for user in self._users:
            if user.id == userId:
                user.bankBalance += amount
                print(f"{user.name} has Credited Amount: {amount} Successfully...")

    def debit(self, userId, amount):
        for user in self._users:
            if user.id == userId:
                if user.bankBalance < amount:
                    print(f"{user.name} Debited Amount: {amount} was Unsuccessful...")
                    return
                user.bankBalance -= amount
                print(f"{user.name} Debited Amount: {amount} Successfully...")

class Database:
    def __init__(self) -> None:
        self.name = "PostgreSQL"
        self.version = "12.3"
        self.bank = Bank()

    def data(self):
        print("Data")
    
