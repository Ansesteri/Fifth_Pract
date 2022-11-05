class Pet:
    """V-Pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def talk(self):
        print("My name is", self.name)

def main():
    pet1 = Pet("Bobik")
    pet1.talk()
    pet2 = Pet("Meowie")
    pet2.talk()
    print("Access to attribute -", pet1.name)
    print(pet2)

main()