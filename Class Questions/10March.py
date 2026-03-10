# Bank
""" class Bank:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} credited.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} debited.")
    
    def show(self):
        print(f"Current balance: {self.balance}")

b1 = Bank("Alice", 101, 12789)
b2 = Bank("Bob", 102, 98761)
b3 = Bank("Charlie", 103, 555555)
b1.deposit(5000)
b2.withdraw(10000)
b3.show() """

# super method
""" class Parent:
    def show(self):
        print("This is a parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is a child class")

c=Child()
c.show()
 """

# Employee Manager(super method)
""" class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    
    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

m1=Manager("Alice",50000,"IT")
m1.show() """

#property method
class Circle:
    def __init__(self):
        radius = int(input("Enter radius: "))
        self.radius = radius
    
    @property
    def area(self):
        return 3.14*self.radius**2
    
    @property
    def circumference(self):
        return 2*3.14*self.radius

c1=Circle()
print(c1.area)
print(c1.circumference)

