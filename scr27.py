#!/usr/bin/python
# Nested if statements are if statements which contain if statements which enables the user to create branch decisions
# This script will help us understand nested if statements

name=str(raw_input("Hello, what is your name? "))
pet=str(raw_input("What type of pet do you have? "))
color=str(raw_input("What is the color of your pet? "))
pname=raw_input("What is your pet's name? ")

if pet=="dog":
	if color=="brown":
		print "%s, your %s %s named %s belongs to the Canindae family" %(name,color,pet,pname)
	elif color=="white":
		print "%s, your %s %s named %s belongs to the Canindae family" %(name,color,pet,pname)
	elif color=="black":
		print "%s, your %s %s named %s belongs to the Canindae family" %(name,color,pet,pname)
	else:
		print "You have a dog but I do not understand its color"
elif pet=="cat":
	if color=="brown":
		print "%s, your %s %s named %s belongs to the felidae family" %(name,color,pet,pname)
	elif color=="white":
		print "%s, your %s %s named %s belongs to the felidae family" %(name,color,pet,pname)
	elif color=="black":
		print "%s, your %s %s named %s belongs to the felidae family" %(name,color,pet,pname)
	else:
		print "You have a cat but I do not understand its color"
elif pet=="fish":
	if color=="brown":
		print "%s, your %s %s named %s belongs to the cyprindae family" %(name,color,pet,pname)
	elif color=="white":
		print "%s, your %s %s named %s belongs to the cyprindae family" %(name,color,pet,pname)
	elif color=="black":
		print "%s, your %s %s named %s belongs to the cyprindae family" %(name,color,pet,pname)
	else:
		print "You have a fish but I do not understand its color"
elif pet=="bird":
	if color=="brown":
		print "%s, your %s %s named %s belongs to the avian family" %(name,color,pet,pname)
	elif color=="white":
		print "%s, your %s %s named %s belongs to the avian family" %(name,color,pet,pname)
	elif color=="black":
		print "%s, your %s %s named %s belongs to the avian family" %(name,color,pet,pname)
	else:
		print "You have a bird but I do not understand its color"
else:
	print "Why would you ever want to have a %s as a pet?!? EW" %(pet)
	
	
# For Loop- Execute a sequence of statements multiple times wherein the number is defined by a set
