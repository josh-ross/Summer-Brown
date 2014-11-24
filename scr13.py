#!/usr/bin/python
# This script shows how to provide arguments with the scrip
# Sys/import function is a handy tool
# Enables you to add a feature from the preexisting python modules

from sys import argv

script,first,second,third,fourth,fifth,sixth=argv

print "The script is called:", script
print "Your first variable will be the name, which is:", first
print "Your second variable will be hair color, which is:", second
print "Your third variable will be eye color, which is:", third
print "Your fourth variable will be your age, which is:", fourth
print "Your fifth varuable will be your height, which is:", fifth
print "Your sixth variable will be your weight, which is:", sixth

import os 	# This clears everything up previously
os.system('clear')
import time 	# This causes a delay
time.sleep(1)
print "Hi %r, nice to meet you" %(first)
print "Looks like you have %r hair & %r eyes" %(second,third)
print "So, you're %r years old, %r inches tall and weigh %r pounds" %(fourth,fifth,sixth)
