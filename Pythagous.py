#ask user a,b,c
from math import(sqrt)
user = input("Enter 'a', 'b' or 'c'")

if user == 'c':
    a= int(input ("enter 'a'"))
    b = int(input("enter 'b'"))
    c = sqrt(a*a+b*b)
    print(c)


if user == 'b':
    c = int(input ("enter 'c'"))
    a = int(input("enter 'a'"))
    b = sqrt(c*c-a*a)
    print(b)

if user == 'a':
    c= int(input ("enter 'c'"))
    b = int(input("enter 'b'"))
    a = sqrt(c*c-b*b)
    print(a)




