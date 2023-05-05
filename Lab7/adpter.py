# Existing payment gateway interfaces

class PaymentGatewayA:
    def make_payment(self, amount):
        print(f"Payment Gateway A: Making payment of {amount} USD")

class PaymentGatewayB:
    def pay(self, amount):
        print(f"Payment Gateway B: Paying {amount} USD")


# Target interface for the online payment system

class PaymentGateway:
    def process_payment(self, amount):
        pass


# Adapters for integrating PaymentGatewayA and PaymentGatewayB

class PaymentGatewayAAdapter(PaymentGateway):
    def __init__(self, gateway_a):
        self.gateway_a = gateway_a

    def process_payment(self, amount):
        self.gateway_a.make_payment(amount)

class PaymentGatewayBAdapter(PaymentGateway):
    def __init__(self, gateway_b):
        self.gateway_b = gateway_b

    def process_payment(self, amount):
        self.gateway_b.pay(amount)


# Client code with menu card

def display_menu():
    print("=== Menu Card ===")
    print("1. Payment Gateway A")
    print("2. Payment Gateway B")
    print("3. Exit")
    print("=================")

def process_payment(payment_gateway, amount):
    payment_gateway.process_payment(amount)

# Create instances of existing payment gateways
gateway_a = PaymentGatewayA()
gateway_b = PaymentGatewayB()

# Create adapters for PaymentGatewayA and PaymentGatewayB
adapter_a = PaymentGatewayAAdapter(gateway_a)
adapter_b = PaymentGatewayBAdapter(gateway_b)

# Menu loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter payment amount: "))
        process_payment(adapter_a, amount)  # Use PaymentGatewayA
    elif choice == '2':
        amount = float(input("Enter payment amount: "))
        process_payment(adapter_b, amount)  # Use PaymentGatewayB
    elif choice == '3':
        print("Thank you for using the payment system!")
        break
    else:
        print("Invalid choice. Please try again.")
