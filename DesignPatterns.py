class Dog:
    
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Bark"

class Cat:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Meow"

def getpet(pet="dog"):
    pets=dict(dog=Dog("hope"),cat=Cat("Peace"))
    return pets[pet]

d=getpet("dog")
print(d.speak())

c=getpet("cat")
print(c.speak())



