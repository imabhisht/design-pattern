import os
import pickle

#Caretaker
class Editor:
    def __init__(self):
        self.content = ""

    def add_content(self, new_content):
        self.content += new_content

    def get_content(self):
        return self.content

    def create_memento(self):
        return pickle.dumps(self.__dict__)

    def restore_memento(self, memento):
        self.__dict__ = pickle.loads(memento)

#Memento
class History:
    def __init__(self):
        self.undo_stack = []

    def save(self, memento):
        self.undo_stack.append(memento)

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        memento = self.undo_stack.pop()
        return memento

editor = Editor()
history = History()

#Originator
while True:
    os.system("clear")
    print("1. Add content")
    print("2. Undo")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system("clear")
        new_content = input("Enter new content: ")
        history.save(editor.create_memento())
        editor.add_content(new_content)
        print(f"Current content: {editor.get_content()}")
        input("Press Enter to continue...")
    elif choice == 2:
        os.system("clear")
        memento = history.undo()
        if memento:
            editor.restore_memento(memento)
            print(f"Current content: {editor.get_content()}")
        input("Press Enter to continue...")
    elif choice == 3:
        break
    else:
        print("Invalid choice.")
