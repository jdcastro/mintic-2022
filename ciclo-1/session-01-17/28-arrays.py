#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a unidimensional array is a list of elements, in python we can use multiple types of elements in a list.
"""
ages = [45, 63, 18, 25, 53]
print(ages[0])
ages.append(23)
ages.append(20)
print(ages)
print(len(ages))
ages[0] = 50
print(ages)