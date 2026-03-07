#1 Factorial of a number using recursion
""" import sys
sys.setrecursionlimit(2000)
sys.set_int_max_str_digits(50000)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}") """

#2 Write a function to add minimum 2 and maximum 5 numbers using recursion
""" def add_numbers(*args):
    if len(args) < 2 or len(args) > 5: #limit
        print("Not within range")
        return None
    if len(args) == 2: #base case
        return args[0] + args[1]
    else:
        return args[0] + add_numbers(*args[1:])

numbers = []
n = int(input("How many numbers do you want to add (2-5)? "))
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"The sum of the numbers is: {add_numbers(*numbers)}") """

#3 Write a programn to find out the sum of digits of a number using recursion
n=input("Enter a number: ")
def sum(n):
    if len(n) == 1:
        return int(n)
    return int(n[0]) + sum(n[1:])

print(f"The sum of the digits of {n} is {sum(n)}")
