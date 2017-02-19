x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# string inside of a string times 2
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# string inside of a string
print "I said: %r." % x
# 2 strings inside of a string inside of a string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# strings are added to the end of each other
print w + e
