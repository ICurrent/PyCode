import turtle
turtle.title('OLYMPICS')

turtle.bgcolor('black')
turtle.hideturtle()

turtle.goto(0, 100)

turtle.pendown()
turtle.color('white')
turtle.write("OLYMPICS", align='center', font=('cursive', 40, 'bold'))
#turtle.pencolor('blue')
#turtle.write("OLYMPICS", align='center', font=('cursive', 39, 'bold'))


turtle.pensize(5)
turtle.pencolor('white')
turtle.penup()
turtle.goto(-70,0)
turtle.pendown()
turtle.circle(40)


turtle.pencolor('red')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(40)


turtle.pencolor('yellow')
turtle.penup()
turtle.goto(70,0)
turtle.pendown()
turtle.circle(40)

turtle.pencolor('green')
turtle.penup()
turtle.goto(-35,-50)
turtle.pendown()
turtle.circle(40)

turtle.pencolor('orange')
turtle.penup()
turtle.goto(35,-50)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(0, -120)
turtle.pendown()
turtle.color('white')
turtle.write("2022", align='center', font=('impact', 39))


turtle.mainloop()