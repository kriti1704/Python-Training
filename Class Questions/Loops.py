#while loop
""" i=50
while i>=40:
    print(i,end=" ")
    i-=1 """

""" i=0
while i<=20:
    print(i)
    i=i+2 """

#reverse a no
""" n=eval(input("enter a number:"))
rev=0
while(n>0):
    last=n%10
    rev= rev*10 + last
    n=n//10

print(rev) """

#reverse a string
""" n=input("enter a string:")
rev=''
i=-1
while i>=(-len(n)):
    rev += n[i]
    i=i-1

print(rev) """

#sum of first 10 even no
""" i=0
sum=0
while i<=10:    
    sum+=i
    i=i+2
print(sum) """

#print a table
""" n=int(input("Enter a number:"))
i=1
while i<=10:
    print(n," x ",i," = ",n*i)
    i=i+1 """

#for loop
""" a={10,20,30,40,50}
for i in range(1,10):
    print(i) """

#replacing space with _ in a string
name="Kriti Jain"
s=''
for i in name:
    if i==' ':
        s+='_'
    else:
        s+=i
print(s)