# Game to geuss the random number
import random
computer = random.randint(1,10)
geuss = False
counter = 0
while not geuss:
    usernum = int(input("Enter number between 1 and 10: "))
    counter = counter +1
    if usernum == computer:
        geuss = True
    elif usernum < computer:
        print("too low!!")
    else:
        print("too high!!")

    if counter > 2:
        print("Too many guesses!!")
        break

if geuss:
    print("You got it!!")
else:
    print("You lost !!")