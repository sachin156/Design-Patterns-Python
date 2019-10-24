class Dog:
    
    def speak(self):
        return "Bark"
    def __str__(self):
        return "Dog"

class DogFactory:

    def getpet(self):
        return Dog()
    
    def getfood(self):
        return "Dog Food"

class PetFactory:
    
    def __init__(self,petfactory=None):
        self.petfactory=petfactory

    def showpet(self):
        petname=self.petfactory.getpet()
        petfood=self.petfactory.getfood()

        print(petname)
        print(petfood)

factory=DogFactory()

shopfactory=PetFactory(factory)
shopfactory.showpet()



