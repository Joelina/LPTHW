from sys import argv #imports argv

script, filename = argv #names which arguments it needs to run

txt = open(filename) #opens the txt file given as filename

print "Here's your file %r:" % filename #prints the string and the filename
print txt.read() #prints what's inside the txt file --> read with no parameters

print "Type the filename again:" #print string
file_again = raw_input("> ") #assigns var file_again to raw_input

txt_again = open(file_again) #assigns var txt_again to open file_again

print txt_again.read() #print what's inside the txt file with read
