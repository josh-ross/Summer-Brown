# Using tkinter in scripts
import Tkinter
import tkMessageBox
import turtle
from sys import exit
win=turtle.Screen()


def star():
	global pablo
	pablo=turtle.Turtle()
	pablo=turtle.Turtle()
	pablo.color('red')
	for a in range(25):
		pablo.forward(200)
		pablo.left(170)
def quit():
	exit(0)

def clear():
	pablo.reset()
        pablo1.reset()
def pent():
	global pablo1
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
	
top = Tkinter.Tk()
top.title("Turtle Star")
top.geometry('200x200+100+100')
b1= Tkinter.Button(top,text='Star')
b2= Tkinter.Button(top,text='Penta')
b3=Tkinter.Button(top,text='Quit')
b4=Tkinter.Button(top,text='Clear')
b1.grid(row=0,column=0,padx=10,pady=10)
b2.grid(row=1,column=0,padx=10,pady=10)
b3.grid(row=0,column=1,padx=10,pady=10)
b4.grid(row=1,column=1,padx=10,pady=10)
b1.configure(command=star)
b2.configure(command=pent)
b3.configure(command=quit)
b4.configure(command=clear)
top.mainloop()
