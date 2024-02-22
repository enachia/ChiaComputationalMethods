# Exercise 2.4

'''A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. 
     Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, 
          then print out the time in years that the spaceship takes to reach its destination 
               (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship. 
     Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.'''

import numpy as np
import sys
import math

# Ask the user for the value of x and v
x = float(input("Enter the distance to the destination in light years: "))
v = float(input("Enter the speed of the spaceship as a fraction of the speed of light: "))

# Calculate the time it takes for the spaceship to reach its destination
t = x / v

# Print out the time
print(f"The spaceship takes {t} years to reach its destination.")














import argparse
#print time in yrs it takes for spaceship to reach destination

def calc_t(distance, speed):
    #time observed from earth
    t_earth = distance / speed

    #time observed from spaceship
    gamma = 1 / np.sqrt(1 - speed**2)
    t_ship = t_earth / gamma

    return t_ship, t_earth
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('distance', type=float, help='the distance to the destination in light years')
    parser.add_argument('speed', type=float, help='the speed of the spaceship as a fraction of the speed of light')

    args = parser.parse_args()

    t_ship, t_earth = calc_t(args.distance, args.speed)

    print(f"The time observed from the spaceship is {t_ship:.2f} years")
    print(f"The time observed from earth is {t_earth:.2f} years")

if __name__ == '__main__':
    main()
