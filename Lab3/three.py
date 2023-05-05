# Builder Design Pattern

import os


class Car:
    def __init__(self):
        self._make = None
        self._model = None
        self._year = None
        self._engine = None
        self._wheels = None
        self._fuel = None
    def __str__(self):
        return '{} {} {} with {} engine {} and {} wheels'.format(self._year, self._make, self._model, self._fuel,self._engine, self._wheels)

class CarBuilder:
    def __init__(self):
        self._car = Car()
    def build_make(self, make):
        self._car._make = make
        return self
    def build_model(self, model):
        self._car._model = model
        return self
    def build_year(self, year):
        self._car._year = year
        return self
    def build_engine(self, engine):
        self._car._engine = engine
        return self
    def build_wheels(self, wheels):
        self._car._wheels = wheels
        return self

    def build_fuel(self):
        self._car._fuel = 'Petrol'
        return self

    def build(self):
        return self._car

class ElectricCarBuilder:
    def __init__(self):
        self._car = Car()
    def build_make(self, make):
        self._car._make = make
        return self
    def build_model(self, model):
        self._car._model = model
        return self
    def build_year(self, year):
        self._car._year = year
        return self
    def build_engine(self, engine):
        self._car._engine = engine
        return self
    def build_wheels(self, wheels):
        self._car._wheels = wheels
        return self
    def build_fuel(self):
        self._car._fuel = 'Electric'
        return self

    def build(self):
        return self._car


class CarDirector:
    def __init__(self, builder):
        self._builder = builder
    def construct(self):
        buildMake = input("Enter Make: ")
        buildModel = input("Enter Model: ")
        buildYear = int(input("Enter Year: "))
        buildEngine = input("Enter Engine: ")
        buildWheels = int(input("Enter Wheels: "))

        input("The Car will be built by the Factory. \nPress Enter to continue...\n\n")

        return (self._builder.build_make(buildMake).build_model(buildModel).build_year(buildYear).build_engine(buildEngine).build_wheels(buildWheels).build_fuel().build())

class ElectricCarDirector:
    def __init__(self, builder):
        self._builder = builder
    def construct(self):
        buildMake = input("Enter Make: ")
        buildModel = input("Enter Model: ")
        buildYear = int(input("Enter Year: "))
        buildEngine = input("Enter Engine: ")
        buildWheels = int(input("Enter Wheels: "))

        input("The Car will be built by the Factory. \nPress Enter to continue...\n\n")


        return (self._builder.build_make(buildMake).build_model(buildModel).build_year(buildYear).build_engine(buildEngine).build_wheels(buildWheels).build_fuel().build())


while True:
    os.system('clear')
    print("Welcome to the Factory Design Pattern")
    print("1. Build a Car")
    print("2. Build an Electric Car")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system('clear')
        print("Building a Car...")

        
        builder = CarBuilder()
        director = CarDirector(builder)
        car = director.construct()
        print(car)


        input("Press Enter to continue...\n\n")
    elif choice == 2:
        os.system('clear')
        print("Building an Electric Car...")
        builder = ElectricCarBuilder()
        director = ElectricCarDirector(builder)
        car = director.construct()
        print(car)
        input("Press Enter to continue...\n\n")
    elif choice == 3:
        break
    else:
        print("Invalid Choice")

# Path: sem4/dp/factory_design/four.py