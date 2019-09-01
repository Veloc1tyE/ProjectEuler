# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:29:05 2019

@author: billj
"""

from itertools import permutations
import math

number = '0123456789'
index = int(input())
number = number[0:index+1]

numbers = [''.join(p) for p in permutations(number)]

def isDivisible(number, primes):
    for i in range(1, len(number)-2):
        if int(number[i:i+3]) % primes[i]:
            return False
    return True

total = 0
primes = [1, 2, 3, 5, 7, 11, 13, 17]

for number in numbers:
    if isDivisible(number, primes):
        total += int(number)

print(total)

#16695334890
def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def calculatePrimes(number):
    primes = {2,}
    for i in range(3, number, 2):
        isPrime = True
        for element in primes:
            if (element**2 > i):
                break
            if i % element == 0:
                isPrime = False
                break
        if isPrime:
            primes.add(i)
    return primes

number = '987654321'

for i in range(0, 9):
    base = number[i:]
    numbers = [''.join(p) for p in permutations(base)]
    largest = 0
    for element in numbers:
        if isPrime(int(element)):
            largest = int(element)
            break
    if largest != 0:
        print(largest)
        break
    

tests = int(input())

for i in range(tests):
    # Precalculations
    number = '987654321'
    maxNum = int(input())
    # Same num digits as maxNum
    index = 9 - len(str(maxNum))
    number = number[index:]

    for i in range(0, len(number)):
        # Main loop
        base = number[i:]
        numbers = [''.join(p) for p in permutations(base)]
        largest = 0
        for element in numbers:
            if isPrime(int(element)):
                if int(element) <= maxNum:
                    largest = int(element)
                    break
        if largest != 0:
            if largest == 1:
                print(-1)
            else:
                print(largest)
            break

indices = input().split(' ')
for i in range(len(indices)):
    indices[i] = int(indices[i])

def sumofDigits(n):
    numerator = 9*(10**n*(n+1)) - 10**(n+1) + 1
    return int(numerator / 9)

def findID(number, i):
    return number - i

def findNumber(ID, n):
    return (10**n-1) - math.floor(ID/n)

def findRes(ID, n):
    return ID % n + 1

def findChampernowne():
    indices = input().split(' ')
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    
    total = 1

    for index in indices:
        num_digits = len(str(index))-1
            
        number = sumofDigits(num_digits)

        if number < index:
            num_digits += 1
            number = sumofDigits(num_digits)

        ID = findID(number, index)
        num = findNumber(ID, num_digits)
        res = findRes(ID, num_digits)
        result = int((str(num))[-res])
        total *= result
    
    print(total)

tests = int(input())

for i in range(tests):
    findChampernowne()
    