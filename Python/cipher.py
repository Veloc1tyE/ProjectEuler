# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:39:03 2019

@author: Veloc1ty
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

# Here we use frequency analysis to decode the text
maxCount = 0
maxKey = []
# We iterate through the letters of the alphabet and keep track of how common ' ' or 'e' is
for i in eng_letters:
    for j in eng_letters:
        for k in eng_letters:
            count = 0
            key = [i, j, k]
            valid = True
            for n in range(len(cipher)):
                # Count ' ' (32) and 'e' (101). The higher the count, the more likely it will be a valid key
                if cipher[n] ^ key[n % 3] == 32 or cipher[n] ^ key[n % 3] == 101:
                    count += 1
            if count > maxCount:
                maxCount = count
                maxKey = key

# Print the text and return its alphanumeric total count
count = 0
newString = ""
for t in range(len(cipher)):
    dex = cipher[t] ^ maxKey[t%3]
    newString += chr(dex)
    count += cipher[t] ^ maxKey[t%3]
