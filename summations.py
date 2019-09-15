# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 08:59:10 2019

@author: Veloc1ty
"""

""" 
    This is an awesome dynamic programming technique
    Essentially we want an algorithm that figures out
    how many ways we can express a number as a summation
    of positive integers 
"""


index = 1
while True:
    target = index
    ns = range(1, target)
    ways = [1] + [0]*target # Ways forms our basic steps, e.g we could have 1->100

    for n in ns:
        for i in range(n, target+1): # It feels like divide and conquer, partition into smaller building blocks
            ways[i] += ways[i-n] # We find next series of summations using previous ones
        
    if ways[target]+1 % 1000000 == 0: # Here we just want to find a number that has 1,000,000 partitions
        print(index)
        break
    

target = 6
ns = range(1, target)
ways = [1] + [0]*target

for n in ns:
    for i in range(n, target+1):
        ways[i] += ways[i-n]
        
print(ways[target]+1)
        
if ways[target]+1 % 1000000 == 0:
   print(index) # Modified hackerrank version

# https://en.wikipedia.org/wiki/Pentagonal_number_theorem
# This is a general function for determining how many ways you 
# can partition some set of objects.
k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p, sgn, n, m  = [1], [1, 1, -1, -1], 6, 1e6

px, i = 0,0
while k[i] <= n:
    print(int(n-k[i]))
    px += p[int(n - k[i])] * sgn[int(i%4)]
    i += 1

# We want to figure out how many ways we can
# Partition n objects, which we do using the 
# Pentagonal number theorem below
while p[n]>0:
    n += 1
    px, i = 0, 0
    while k[int(i)] <= n:
        px += p[int(n - k[int(i)])] * sgn[int(int(i)%4)]
        i += 1
    p.append(px % m)

print("Project Euler 78 Solution =", n)
# That's the solution for 78, Hackerrank requires some modification

# Finally, here we want to sum together all the integers up to some limit
# For irrational square roots
import decimal

def euler80(numbers,limit) :
  sq = int(numbers ** 0.5)
  s = set(range(numbers+1)) - set(x*x for x in range(sq))
  decimal.getcontext().prec = limit + 5
  ds = 0
  for i in s :
  #for i in [2] :
    d = decimal.Decimal(i)
    sqrt_d = d.sqrt()
    s = str(sqrt_d).replace(".", "")[ : limit]
    ds += sum(int(c) for c in s)
  return ds

# It's money time
numbers = int(input())
decimals = int(input())
c,s = euler80(numbers,decimals)
print(c)
    
    
