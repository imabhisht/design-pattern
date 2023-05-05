

class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print(f"Leaf {self.name} operation")

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def operation(self):
        print(f"Composite {self.name} operation")
        for child in self.children:
            child.operation()


root = Composite("root")
root.add(Leaf("leaf1"))
root.add(Leaf("leaf2"))

comp = Composite("composite")
comp.add(Leaf("leaf3"))
comp.add(Leaf("leaf4"))

root.add(comp)
root.operation()