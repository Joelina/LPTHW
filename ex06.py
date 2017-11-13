x = "There are %d types of preople" % 10 #x says there are 10 types of people
binary = "binary" #binary is the string "binary"
do_not = "don't" #do_not is the string "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #y puts the two previously defined strings in a sentence

print x #prints x
print y #prints y

print "I said %r." % x #repeats the sentence from x
print "I also said: '%s'." % y #repeats the sentence from y

hilarious = False #defines the var hilarious as False
joke_evaluation = "Isn't that joke so funny?! %r" #evaluates the joke and gives hilarious as answer

print joke_evaluation % hilarious #prints the sentence and answer from the joke evaluation

w = "This is the left side of..." #defines this string to the var w
e = "a string with a right side." #defines this string to the var e

print w + e #prints the two strings of w and e
