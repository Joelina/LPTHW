from sys import argv

script, name, colour = argv

print "The script is called:", script
print "Your name is:", name
print "Your favourite colour is:", colour

print "How old are you?",
age = raw_input()
print "So, you're %r years old." % age
