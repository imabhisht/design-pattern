class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, "Manager")
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def remove_employee(self, employee):
        self.subordinates.remove(employee)

    def display_info(self):
        super().display_info()
        print("Subordinates:")
        for subordinate in self.subordinates:
            subordinate.display_info()


class LeafEmployee(Employee):
    def __init__(self, name):
        super().__init__(name, "Employee")


# Client code
# Create employees
ceo = Manager("John (CEO)")
cto = Manager("Alice (CTO)")
cfo = Manager("Bob (CFO)")
employee1 = LeafEmployee("Mike (Developer)")
employee2 = LeafEmployee("Sara (Developer)")
employee3 = LeafEmployee("Tom (Accountant)")

# Compose the organizational structure
ceo.add_employee(cto)
ceo.add_employee(cfo)
cto.add_employee(employee1)
cto.add_employee(employee2)
cfo.add_employee(employee3)

# Display organizational structure
ceo.display_info()