# State Desgin Pattern
# Implement State design pattern for the Following use

# A Mobile has 3 different types of alert states such as rining, vibration and silent.
# Each Alert type has different style of giving alert to mobile user. User has to set its alert type.
# and accordingly they will get specific alert.


# State Design Pattern Program

from abc import ABC, abstractmethod

class MobileState(ABC):
    @abstractmethod
    def alert(self):
        pass

class Ringing(MobileState):
    def alert(self):
        print("Ringing Alert")

class Vibration(MobileState):
    def alert(self):
        print("Vibration Alert")

class Silent(MobileState):
    def alert(self):
        print("Silent Alert")

class Mobile:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def alert(self):
        self.state.alert()

if __name__ == "__main__":
    mobile = Mobile()
    mobile.setState(Ringing())
    mobile.alert()

    mobile.setState(Vibration())
    mobile.alert()

    mobile.setState(Silent())
    mobile.alert()

# Output:
# Ringing Alert
# Vibration Alert
# Silent Alert



