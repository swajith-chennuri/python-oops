class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self,lang):
        print(f"Hello, my name is {self.name} and my age is {self.age} and my languange is {lang}")

# Create an instance of the Person class
Swajith = Person(name="swajith", age=20)

# Call the speak method on the instance
Swajith.speak(lang)
