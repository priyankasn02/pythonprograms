# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:26:19 2018

@author: SONY
"""

import random
import time
import sys

diceNumber = random.randint(1,6)



print("lets play dice of destiny")

play1 = input("Player 1 name?")
play2 = input("Player 2 name?")
prize = input("What does the loser have to do?")

play1Num = input(play1 + " choose a number 1-6.")
play2Num = input(play2 + " choose a number 1-6.")

play1Num = int(play1Num)
play2Num = int(play2Num)

if play1Num == diceNumber:
    print("The Dice rolled...")
    print(diceNumber)
    print(play1.upper() + " WINS!")
    print(play2 + " must: " + prize)
    sys.exit()

if play2Num == diceNumber:
    print("The Dice rolled...")
    print(diceNumber)
    print(play2.upper() + " WINS!")
    print(play1 + " must: " + prize)
    sys.exit()

while diceNumber != play1Num and play2Num:
    print("The Dice rolled...")
    print(diceNumber)
    print("both wrong, rolling again...")
    diceNumber = random.randint(1,6)
    time.sleep(1)

if play1Num == diceNumber:
    print("The Dice rolled...")
    print(diceNumber)
    print(play1.upper() + " WINS!")
    print(play2 + " must: " + prize)
    break

if play2Num == diceNumber:
    print("The Dice rolled...")
    print(diceNumber)
    print(play2.upper() + " WINS!")
    print(play1 + " must: " + prize)
    break