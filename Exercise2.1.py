
# Exercise 2.1

''' A ball is dropped from a tower of height h with initial velocity zero. 
     Write a program that asks the user to enter the height in meters of the tower and 
          then calculates and prints the time the ball takes until it hits the ground, ignoring air resistance.
     Use your program to calculate the time for a ball dropped from a 100 m high tower.'''

import math
import sys

print(sys.argv)

if __name__ == '__main__':
    g = 9.81
    #height is the first argument in sys.argv
    h = float(sys.argv[1])
    #calculate time it takes to fall
    t = math.sqrt(2*h/g)

    print(f"The time it takes to fall is: {t:.2f} seconds")




