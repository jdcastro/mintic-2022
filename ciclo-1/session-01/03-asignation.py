#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
en-EN:
we can assign a value to a variable using the equal sign
es-ES:
podemos asignar un valor a una variable usando el signo igual
examples:
"""

# assign a value to a variable
variable = "Hello"

# reassign a value to a variable
variable = 1 

# assign a value to a variable from user input
variable_from_keyboard = input("Input a number: ")

# assign multiple values to multiple variables
a, b, c, d, e, f, g, h, i, j = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# assign multiple values to a single variable, a tuple. 
variable_multiple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 

# assign multiple values to multiple variables to a tuple
variable_mult = k, l, m = 11, 12, 13 

# assign multiple values from a tuple to multiple variables
n, o, p, q, r, s, t, u, v, w = variable_multiple 

# assign a tuple to a variable with a tuple inside.
varable_t = (1.1, 2.2, (3.3, 4.4, 5.5)) 

# assing multiple values to multiple variables from keyboard
ac, bc, cc, dc, ec, fc, gc, hc, ic, jc = input("Input 10 words separate by space: ").split()

ab, bb, cb, db, eb, fb, gb, hb, ib, jb = map(int, input("Input 10 numbers separate by space: ").split())

# print all values
print(variable, variable_from_keyboard, variable_multiple, variable_mult, varable_t,
      "\n", a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w)
print(ab, bb, cb, db, eb, fb, gb, hb, ib, jb)
print(ac, bc, cc, dc, ec, fc, gc, hc, ic, jc)