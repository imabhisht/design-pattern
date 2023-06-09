class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"ConcreteFlyweight: {self.intrinsic_state}, {extrinsic_state}")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, intrinsic_state):
        if intrinsic_state not in self.flyweights:
            self.flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)
        return self.flyweights[intrinsic_state]


def main():
    flyweight_factory = FlyweightFactory()

    flyweight = flyweight_factory.get_flyweight("A")
    flyweight.operation(1)

    flyweight = flyweight_factory.get_flyweight("B")
    flyweight.operation(2)

    flyweight = flyweight_factory.get_flyweight("A")
    flyweight.operation(3)


if __name__ == "__main__":
    main()

# #Flyweight design Pattern

# class Flyweight:
#     def __init__(self, sharedState):
#         self._sharedState = sharedState

#     def operation(self, uniqueState):
#         s = self._sharedState
#         u = uniqueState
#         print("Flyweight: Displaying shared (%s) and unique (%s) state." % (s, u))
# class FlyweightFactory:
#     def __init__(self, initialFlyweights):
#         self._flyweights = {}
#         for state in initialFlyweights:
#             self._flyweights[self.getKey(state)] = Flyweight(state)

#     @staticmethod
#     def getKey(state):
#         return "_".join(sorted(state))

#     def getFlyweight(self, sharedState):
#         key = self.getKey(sharedState)

#         if not self._flyweights.get(key):
#             print("FlyweightFactory: Can't find a flyweight, creating new one.")
#             self._flyweights[key] = Flyweight(sharedState)
#         else:
#             print("FlyweightFactory: Reusing existing flyweight.")

#         return self._flyweights[key]

#     def listFlyweights(self):
#         count = len(self._flyweights)
#         print(f"FlyweightFactory: I have {count} flyweights:")
#         print(self._flyweights)

# def addCarToPoliceDatabase(
#     factory, plates, owner, brand, model, color
# ):
#     print(
#         "Hello officer, this is the information we have for this car:")
#     print(f"Plate: {plates}")
#     print(f"Owner: {owner}")
#     print(f"Brand: {brand}")
#     print(f"Model: {model}")
#     print("Got it, thanks!")
#     print(f"Color: {color}")
# def main():
#     factory = FlyweightFactory(["Chevrolet", "Camaro2018", "pink"])
#     factory.listFlyweights()

#     addCarToPoliceDatabase(
#         factory,
#         "CL234IR",
#         "James Doe",
#         "BMW",
#         "M5",
#         "red",
#     )

#     factory.listFlyweights()

#     addCarToPoliceDatabase(
#         factory,
#         "CL234IR",
#         "James Doe",
#         "BMW",
#         "X1",
#         "red",
#     )

#     factory.listFlyweights()

#     print("Client: Testing with the same user twice.")
#     addCarToPoliceDatabase(
#         factory,
#         "CL234IR",
#         "James Doe",
#         "BMW",
#         "M5",
#         "red",
#     )

#     print("Client: Testing with the same user but different plate.")
#     addCarToPoliceDatabase(
#         factory,
#         "CL234IR",
#         "James Doe",
#         "BMW",
#         "X1",
#         "red",
#     )

#     factory.listFlyweights()



# if __name__ == "__main__":
#     main()