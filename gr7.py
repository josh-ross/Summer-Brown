import turtle
win = turtle.Screen()
pablo1=turtle.Turtle()

for a in range(4):
	pablo1.forward(100)
	pablo1.left(90)
for b in range(3):
	pablo1.color('blue')
	pablo1.forward(100)
	pablo1.right(120)
pablo1.up()
pablo1.goto (0,100)
pablo1.down()
for c in range(3):
	pablo1.color('red')
	pablo1.forward(100)
	pablo1.left(120)
pablo1.up()
pablo1.goto (100,0)
pablo1.down()
for d in range(4):
	pablo1.color('yellow')
	pablo1.forward(58)
	pablo1.left(60)
pablo1.up()
pablo1.goto (0,0)
pablo1.down()
for e in range(4):
	pablo1.color('green')
	pablo1.right(60)
        pablo1.forward(58)
win.exitonclick()
