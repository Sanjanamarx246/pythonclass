# create list of numbers
# print each number in that list

numList= [2, 4, 6, 8, 10, 12, 14]
for number in numList:
    print(number)
    print(number * number)




# add all the numbers in the list
addition = 0
for number in numList:
    addition= addition + number

print(addition)

multiply = 1
for number in numList:
    multiply = multiply * number

print(multiply)

numList=list(range(10))
print(numList)

#table of three
numList=(range(1,11))
for num in numList:
    print(num)



user = int(input("enter number"))
numList=(range(1,user))
for num in numList:
    print(num)
