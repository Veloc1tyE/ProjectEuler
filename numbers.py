# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:38:07 2019

@author: Veloc1ty
"""

import math
def Triangle(n):
    return n*(n+2)/2

def Pentagon(n):
    return n*(3*n-1)/2

def Hexagon(n):
    return n*(2*n-1)

def Solver(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return None
    if -b + math.sqrt(D) > 0:
        return (-b + math.sqrt(D))/2
    elif -b - math.sqrt(D) > 0:
        return (-b - math.sqrt(D))/2
    else:
        return None

matcher = 0
n = 286
while True:
    const = Triangle(n)
    if int(Pentagon(Solver(1.5, -0.5, -const))) == int(const):
        if int(Hexagon(Solver(2, -1, -const))) == int(const):
            matcher = const
            print('yay!')
            break
    n += 1
    
print(matcher)
        
    
    
