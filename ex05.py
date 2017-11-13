name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
c = 1 * 2.54 / 1
height_c = c * height
k = 1 * 0.45359237
weight_k = k * weight

print "Let's talk about %s." % name
print "He's %i inches tall." % height
print "That are %d centimeters." % height_c
print "He's %d pounds heavy." % weight
print "That are %d kilograms." % weight_k
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
