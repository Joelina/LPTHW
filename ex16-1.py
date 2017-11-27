from sys import argv #imports argv

script, filename = argv #names which arguments it needs to run

txt = open(filename) #opens the txt file given as filename

print "Here's your file %r:" % filename #prints the string and the filename
print txt.read()
