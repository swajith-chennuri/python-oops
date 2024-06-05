class Animal:
    def __init__(self,name,location,age):
        self.name=name
        self.location=location
        self.age=age
    def description(self):
        print(f"This is {self.name} and iam from {self.location} and iam {self.age}")
class Cat(Animal):
    def __init__(self,name,breed,age,location):
        super(). __init__(name,age,location)
        self.breed=breed
    def description(self):
        print(f"This guy {self.name} he is so cute and he is {self.age} old. His breed is {self.breed} and is {self.location}")      
cat=Cat(name="bisshu", age= 3, breed="pershian", location="bhemaram")
cat.description()