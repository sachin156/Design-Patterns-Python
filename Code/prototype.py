import copy
class Prototype:

    def __init__(self):
        self.objects={}
    
    def register_object(self,name,obj):
        self.objects[name]=obj
    
    def unregister_object(self,name):
        del self.objects[name]
    
    def clone(self,name,**attr):
        obj=copy.deepcopy(self.objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name="tesla"
        self.color="Red"
        self.options="ex"
    
    def __str__(self):
        return (self.name,self.color,self.options)

c=Car()
prototype=Prototype()
prototype.register_object("tesla",c)

c1=prototype.clone("tesla")
print(c1)


