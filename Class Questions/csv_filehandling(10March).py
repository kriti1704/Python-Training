import csv
from datetime import date

#writer
""" file = open("expense.csv",'w',newline="")
w=csv.writer(file)
w.writerow(["Date","Expense","Amount"])
w.writerows(
    [
        [date.today(),"Food",200],
        [date.today(),"Transport",100],
        [date.today(),"Entertainment",300]
    ]
)
file.close() """

#reader
file = open("expense.csv",'r',newline="")
r=csv.reader(file)
#print(list(r))
for row in r:
    print(row)
file.close() 
