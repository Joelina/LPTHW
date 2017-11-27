the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'bananas', 'kiwis']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

#can also go through mixed lists, but have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

#we can also build lists, first empty
elements = []

#then use range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    #append is a function lists understand
    elements.append(i)

for i in elements:
    print "Element was: %d" % i
