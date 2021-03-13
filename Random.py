# Pattol Albadry 
# Sep 17.2020
# Lab 2: Demo code

from random import randint

roll = input("press Y to roll the dice, press N to quit")
while roll.lower () == "y":
    print(randint(1,10))
    roll = input("press Y to roll again, press N to quit")

print("okay, we'll put the dice away.")
