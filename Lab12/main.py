# State design pattern example with a simple vending machine

# Context
class VendingMachine:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def request(self):
        if self._state is not None:
            self._state.handle_request()

# Abstract State
class VendingMachineState:
    def handle_request(self):
        pass

# Concrete States
class ReadyState(VendingMachineState):
    def handle_request(self):
        print("Vending machine is ready. Please select an item.")

class DispensingState(VendingMachineState):
    def handle_request(self):
        print("Vending machine is dispensing the selected item.")

class EmptyState(VendingMachineState):
    def handle_request(self):
        print("Vending machine is empty. Please refill the items.")

# Client
def main():
    # Create a vending machine
    vending_machine = VendingMachine()

    # Set initial state to ReadyState
    vending_machine.set_state(ReadyState())

    while True:
        print("1. Select item")
        print("2. Dispense item")
        print("3. Refill items")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vending_machine.request()
        elif choice == "2":
            vending_machine.set_state(DispensingState())
            vending_machine.request()
            vending_machine.set_state(ReadyState())
        elif choice == "3":
            vending_machine.set_state(EmptyState())
            vending_machine.request()
            vending_machine.set_state(ReadyState())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
