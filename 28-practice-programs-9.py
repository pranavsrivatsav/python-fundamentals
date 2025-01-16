#Modules practice

"""
Import the math module.
• Use the following functions from the math module: 
    o sqrt() to calculate the square root of a number.
    o pow() to calculate the power of a number.
    o sin(), cos(), tan() to calculate trigonometric functions.
    o pi to access the value of pi.
"""

import math


print(math.sqrt(121))
print(math.pow(2,4))

angle_radians = math.pi /2 #90 degrees
print(math.sin(angle_radians))
print(math.cos(angle_radians))
print(math.tan(angle_radians))


"""
Import the random module.
• Use the following functions from the random module: 
    o randint() to generate a random integer within a specified range.
    o random() to generate a random floating-point number between 0 and 1.
    o choice() to select a random element from a list.
    o shuffle() to shuffle the elements of a list in place
"""
import random

print(random.randint(1,100))
print(random.random())

sampleList = [123,"sfdsfg",True]
print(random.choice(sampleList))

random.shuffle(sampleList)
print(sampleList)


"""
Import the datetime module.
• Use the following functions from the datetime module: 
    o datetime.now() to get the current date and time.
    o date.today() to get the current date.
    o timedelta() to perform date and time calculations
"""

import datetime
print(datetime.date.today())

