#!/usr/bin/python
# This is the script for HW1 question number 6

list1=['I','Mom','Dad','Sister']
list2=['Mon','Tue','Wed','Thu','Fri']

tuple1=(8,2,4,6,7)
tuple2=('movies','ballet','gym','spa','Taekwondo')

print 'This is our family schedule for this week'
print "%s goes to the %s on %s at %sPM" %(list1[2],tuple2[0],list2[0],tuple1[3])
print "%s goes to %s at %sPM on %s" %(list1[1],tuple2[3],tuple1[2],list2[0])
print "%s goes to %s at %sAM on %s" %(list1[2],tuple2[2],tuple1[0],list2[1])
print "%s go to %s at %sAM on %s" %(list1[0],tuple2[4],tuple1[3],list2[2])
print "My %s goes to %s at %sPM on %s" %(list1[3],tuple2[1],tuple1[3],list2[3])
print "We all go to %s at %sPM on %s" %(tuple2[0],tuple1[4],list2[4])
