# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:29:05 2019

@author: Veloc1ty
"""

# A range of playtools for the PE arena
from itertools import permutations
import math

number = '0123456789'
index = int(input())
number = number[0:index+1]

numbers = [''.join(p) for p in permutations(number)]

def isDivisible(number, primes):
    # Figure out if a section of a number is divisible by primes
    # Useful for chopping and changing and defining properties relating to PE
    for i in range(1, len(number)-2):
        if int(number[i:i+3]) % primes[i]:
            return False
    return True

total = 0
primes = [1, 2, 3, 5, 7, 11, 13, 17]

# Are the subsets of the numbers divisible by primes?
if __name__ == '__main__':
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
    # Calculate a vector of primes
    # Dividing by primes instead of all numbers optimises the code
    primes = [2]
    for i in range(3, number, 2):
        isPrime = True
        for element in primes:
            if (element**2 > i):
                break
            if i % element == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
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
    
# Chapernowne section

def sumofDigits(n):
    # Simply sums up the digits up to a point
    # Formula sourced from wikipedia entry on Chapernowne's constant
    numerator = 9*(10**n*(n+1)) - 10**(n+1) + 1
    return int(numerator / 9)

def findID(number, i):
    # Process for finding particular Chapernowne entry section
    # This enables us to determine the behaviour of numbers around i
    return number - i

def findNumber(ID, n):
    # Given the location and indice, we can find the exact number in
    # the Chapernowne expansion
    return (10**n-1) - math.floor(ID/n)

def findRes(ID, n):
    # Find indice of digit within determined number
    return ID % n + 1

def findChampernowne():
    # Work house function to find a particular digit in Chapernowne expansion
    # input() refers to hackerrank implementation (We find the sum of digits up to this point)
    indices = input().split(' ')
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    
    total = 1

    for index in indices:
        num_digits = len(str(index))-1
        
        # Find the sum of digits up to a point
        # This helps us find our desired digit
        number = sumofDigits(num_digits)
        
        # Adjustment, number is only < index for 1 digit numbers
        # sumOfDigits will return 0 for number in this case
        # Due to implementation nature
        # So we must manually adjust
        if number < index:
            num_digits += 1
            number = sumofDigits(num_digits)
        
        # Now we zero in on the exact digit we're looking for
        ID = findID(number, index)
        num = findNumber(ID, num_digits)
        res = findRes(ID, num_digits)
        result = int((str(num))[-res])
        total *= result
    
    print(total)

# How many times do we want to test it?
tests = int(input())

# Let's go!
if __name__ == '__main__':
    for i in range(tests):
        findChampernowne()
    
