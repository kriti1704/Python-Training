# four pillars of OOPS
# 1. Abstraction

from abc import abstractmethod

class Car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("car is starting")

c1=Car()
c1.start()

# 2. Encapsulation
class Student:
    def __init__(self,name,age):
        self.__name=name #private attribute
        self.__age=age

    def display(self):
        print("Name:",self.__name)
        print("Age:",self.__age)

s1=Student("Alice",20)
s1.display()

# 3. Inheritance
class Parent:
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    def child_method(self):
        print("This is child method")

c1=Child()
c1.parent_method()
c1.child_method()

# 4. Polymorphism(method overloading)
class Bird:
    def sound(self):
        print("Bird chirps")

class Dog:
    def sound(self):
        print("Dog barks")

b1=Bird()
d1=Dog()
b1.sound()
d1.sound()

#Operator overloading
class Number:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,other): #dunder method for + operator
        return self.value + other.value

n1=Number(5)
n2=Number(10)
print(n1+n2) # + is used to call __add__ method

#Method overriding
class Parent:
    def show(self):
        print("This is a parent class")

class Child(Parent):
    def show(self):
        print("This is a child class")

c=Child()
c.show() # child class method will be called instead of parent class method
