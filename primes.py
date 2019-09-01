# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:48:38 2019

@author: billj
"""

def checkPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def isTruncatable(n):
    while n != 0:
        n = n // 10
        if not checkPrime(n):
            return False

num = 7
counter = 0       
total = 0

while counter < 11:
    num += 2
    isPrime = checkPrime(num)
    if isPrime:
        flag1 = isTruncatable(num)
        if flag1 == False:
            continue
        flag2 = isTruncatable(int(str(num)[::-1]))
        if flag2 == False:
            continue
        else:
            counter += 1
            total += num

    
            
        
