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
class College:
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
print(s2.name,s2.age,s2.course,s2.c_name,s2.location,s2.code)


