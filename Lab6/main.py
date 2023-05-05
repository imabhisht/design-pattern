#Adpter Design Pattern

import os
import random
class Bank:
    def __init__(self):
        # self.__bankName = ""
        self.__bankAccount = []

    def getBankAccount(self,bankAccountNumber: int):
        print("b", self.__bankAccount)
        for bankAccount in self.__bankAccount:
            if bankAccount.getBackAccountNumber() == bankAccountNumber:
                return bankAccount

    def createBankAccount(self, __balance: int):
        bankAccount = BankAccount(__balance)
        print(bankAccount)
        self.__bankAccount.append(bankAccount)
        print(f"[Bank]: {bankAccount.getBankAccountNumber()} Account Created....")
        return bankAccount

    def transferAmountBetweenTwoAccount(self, BankAccountOne, BankAccountTwo,  amount, message: str = ""):
        if BankAccountOne.__balance >= amount:
            BankAccountOne.__balance -= amount
            BankAccountTwo.__balance += amount
            BankAccountOne.__transactions.append(f"[Bank] Type: Debited Amount: {amount} from Account: {BankAccountOne.__accountNumber}")
            BankAccountTwo.__transactions.append(f"[Bank] Type: Credited Amount: {amount} to Account: {BankAccountTwo.__accountNumber}")
            return True
        else:
            return False

    def transcation(self, bankAccountNumber: int,amount: int, type: str, message:str = ""):
        bankAccount = self.getBankAccount(bankAccountNumber)
        if bankAccount and type == "deposit":
            bankAccount.__balance += amount
            bankAccount.__transactions.append(f"[Bank] Type: {type} | Amount: {amount} | Message: {message}")
            return True

        elif bankAccount and type == "withdraw":
            if bankAccount.__balance >= amount:
                bankAccount.__balance -= amount
                bankAccount.__transactions.append(f"[Bank] Type: {type} | Amount: {amount} | Message: {message}")
                return True
            else:
                return False

        else:
            return False

class BankAccount(Bank):
    def __init__(self, __balance: int, __accountNumber: int = 0, __name="Unknown" , __bankName: str = "SBI"):
        self.__accountNumber = random.randint(1000000000, 9999999999)
        self.__accountType = "Saving"
        self.__balance = __balance
        self.__transactions = []
        self.__upiIdAlloted = []
        self.__name = __name
        self.__bankName = __bankName

    def getBankAccountNumber(self):
        return self.__accountNumber

    def getAllDetails(self):
        return {
            "accountNumber": self.__accountNumber,
            "accountType": self.__accountType,
            "balance": self.__balance,
            "transactions": self.__transactions,
            "upiIdAlloted": self.__upiIdAlloted,
            "name": self.__name,
            "bankName": self.__bankName
        }

    def getBackAccountNumber(self):
        return self.__accountNumber
    
    def getBalance(self):
        return self.__balance
    
    def getTransactions(self):
        return self.__transactions

    def getUPIIdAlloted(self):
        return self.__upiIdAlloted
    
    def getName(self):
        return self.__name

    def getBankName(self):
        return self.__bankName

   

class UPI(Bank):
    def __init__(self):
        self.__bankAccounts = []

    def addBankAccount(self, bankAccountNumber: int):
        bankAccount = Bank.getBankAccount(bankAccountNumber)
        if bankAccount:
            self.__bankAccounts.append(bankAccount)
            return True
        else:
            return False

    def allotUPIId(self, bankAccountNumber: int, upiId: str):
        bankAccount = self.getBankAccount(bankAccountNumber)
        if bankAccount:
            bankAccount.__upiIdAlloted.append(upiId)
            print(f"[UPI]: {upiId} Alloted to {bankAccount.getBackAccountNumber()}....")
            return True
        else:
            print(f"[UPI]: {bankAccountNumber} Not Found....")
            return False

    def getBankAccountUsingUPIId(self, upiId: str) -> BankAccount:
        for bankAccount in self.__bankAccountbankAccounts:
            if upiId in bankAccount.__upiIdAlloted:
                return bankAccount

    
    def transferMoneyBetweenAccount(self,upiIdOne: str, upiIdTwo: str, amount:int, message: str=""):
        bankAccountNumberOne = self.getBankAccountUsingUPIId(upiIdOne);
        bankAccountNumberTwo = self.getBankAccountUsingUPIId(upiIdTwo);

        if bankAccountNumberOne and bankAccountNumberTwo:
            return self.transferAmountBetweenTwoAccount(bankAccountNumberOne, bankAccountNumberTwo, amount, message)



    


def main():

    bank = Bank()
    upi = UPI()
    temp_upiId = ""
    temp_bankAccount : BankAccount = None
    
    while True:
        os.system("clear")
        print("=============================================")
        print("UPI System")
        print("=============================================")
        print()
        if(temp_bankAccount):  
            temp_daa = temp_bankAccount.getAllDetails() 
            print(f"Welcome {temp_daa['name']}")
            print(f"Bank Account Number: {temp_daa['accountNumber']}")
            print(f"Balance: {temp_daa['balance']}")
            print(f"UPI Id: {temp_upiId}")
            print("---------------------------------------------")
            print()

        print("1. Create Bank Account")
        print("2. Create UPI Id")
        print("3. Deposit Money to Bank")
        print("4. Withdraw Money from Bank")
        print("5. Tranfer Money from Bank to Bank")
        print("6. Tranfer Money from UPI to UPI")
        print("7. Select Bank Account")
        print("8. Exit")
        print()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            os.system("clear")
            tempName = input("Enter your name: ")
            tempBalance = int(input("Enter your balance: "))
            temp_bankAccount = bank.createBankAccount(tempBalance)
            input("Press enter to Contiune....")

        elif choice == 2:
            os.system("clear")
            tempupi = input("Enter UPI ID: ")
            if B .allotUPIId(temp_bankAccount.getBackAccountNumber(), tempupi):
                temp_upiId = tempupi
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")

        elif choice == 3:
            os.system("clear")
            tempAmount = int(input("Enter Amount: "))
            if bank.transcation(temp_bankAccount.__accountNumber, tempAmount, "deposit"):
                print("[Client] Money Deposited....")
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")

        elif choice == 4:
            os.system("clear")
            tempAmount = int(input("Enter Amount: "))
            if bank.transcation(temp_bankAccount.__accountNumber, tempAmount, "withdraw"):
                print("[Client] Money Withdrawn....")
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")


        elif choice == 5:
            os.system("clear")
            tempBankAccountNumber = int(input("Enter Bank Account Number: "))
            tempAmount = int(input("Enter Amount: "))
            if bank.transferAmountBetweenTwoAccount(temp_bankAccount, bank.getBankAccount(tempBankAccountNumber), tempAmount):
                print("[Client] Money Transfered....")
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")

        elif choice == 6:
            os.system("clear")
            tempupi = input("Enter UPI ID: ")
            tempAmount = int(input("Enter Amount: "))
            if bank. upi.transferMoneyBetweenAccount(temp_upiId, tempupi, tempAmount):
                print("[Client] Money Transfered....")
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")

        
        elif choice == 7:
            os.system("clear")
            tempBankAccountNumber = int(input("Enter Bank Account Number: "))
            temp_bankAccount = bank.getBankAccount(tempBankAccountNumber)
            if temp_bankAccount:
                print("[Client] Bank Account Selected....")
            else:
                print("[Client] Something went wrong....")
            input("Press enter to Contiune....")

        elif choice == 8:
            os.system("clear")
            break

        


            







    
if __name__ == "__main__":
    main()