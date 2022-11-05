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
        print("My name is", self.__name,
        ", and I fell myself", self.mood)
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    
    def play(self, fun = 4):
        print("Yahoooo!!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "amazing"
        elif 5 <= unhappiness <= 10:
            m = "good"
        elif 11 <= unhappiness <= 15:
            m = "bad"
        else:
            m = "awful"
        return m

def main():
    pet_name = input("How will you call your animal?: ")
    pet = Pet(pet_name)
    
    choice = None
    while choice != "0":
        print \
        ("""
        My animal
        
        0 - Exit
        1 - Discover mood of your animal
        2 - Feed animal
        3 - Play with animal
        """)
        choice = input("Your choice: ")
        print()
        if choice == '0':
            print("Goodbye.")
        elif choice == '1':
            pet.talk()
        elif choice == '2':
            pet.eat()
        elif choice == '3':
            pet.play()
        else:
            print("Sorry, but we don`t have this option", choice)

main()