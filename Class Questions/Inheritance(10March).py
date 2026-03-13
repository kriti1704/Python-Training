# Types of inheritance
# 1 Single inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d1=Dog()
d1.eat()
d1.bark()

# 2 Multilevel inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")

p1=Puppy()
p1.eat()
p1.bark()
p1.weep()

# 3 Hierarchical inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d1=Dog()
c1=Cat()
d1.eat()
d1.bark()
c1.eat()
c1.meow()

# 4 Multiple inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Bird:
    def fly(self):
        print("Bird is flying")

class Eagle(Animal, Bird):
    def hunt(self):
        print("Eagle is hunting")

e1=Eagle()
e1.eat()
e1.fly()
e1.hunt()

# 5 Hybrid inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal): #hierarchical inheritance
    def bark(self):
        print("Dog is barking")

class Cat(Animal): #hierarchical inheritance
    def meow(self):
        print("Cat is meowing")

class Puppy(Dog): #multilevel inheritance
    def weep(self):
        print("Puppy is weeping")

p1=Puppy()
p1.eat()
p1.bark()
p1.weep()
