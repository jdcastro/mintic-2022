#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
en-EN:
you can use expressions in Python, like this:
es-ES:
Puedes usar expresiones en Python, de esta forma:
example:
"""

print ("give me two numbers, and I'll divide them.")
number_a = int(input("first number: "))
number_b = int(input("second number: "))

# expressions are evaluated in the order they are written
division = number_a / number_b # this is a division expression
quotient = number_a // number_b # this is a quotient expression
remainder = number_a % number_b # this is a remainder expression

# way to print the result of an expression
print ("{0} divided by {1} is {2} with a remainder of {3} and quotiend {4}".format(number_a, number_b, division, remainder, quotient))
print ("{} divided by {} is {} with a remainder of {} and quotiend {}".format(number_a, number_b, division, remainder, quotient))
print ("%s divided by %s is %s with a remainder of %s and quotiend %s" % (number_a, number_b, division, remainder, quotient))
print (number_a, "divided by", number_b, "is", division, "with a remainder of", remainder, "and quotiend", quotient)
print (str(number_a) + " divided by " + str(number_b) + " is " + str(division) + " with a remainder of " + str(remainder) + " and quotiend " + str(quotient))
