#split method 
""" l=['p1.py','first.txt','T3.py','Tk.txt','Tfk.com']
dict={}
for i in l:
    t = i.split('.')

    if t[1] in dict:
        dict[t[1]].append(t[0]) #append in list
    else:
        dict[t[1]] = [t[0]] #create list values 

print(dict)"""

#2
""" s='aaabbaabccc'
ans=''
count=1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        ans += s[i] + str(count)
        count = 1

ans += s[-1] + str(count)
print(ans) """

#3
""" l=[(2+3j),12,'Program','Pyhton',False]
dict={}
for i in l:
    if type(i)==str:
        dict[i] = ''
        for j in i:
            if j in 'aeiouAEIOU':
                dict[i] += j

print(dict) """

#4 Termination statements
""" for i in range(1,11):
    if i==4:
        continue
    print(i)

    if i==7:
        break

    if i==9:
        pass """  