formatter = "%r %r %r %r" #var formatter is defined to a string that has to reprint its given input

print formatter % (1, 2, 3, 4) #prints this in the string of formatter
print formatter % ("one", "two", "three", "four") #prints this in the string of formatter
print formatter % (True, False, False, True) #prints this in the string of formatter
print formatter % (formatter, formatter, formatter, formatter) #prints the formatter in the formatter
print formatter % ( #prints the following strings in the string of the formatter
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
