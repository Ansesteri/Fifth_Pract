class Pet:
    """V-Pet"""
    total = 0

    @staticmethod
    def status():
        print('Total number of animals', Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1
    
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "" or new_name == " ":
            print("Name of animal can`t be valid stroke.")
        else:
            self.__name = new_name
            print("Name has successfully changed.")

    def talk(self):
        print("My name is", self.__name)

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