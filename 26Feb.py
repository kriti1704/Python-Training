#Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333 (always float)
print("Modulus:", a % b)         # 1 (remainder)
print("Floor Division:", a // b) # 3 (removes decimal)
print("Exponent:", a ** b)  

#Relational Operators
x = 5
y = 5
z = 10

print(x == y)   
print(x != z)  
print(x > z)    
print(x < z)   
print(x >= 5)   
print(x <= 4)        

#Assignment Operators
num = 10

num += 5   
print(num) 

num -= 2
print(num)

num *= 2
print(num) 

num /= 2
print(num)

num //= 2
print(num) 

num **= 2
print(num) 

#Logical Operators
age = 20
has_id = True

print(age >= 18 and has_id)  
print(age < 18 or has_id)   
print(not has_id) 

#Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  
print(a is not c)  

#Membership Operators
name = "Kriti"

print("K" in name)       
print("Z" not in name)   

nums = [1,2,3,4]
print(3 in nums)

#Bitwise Operators
a = 5   # 0101
b = 3   # 0011

print(a & b)  
print(a | b)  
print(a ^ b)  
print(~a)     
print(a << 1) 
print(a >> 1) 