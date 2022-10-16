#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remove a element from the array
"""
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5, 5]
print(vector)
vector.remove(5)
print(vector, "remove number 5\n")

vector.pop(3)
print(vector, "pop position 3\n")

# remove all 5 from the array using the method lambda
vector = list(filter (lambda x: x != 5, vector))
print(vector, "remove all 5\n")


#clear the array
vector.clear()
