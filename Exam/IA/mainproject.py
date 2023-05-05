from project import *
import os

def main():
    tempObj = None
    # level1Choice = 0
    # level2Choice = 0
    currentCusine = ""

    

    while True:
        if currentCusine != "":
            while True:
                os.system("clear")
                print("Current Cuisine: " + currentCusine)
                foodList : list = tempObj.dishes;
                # print(foodList)
                cind = 0
                for food in foodList:
                    cind+=1
                    print(f"{cind}. {food['name']}")

                print("0. Back to Main Menu")
            
                secondChoice = int(input("Enter your choice: "))

                if secondChoice == 0:
                    print("here2")
                    input("Press Enter to continue...")
                    currentCusine = ""
                    break


                foodName = input("Enter the name of the food:")
                if secondChoice > 0:
                    tempObj.get_food_factory(foodList[secondChoice-1]['name'],foodList ).cook(foodName);

                input("Press Enter to continue...")

                
        os.system("clear")
        print("-----------------------")
        print("Welcome to Food Counter")
        print("-----------------------")
        print("Our Cuisine: ")
        print("1. Western Food")
        print("2. Indian Food")
        print("3. South Asian Food")

        

        choice = int(input("Enter your choice: "))

        if choice == 1:
            currentCusine = "Western"
            tempObj = WesternFoodFactory()

        elif choice == 2:
            currentCusine = "Indian"
            tempObj = IndianFoodFactory()

        elif choice == 3:
            currentCusine = "South Asian"
            tempObj = SouthAsianFoodFactory()

        

if __name__ == "__main__":
    main()