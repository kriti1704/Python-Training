#11
""" a=input('Enter a value:')
if (a.isdigit() and len(a)==3):
    print(a+" is a 3-digit number")
else:
    print(a+" is not a 3-digit number") """

#12
""" a=input("Enter a string:")
if len(a)>5:
    print('string is greater than 5')
else:
    print('string is not greater than 5') """

#13
""" a=int(input('enter a number:'))
if a==0:
    print("Zero")
else:
    print("Not Zero") """

#14
""" age=int(input("Enter your age:"))
id=input("Is id valid(True/False):")
if (age>=18 and id=="True"):
    print("Eligible")
else:
    print("Not Eligible") """

#15
""" a=int(input("Enter a number:"))
if a>=10 and a<=50:
    print("In range")
else:
    print("Not in range") """

#16
""" a=eval(input("Enter first number:"))
b=eval(input("Enter second number:"))
op=input("Enter operator (+ or -):")
if op=='+':
    print(a+b)
else:
    print(a-b) """

#17
""" name="Kriti"
password="1234"
a=input("Enter username:")
b=input("Enter password:")
if a==name and b==password:
    print("Login Successfully!")
else:
    print("Invalid credentials") """

#18
""" a=eval(input("Enter temperature:"))
if a>=25:
    print("Hot")
else:
    print("Cold") """

#19
""" a=input("Enter a number:")
rev =a[::-1]
if a==rev:
    print("Palindrome")
else:
    print("Not palindrome") """

#20
""" a=eval(input("Enter a numnber:"))
if a>100:
    print("Greater than 100")
else:
    print("Not greater than 100") """

#nested-if 1
""" age=int(input("Enter your age:"))
income=eval(input("Enter your income:"))
score=eval(input("Enter your credit score:"))
if age>=21:
    if income>=25000:
        if score>=700:
            print("Loan Approved")
        else:
            print("Loan Rejected (Low Credit Score)")
    else:
        print("Loan Rejected (Low Income)")
else:
    print("Loan Rejected (Age not eligible)") """

#2
""" math=eval(input("Enter marks in math:"))
sci=eval(input("Enter marks in science:"))
eng=eval(input("Enter marks in english:"))
avg=(math+sci+eng)/3
if(math>=40 and sci>=40 and eng>=40):
    if avg>=75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail") """

#3
i=eval(input("Enter your income:"))
if i>500000:
    if i<=1000000:
        print("20% tax")
    else:
        print("30% tax")
else:
    if i>250000:
        print("5% tax")
    else:
        print("no tax")