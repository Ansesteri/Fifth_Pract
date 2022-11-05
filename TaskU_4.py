class Pet:
    """V-Pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __str__(self):
        ans = "Object class Pet\n"
        ans += 'name: ' + self.name + '\n'
        return ans
    def talk(self):
        print("My name is", self.name)

def main():
    pet1 = Pet("Bobik")
    pet2 = Pet("Meowie")
    print(pet2)

main()