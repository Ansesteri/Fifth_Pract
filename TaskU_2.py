class Pet:
    """V-Pet"""
    def __init__(self):
        print('An animal was born')
    def talk(self):
        print("Hi, I am an animal!")

def main():
    pet1 = Pet()
    pet1.talk()
    pet2 = Pet()
    pet2.talk()

main()