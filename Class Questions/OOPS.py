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