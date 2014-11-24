# This is the script for question 11
translation=[]
vowel=['a','e','i','o','u','A','E','I','O','U']
print "Type a sentence to translate"
word=raw_input()
for a in word:
	if a in vowel:
		translation.append(a)
		translation.append(a)
		translation.append('j')
	else:
		translation.append(a)
print ''.join(translation)
