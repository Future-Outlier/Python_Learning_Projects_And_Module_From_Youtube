# if there's a same name in child class and upper level class
# programming will override the upper level class and use the child object
# super class to avoid unnecessay operation for coding system

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I can't make noise...")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # use "super().__init__" represents the object of parents
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 34, "green")
c.show()
d = Dog("Jill", 25)
d.show()
