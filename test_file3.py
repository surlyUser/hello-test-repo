# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:41:42 2025

@author: gerald
"""

#-------------- #1 equations.py -------------------------
import cmath

def quadratic(a, b, c):
    # a = float(a)
    # b = float(b)
    # c = float(c)
    if a < 0:
        # print('The denominator must not be zero, try again!')
        return 'The denominator must not be zero, try again!'
    
    q = cmath.sqrt((b**2 - 4 * a * c))
    x1 = (-b + q) / (2 * a)
    x2 = (-b - q) / (2 * a)
    x1 = complex(round(x1.real, 2), round(x1.imag, 2))
    x2 = complex(round(x2.real, 2), round(x2.imag, 2))
    # print(f'x1: {x1:.2f} x2: {x2:.2f}')
    # return f'x1: {x1:.2f} x2: {x2:.2f}'
    solutions = [x1, x2]

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

solution = quadratic(a, b, c)
print(solution)

#-------------
# python -m pytest equations_test.py
