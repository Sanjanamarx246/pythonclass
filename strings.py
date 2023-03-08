# python file for strings
name = input("enter your name")
counter = 0
while counter < len(name):
    print(name[counter])
    counter = counter + 1

strList = ["Hello", name,"You are great at coding"]
toPrint = " ".join(strList)
print(toPrint)
