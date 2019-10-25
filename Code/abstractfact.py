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


class Cat:
    
    def speak(self):
        return "Meow"
    def __str__(self):
        return "Cat"

class CatFactory:

    def getpet(self):
        return Cat()
    
    def getfood(self):
        return "Cat Food"



class PetFactory:
    
    def __init__(self,petfactory=None):
        self.petfactory=petfactory

    def showpet(self):
        petname=self.petfactory.getpet()
        petfood=self.petfactory.getfood()

        print(petname)
        print(petfood)

factory=DogFactory()
factory1=CatFactory()

shopfactory=PetFactory(factory)
shopfactory1=PetFactory(factory1)

shopfactory.showpet()
shopfactory1.showpet()


