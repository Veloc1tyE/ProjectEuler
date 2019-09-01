# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:32:43 2019

@author: billj
"""

import time

def findCarbon(num_years, num_trees, tree):
    if tree == "eucalypt":
        print("You've offset " + str(int(15.7*num_years*num_trees)) + " kg of CO2")
        return True
    else:
        print("Invalid Datatype")
        return False

print("Hello There! Here we display your user statistics")
time.sleep(1)
print("Given the number of trees you've planted, ")
time.sleep(1)
print("As well as the amount of time they've been growing\n")


while True:
    print("Please input the number of trees you've planted")
    num_trees = int(input())
    print("Please input the number of years they've been growing")
    num_years = int(input())
    print("Please specify the type of tree")
    tree = str(input())

    tree = tree.lower()
    if findCarbon(num_years, num_trees, tree):
        break

        


    