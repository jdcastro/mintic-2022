#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
en-EN:
example of operators precedence and associativity in Python
es-ES:
ejemplo de precedencia y asociatividad de operadores en Python
example:
"""
# first python excecute the operation in the order of:
# 0. parentheses
# 1. multiplication, division and modulus, exponentiation
# 3. addition, subtraction
# with the associativity of left-to-right precedence

simple_ecuation = 1 + 2 * 3 / 4 % 5  + (6 - 7) ** 8
print (simple_ecuation)