import math
from databaseConnection import DatabaseConnection

class User:
    def __init__(self, name, bankBalance):
        self.id = math.floor(math.random() * 1000)
        self.name = name
        self.bankBalance = bankBalance
        self.connectionExists = False
        self.connection = DatabaseConnection.getInstance()

    def connect(self):
        self.connectionExists = True

    def disconnect(self):
        self.connectionExists = False