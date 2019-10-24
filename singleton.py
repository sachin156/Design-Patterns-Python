class Borg:
    globaldict={}
    def __init__(self):
        self.__dict__=self.globaldict

class Singleton(Borg):
    def __init__(self,**kwargs):
        # Borg.__init__(self)
        Borg.globaldict.update(kwargs)
    
    def __str__(self):
        return str(self.globaldict)

x=Singleton(p="polymorphism")
print(x)

y=Singleton(I="Inheritance")
print(y)

