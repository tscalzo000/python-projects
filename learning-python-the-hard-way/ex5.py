name = 'Zed A. Shaw'
age = 35
height = 74.0
weight = 180.0
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "He's %d kilos heavy." % (weight * 0.45359237)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
