import math
# from database import Database
# from user import User
import random

class Bank:
    def __init__(self):
        self.name = "Kotak Mahindra Bank"
        self._users = []

    def addUser(self):
        name = input("Enter Name: ")
        bankBalance = int(input("Enter Bank Balance: "))
        self._users.append(User(name, bankBalance))

    def getAllUsers(self):
        for user in self._users:
            print(f"[Bank]:\nId: {user.id} \nName: {user.name} \nBank Balance: {user.bankBalance} \n-----------------")

    def credit(self, userId, amount):
        print(self._users)
        for user in self._users:
            if user.id == userId:
                user.bankBalance += amount
                print(f"[Bank]: {user.name} has Credited Amount: {amount} Successfully...")

    def selectUser(self):
        print("[Bank]: List of Users: ")
        for user in self._users:
            print(f"\nId: {user.id} \nName: {user.name} \nBank Balance: {user.bankBalance} \n-----------------")
        
        userId = int(input("[Bank]: Enter User Id: "))
        for user in self._users:
            if user.id == userId:
                return user


    def debit(self, userId, amount):
        for user in self._users:
            if user.id == userId:
                if user.bankBalance < amount:
                    print(f"{user.name} Debited Amount: {amount} was Unsuccessful...")
                    return
                user.bankBalance -= amount
                print(f"[Bank]: {user.name} Debited Amount: {amount} Successfully...")

class Database:
    def __init__(self) -> None:
        self.name = "PostgreSQL"
        self.version = "12.3"
        self.bank = Bank()

    def data(self):
        print("Data")
    

class User:
    def __init__(self, name, bankBalance):
        self.id = random.randint(1000,9999)
        self.name = name
        self.bankBalance = bankBalance
        self.connectionExists = False
        self.connection = DatabaseConnection.getInstance()

    def connect(self):
        self.connectionExists = True

    def disconnect(self):
        self.connectionExists = False

    def getConnectionStatus(self) -> bool:
        return self.connectionExists


class DatabaseConnection:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if DatabaseConnection.__instance == None:
            print("Database Connection Eastablished")
            return DatabaseConnection()
        
        print("Database Connection Already Eastablished")
        return DatabaseConnection.__instance
 
    def __init__(self):
        """ Virtually private constructor. """
        
        if DatabaseConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseConnection.__instance = self

    
    def credit(self, db: Database ,user: User, amount):
        if user.connectionExists:
            print("[Connection]: User already in Mid-Transaction!")
            return
        
        user.connect()
        db.bank.credit(user.id, amount)
        print("[Connection]: Operation Completed!!")
        return

    def debit(self, db: Database ,user: User, amount):
        if user.connectionExists:
            print("[Connection]: User already in Mid-Transaction!")
            return

        user.connect()
        db.bank.debit(user.id, amount)
        print("[Connection]: Operation Completed!!")
        return



