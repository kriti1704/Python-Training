#Types of arguments

# 1 Positional arguments
""" def fname(a, b):
    print(a+b)
fname(1, 2) """

# 2 Default arguments
""" def fname(a, b=5,c=None):
    print(a+b)
fname(1) """

# 3 Keyword arguments
""" def fname(a, b):
    print(a+b)
fname(b=1, a=2) """

# 4 Variable length arguments
""" def fname(*args):
    print(args)
fname(1, 2, 3, 4, 5) """

# form
""" def form(name,email,phone,age=21,*marks):
    print("name:",name)
    print("email:",email)
    print("age:",age)
    print("phone:",phone)   
    print("marks:",marks)

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
marks = []
for i in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)

form(name,email,phone,*marks) """

# factorial
def factorial(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")

# class and object
class car:
    name="bmw"
    