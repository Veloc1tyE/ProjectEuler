# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:39:03 2019

@author: billj
"""

# time module
import time

# time at the start of program execution
start = time.time()

# open the file
f = open('cipher.txt')

# Strip and split the contents of the file to a list
cipher = f.read().strip().split(',')

# convert the string to integer
cipher = [int(x) for x in cipher]

# letters in ascii from a-z
eng_letters = range(97, 123)

# first letter of the encryption key
first_letter = set([])

maxCount = 0
maxKey = []
for i in eng_letters:
    for j in eng_letters:
        for k in eng_letters:
            count = 0
            key = [i, j, k]
            valid = True
            for n in range(len(cipher)):
                if cipher[n] ^ key[n % 3] == 32 or cipher[n] ^ key[n % 3] == 101:
                    count += 1
            if count > maxCount:
                maxCount = count
                maxKey = key

count = 0
newString = ""
for t in range(len(cipher)):
    dex = cipher[t] ^ maxKey[t%3]
    newString += chr(dex)
    count += cipher[t] ^ maxKey[t%3]
