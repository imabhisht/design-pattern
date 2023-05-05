from abc import abstractmethod

class Chief:
    @abstractmethod
    def cook(self, dishName):
        print("[Cook]: Cooking " + dishName)
        pass