#OOPS
# class and object
""" class Car: #class
    name="bmw" #attributes
    speed=200
    def run(self): #method
        print("car is running")

c1=Car() #object
print(c1) #address of object
print(Car) #class
print(c1.__dict__) #attributes of object
print(c1.name)
print(c1.speed)
c1.run() """

# 2
""" class College:
    c_name = "JECRC"
    location = "JAIPUR"
    code = "302022"

s1=College()
s2=College()
s1.name="Alice"
s1.age=20
s1.course="B.Tech"
s2.name="Bob" 
s2.age=22
s2.course="M.Tech"

print(s1.name,s1.age,s1.course,s1.c_name,s1.location,s1.code)
print(s2.name,s2.age,s2.course,s2.c_name,s2.location,s2.code) """

# Constructor
""" class Student:
    def __init__(self,name,age,course): #constructor
        self.name=name
        self.age=age
        self.course=course

s1=Student("Alice",20,"B.Tech")
s2=Student("Bob",22,"M.Tech")
print(s1.name,s1.age,s1.course)
print(s2.name,s2.age,s2.course) """

# display method
""" class Student:
    def __init__(self,name,age,course): 
        self.name=name
        self.age=age
        self.course=course

    def display(self): 
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)

s1=Student("Alice",20,"B.Tech")
s2=Student("Bob",22,"M.Tech")
s1.display()
s2.display() """

# Types of methods
# 1 instance method
""" class Student:
    college="JECRC" #class variable
    def __init__(self,name,age,course): 
        self.name=name
        self.age=age
        self.course=course

    def modify(self):
        self.college="NIT" #modifying class variable using instance method

    def display(self): 
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print("College:",self.college)

s1=Student("Alice",20,"B.Tech")
s1.modify()
s1.display() #instance method
s2=Student("Bob",22,"M.Tech")
s2.display()  """

# 2 class method
""" class Student:
    college="JECRC" #class variable

    @classmethod
    def get_college(cls):
        cls.college="NIT" #modifying class variable
        print("College:",cls.college) 

s1=Student()
Student.get_college() #class method
s1.get_college() #class method can be called by object also """

# 3 static method
class Student:
    college="JECRC" #class variable

    @staticmethod
    def info():
        print("This is a student class")
    
    @staticmethod
    def add(a,b):
        print("Sum:",a+b)

Student.info() #static method
s1=Student()
s1.add(10,20) #static method can be called by object also


