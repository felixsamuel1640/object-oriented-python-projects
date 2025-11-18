class Flyer:
    def fly(self):
        print("This animal can fly")

class Swimmer:
    def swim(self):
        print("This animal can swim")

class Duck(Flyer, Swimmer):
    pass


duck = Duck()

duck.fly()
duck.swim()

