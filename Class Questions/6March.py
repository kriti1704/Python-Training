#Functions 1

""" #Global Variables
a=500

#Local Variables
def fname():
    global a
    a=100
    b=150
    print(a+b)
    def fname1():
        nonlocal b
        b=200
    
    fname1()
    print(b)

fname() """

#2 calculating the product of a list of numbers
""" def product(a):
    ans=1
    for i in a:
        ans=ans*i
    return ans

a=[1,2,3,4]
print(product(a)) """

# 3 print initial character present in the string
""" s = input("Enter a string: ")
c = input("Enter a character: ")

def initial_character(s, c):
    if c in s:
        return s.index(c)
    else:
        return -1

result = initial_character(s, c)

if result != -1:
    print(result)
else:
    print("Character not found in the string") """

# 4 Packing
""" def packing(t,*args):
    print(t)
    return args

print(packing(1,2,3,4,5)) """

# 5 Double packing
""" def double_packing(**args):
    return args

print(double_packing(a=1, b=2, c=3, d=4, e=5)) """

# 6 Unpacking
""" def unpacking(a, b, c):
    print(a,b,c)

unpacking(*"hel") """

# 7 Unpacking a dictionary
def unpacking_dict(a, b, c):
    print(a,b,c)

unpacking_dict(**{"a":1, "b":2, "c":3})



