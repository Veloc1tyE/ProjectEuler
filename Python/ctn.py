# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:14:47 2019

@author: Veloc1ty
"""

import math

words = open("words.txt", 'r')
words = words.read().lower().replace('"', '').split(',')

def mapping(word):
    total = 0
    for letter in word:
        total += ord(letter) - 96
    return total

def Triangular(val):
    index = round(math.sqrt(2*val + 0.25) - 0.5)
    if 0.5*index*(index+1) == val:
        return index
    else:
        return -1

count = 0
for word in words:
    val = mapping(word)
    if isTriangular(val):
        count += 1

print(count)

        
        

    
