#!/usr/bin/python
# This script is used to show the usage of "if" statements
# The if statement is a conditional that, when it is satisfied, activates some part of code

men=int(raw_input("How many men live in your ideal world? "))
women=raw_input("How many women live in your ideal world? ")
babies=raw_input("How many babies live in your ideal world? ")

if men>women:
	print "Not many women! The world is doomed!"
elif men<women:
	print "Too many women! The world is saved!"
else:
	print "We live in a world of equality... the world is doomed"

if men<babies:
	print "Too many babies, The world is drooled on!"
elif men>babies:
	print "Not many babies, how will the human race last?!?"
else:
	print "Babies and men are equal... you're crazy!"

babies=men
if men>=babies:
	print "men are greater than or equal to babies."
elif men<=babies:
	print "men are less than or equal to babies."
if men==babies:
	print "men are babies."
