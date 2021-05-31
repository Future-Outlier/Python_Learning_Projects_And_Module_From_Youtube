# tutorial : https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim
# str.upper()
# self parameter
# __main__Dog
# pass
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark", self.name)

    def set_age(self, age):
        self.age = age

# if we store the information like this, we will have more trouble when the numbers become big.
dogs = ["Tim", "Bill"]
dogs_age = [32, 14]
# the meaning of class makes you store the data efficiently
