import os
class CPU:
    def freeze(self):
        print("Freezing CPU...")

    def jump(self, position):
        print(f"Jumping to position {position}...")

    def execute(self):
        print("Executing command...")

class Memory:
    def load(self, address, data):
        print(f"Loading {data} into address {address}...")

class HardDrive:
    def read(self, sector, size):
        print(f"Reading {size} bytes from sector {sector}...")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("Starting computer...")
        self.cpu.freeze()
        self.memory.load(0, "bootloader")
        self.cpu.jump(0)
        self.cpu.execute()
        self.memory.load(0, "operating system")
        self.cpu.jump(0)
        self.cpu.execute()

    def read_data(self, sector, size):
        self.hard_drive.read(sector, size)

computer = ComputerFacade()

while True:
    os.system("clear")
    print("1. Start computer")
    print("2. Read data from hard drive")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system("clear")
        computer.start()
        input("Press Enter to Contiune...")
    elif choice == 2:
        os.system("clear")
        sector = int(input("Enter sector number: "))
        size = int(input("Enter number of bytes to read: "))
        computer.read_data(sector, size)
        input("Press Enter to Contiune...")
    elif choice == 3:
        break
    else:
        print("Invalid choice")
