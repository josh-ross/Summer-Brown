# A new list can be generated using a for loop as well.
# In order to generate a new list, initially you start with an empty list [] & then use for loop to append a value into it
# list.append(value) will append the value into the list

empty=[]
fruit=["apples","oranges","pears","banana","grapes"]
for a in fruit:
	print "%s are awesome" %a
vege=["onions","tomatoes","kales","potatoes","beets"]
for b in vege:
	print "\t%s just suck" %b 
food=["chicken","beef","fish","pork","lamb"]
for c in food:
	print "%s tastes soooo good" %c
cal=[100,"empty",200,300,400,500]
for d in cal:
	print "\tI bet it has %s calories" %d

for e in range(0,6):
	print "Adding %s to numbers list" %e
	empty.append(e)

new=[0,1,2,3,4,5]
for f in new:
	print "\tThe new number was %s" %f

print "Here is the full list", empty
