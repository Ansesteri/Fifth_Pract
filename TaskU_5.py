class Pet:
    """V-Pet"""
    total = 0

    @staticmethod
    def status():
        print('Total number of animals', Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1
    def __str__(self):
        ans = "Object class Pet\n"
        ans += 'name: ' + self.name + '\n'
        return ans
    def talk(self):
        print("My name is", self.name)

def main():
    print('Access to attribute of class Pet.total:', end = " ")
    print(Pet.total)

    print("Creating animals.")
    pet1 = Pet("Animal 1")
    pet2 = Pet("Animal 2")
    pet3 = Pet("Animal 3")

    Pet.status()

    print("Access to attribute of class through odject:", end = " ")
    print(pet1.total)    

main()