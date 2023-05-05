import math
import os
from databaseConnection import Database, User, Bank


def main():
    user : User = None
    db : Database = Database()
    bank : Bank = Bank()

    while True:
        os.system("clear")
        print(f"----Welcome to the {db.bank.name}----")
        if(user != None):
            print(f"[User]: \nId: {user.id} \nName: {user.name} \nBank Balance: {user.bankBalance}\nConnection Status: {'Connected' if user.getConnectionStatus() else 'Disconnected'}")
            print("---------------------------------")
        print("1. Add User")
        print("2. Credit Amount")
        print("3. Debit Amount")
        print("4. Get Bank All Users")
        print("5. Select User")
        print("6. Toggle Connection")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            os.system("clear")
            db.bank.addUser()
            input("Press Enter to Continue...")

        elif choice == 2:
            os.system("clear")
            if(user == None):
                print("Please Select User First!")
                input("Press Enter to Continue...")
                continue
            
            if(user.getConnectionStatus()):
                print("[Connection]: You're already in Mid-Transaction!")
                tempchoice = input("[Connection]: Do you want to Disconnect?[Y/n] -  ")
                if(tempchoice == "Y" or tempchoice == "y"):
                    user.disconnect()
                    print("[Connection]: User Disconnected!")
                    
                input("Press Enter to Continue...")
                continue

            else: 
                amount = int(input("Enter Amount to Credit: "))
                user.connection.credit(db, user, amount)

                input("Press Enter to Continue...")
        
        elif choice == 3:
            os.system("clear")
            if(user == None):
                print("Please Select User First!")
                input("Press Enter to Continue...")
                continue

            if(user.getConnectionStatus()):
                print("[Connection]: You're already in Mid-Transaction!")
                tempchoice = input("[Connection]: Do you want to Disconnect?[Y/n] -  ")
                if(tempchoice == "Y" or tempchoice == "y"):
                    user.disconnect()
                    print("[Connection]: User Disconnected!")
                    
                input("Press Enter to Continue...")
                continue
            else:
                amount = int(input("Enter Amount to Debit: "))
                user.connection.debit(db, user, amount)

                input("Press Enter to Continue...")

        elif choice == 4:
            os.system("clear")
            db.bank.getAllUsers()

            input("\nPress Enter to Continue...")

        elif choice == 5:
            os.system("clear")
            user = db.bank.selectUser()

            input("Press Enter to Continue...")

        elif choice == 6:
            os.system('clear')
            if(user == None):
                print("Please Select User First!")
                input("Press Enter to Continue...")
                continue
            user.disconnect() if user.getConnectionStatus() else user.connect()
            print(f"Connection Status Now: {'Connected' if user.getConnectionStatus() else 'Disconnected'}")
            input("Press Enter to Continue...")

        elif choice == 7:
            os.system("clear")
            print("Thank You for using our Bank!")
            break


if __name__ == "__main__":  
    main()