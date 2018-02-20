# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:37:09 2018

@author: SONY
"""

from random import randrange
def roll():
    rolled = randrange(1,7)
    if rolled == 1:
        return "1"
    if rolled == 2:
        return "2"
    if rolled == 3:
        return "3"
    if rolled == 4:
        return "4"
    if rolled == 5:
        return "5"
    if rolled == 6:
        return "6"


def rollManyCountTwo(n):
    twoCount = 0
    for i in range (n):
        if roll() == "2":
            twoCount += 1
    print ("In", n,"rolls of a pair of dice, there were",twoCount,"twos.")