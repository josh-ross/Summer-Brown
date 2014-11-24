#!/usr/bin/python
# This is the script for a car rental company (HW2)

import os
os.system('clear')

print "Welcome to Hertz.com. Press any button to enter the website."
web=raw_input()
name=str(raw_input("What is your name? "))
print "Hello %s and welcome to Hertz!" %(name)
import time
time.sleep(1)
print "Before you can rent a car from us, we will just need some basic information from you."
time.sleep(2)
print "Where are you from?"
where=str(raw_input())
print "How old are you?"
age=int(raw_input())
if age>=25:
	print "Hit RETURN to begin the rental process."
	go_on=raw_input()
else:
	print "I am sorry %s, but you are too young to rent a car :(" %(name)
	import sys
	sys.exit("Goodbye!")
		
os.system('clear')
print "Ok %s from %s, let's get started!"%(name,where)
time.sleep (1)
print "We have four types of cars to choose from: compact, fullsize, van and SUV. Which type would you like to rent?"
size=str(raw_input())
if size=="compact":
	print "Would you like to rent a Civic or Corrolla?"
if size=="fullsize":
	print "Would you like to rent an Accord or Camry?"
if size=="van":
	print "Would you like to rent an Odyssey or Sienna?"
if size=="SUV":
	print "Would you like to rent a RAV4 or CRV?"
car=str(raw_input())

print "Okay %s, so you have decided to rent one of our %s's. Now let's move on to the add-on's available for purchase. For the following questions please respond with only 'yes' or 'no'." %(name,car)
time.sleep(3)
print "Would you like to purchase collision damage coverage?"
collision=raw_input()
#if collision=="no"
	#print "Are you sure you do not want to purchase collision damage coverage? It is only an extra $30 per day. (Press z to purchase, anything else to continue)"
#collision2=raw_input()
#if collision2=="z"

print "Would you like to purchase liability coverage?"
liability=raw_input()

print "Would you like to purchase personal protection coverage?"
protect=raw_input()

print "Would you like to purchase roadside assistance?"
road=raw_input()

#def add (car,collision,liability,protect,road):

if car=="Civic":
	carz=30
if car=="Corrolla":
	carz=25
if car=="Accord":
	carz=40
if car=="Camry":
	carz=35
if car=="Odyssey":
	carz=50
if car=="Sienna":
	carz=45
if car=="RAV4":
	carz=55
if car=="CRV":
	carz=60

if collision=="yes":
	costc=30
else:
	costc=0

if liability=="yes":
	costl=20
else:
	costl=0
if protect=="yes":
	costp=15
else:
	costp=0
if road=="yes":
	costr=10
else:
	costr=0
total=carz+costl+costc+costp+costr
print "%s, you have selected to rent a %s" %(name,car)
print "Is this information correct? Press RETURN if yes, press CTRL-C if no."
correct=raw_input()
print "One moment please..."

time.sleep(2)

print "The cost of your total purchase will be:$%s" %(total)
time.sleep(2)
print "Congratulations, and thank you for renting from Hertz. Have a safe ride!"
