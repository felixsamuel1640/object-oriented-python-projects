# Object-Oriented Python Projects

A collection of Python projects built while learning and practicing 
**Object-Oriented Programming (OOP)**.  
This repository includes simple but foundational examples demonstrating 
concepts such as **classes**, **inheritance**, **constructor chaining**, 
**method overriding**, and more.

These projects were created as part of my journey transitioning into tech 
and strengthening my Python fundamentals.

---

## 🚀 Projects in This Repository

### 1. **Basic Inheritance – Animal Sounds**
A simple program showing how child classes inherit from a parent class and 
override methods.

```python
class Animal:
    def sound(self):
        return "This animal makes a sound"

class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

dog = Dog()
cat = Cat()

print(dog.sound()) 
print(cat.sound())
2. Multiple Inheritance – Device Info
A demonstration of how a class can inherit features from more than one 
parent.
class Device:
    def device_info(self):
        return "I am a device."

class Computer:
    def computer_info(self):
        return "I am a computer."

class Laptop(Device, Computer):
    def laptop_info(self):
        return "I am a laptop."

laptop = Laptop()
print(laptop.device_info())
print(laptop.computer_info())
print(laptop.laptop_info())
3. Multilevel Inheritance – Electronics Hierarchy
Shows how inheritance can be extended across multiple levels.
class Electronic:
    def info(self):
        return "This is an electronic item."

class Phone(Electronic):
    def phone_info(self):
        return "This is a phone."

class Smartphone(Phone):
    def smartphone_info(self):
        return "This is a smartphone."

smartphone = Smartphone()
print(smartphone.info())
print(smartphone.phone_info())
print(smartphone.smartphone_info())
📚 What I’m Learning
Understanding classes and objects
Writing clean, reusable code
Inheritance and method overriding
Multiple and multilevel inheritance
Preparing for more advanced topics like:
super()
Polymorphism
Encapsulation
Project structuring
🛠️ How to Run
Clone the repository and run any .py file:
git clone 
https://github.com/YOUR-USERNAME/object-oriented-python-projects.git
cd object-oriented-python-projects
python filename.py
🎯 Future Improvements
Add more real-world OOP projects
Implement super() across classes
Add docstrings and type hints
Add unit tests
Build a full OOP mini-application
🙌 About Me
I’m Michael Carrington, transitioning from logistics into tech.
I’m currently learning Python, building projects, and growing my backend 
and AI engineering skills.
