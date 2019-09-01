# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:48:38 2019

@author: Veloc1ty
"""

# Various fun stuff relating to primes

def checkPrime(num):
    """ Optimised check prime function
    Assuming we don't have a list of primes
    It is only necessary to check up to sqrt(num)
    Since multiples come in pairs
    """
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def isTruncatable(n):
    # Helps determine whether a number
    # can be truncated into primes
    while n != 0:
        n = n // 10
        if not checkPrime(n):
            return False

num = 7
counter = 0       
total = 0

if __name__ == '__main__':
    """We want to find the first ten truncatable primes
    where if we invert the number str(num)[::-1], the 
    number is still truncatable
    
    We mark each number as non-truncatable and continue through
    the loop when we find one. This ensures we're not doing too much
    work.
    """
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

    
            
        
