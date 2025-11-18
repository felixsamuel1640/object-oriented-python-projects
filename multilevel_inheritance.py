class Animal:
    def eat(self):
        print("This animal is eating")

class Mammal(Animal):
    def walk(self):
        print("This animal is walking")

class Dog(Mammal):
    def bark(self):
        print("This dog is barking")


dog = Dog()

dog.eat()
dog.walk()
dog.bark()

