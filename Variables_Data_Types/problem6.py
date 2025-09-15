# Author: Amad Bin Jaiyad
"""
Problem6:
         Swap the values of two variables without using a third variable.
"""
x = 10 
y = 15

print("Before swapping:", x,y)

x,y = y,x # Pythonic way to swap 

print("After swapping:", x,y)