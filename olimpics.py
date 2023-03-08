from turtle import*

radius=100
dist=2 * radius + 7.5
pensize(7)

penup()
goto(-200,100)
pendown()
circle(radius)

penup()
forward(dist)
pendown()
circle(radius)

penup()
forward(dist)
pendown()
circle(radius)

penup()
goto(-200 +radius, 100-radius)
pendown()
circle(radius)

penup()
forward(dist)
pendown()
circle(radius)


done()