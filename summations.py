# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 08:59:10 2019

@author: Veloc1ty
"""

#Project Euler Problem 76


index = 1
while True:
    target = index
    ns = range(1, target)
    ways = [1] + [0]*target

    for n in ns:
        for i in range(n, target+1):
            ways[i] += ways[i-n]
        
    if ways[target]+1 % 1000000 == 0:
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
   print(index)

# list of generalized pentagonal numbers for generating function
k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p, sgn, n, m  = [1], [1, 1, -1, -1], 6, 1e6

px, i = 0,0
while k[i] <= n:
    print(int(n-k[i]))
    px += p[int(n - k[i])] * sgn[int(i%4)]
    i += 1

while p[n]>0:
    n += 1
    px, i = 0, 0
    while k[int(i)] <= n:
        px += p[int(n - k[int(i)])] * sgn[int(int(i)%4)]
        i += 1
    p.append(px % m)

print("Project Euler 78 Solution =", n)

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



numbers = int(input())
decimals = int(input())
c,s = euler80(numbers,decimals)
print(c)
    
    