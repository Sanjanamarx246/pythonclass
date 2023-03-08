from turtle import *

color("teal", "pink")
pensize(5)

begin_fill()
i=0
sides = 1300
while i < sides :
    forward(1)
    left(360/sides)
    i=i+1

end_fill()
done()
