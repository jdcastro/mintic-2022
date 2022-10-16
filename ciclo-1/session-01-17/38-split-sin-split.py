#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# split a sentence withou using split()

sentense = "I am a simple sentence"
tmp = ''
for i in sentense: # for each character in the sentense
    if i == ' ': # if the character is a space (' ') print the tmp variable
        print(tmp) # print the tmp variable 
        tmp = '' # reset the tmp variable
    else:
        tmp += i # add the character to the tmp variable
        
print(tmp) # print every word in the sentense in a new line


# example 2:
# is exactly but slice and make a new list
sentense = "I,am,a,simple,sentence"
list_values = []
tmp = ''

for j in sentense:
    if j == ',':  # if the character is a comma (',') print the tmp variable
        list_values.append(tmp) # add the tmp variable to the list
        tmp = '' # every time a comma is found the tmp variable is reset to empty
    else:
        tmp += j 
if tmp:           # if tmp is not empty
    list_values.append(tmp)
print(list_values)

valor1 = list_values[0]
valor2 = list_values[1]
