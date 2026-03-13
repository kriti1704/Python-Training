#file handling

#write data to file
""" file=open("temp.txt",'w')
file.write("I am the first line!")
file.writelines(["\nI am the second line!","\nI am the third line!\n"])
file.close()
 """
#read data from file using read()
""" file=open("temp.txt",'r')
print(file.read())
file.close()
 """
#readline() method
""" file=open("temp.txt",'r')
print(file.readline()) #reads the first line only
print(file.readline()) #reads the second line only
file.close() """

#readlines() method
""" file=open("temp.txt",'r')
print(file.readlines()) #reads all the lines and returns a list
file.close() """

#write+read mode
""" file=open("temp.txt",'w+')
file.write("I am the first line!")
file.writelines(["\nI am the second line!","\nI am the third line!\n"])
file.seek(0) #moves the cursor to the beginning of the file
print(file.read())
file.close() """

#append mode
""" file = open("temp.txt",'a')
file.write("I am the appended line!")
file.writelines(["\nI am learning pyhton!","\nI am enjoying it!\n"])
file.close() """