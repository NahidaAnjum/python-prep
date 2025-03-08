'''Modules allow us to split our code base in to smaller parts
A module is a file containing python definitions and statements which can be imported and used when Necessary
You can write your own module, another developer's module or python built-in modules
'''
import math

print(math.pi)

def sin(x):
    if 2*x == pi:
        return "Its a pi value"
    else:
        return None
    
pi = 3.14

## To understsnd scope here, if we have same function names as in module its not conflict as they are modules 
# namespace scoped and they should be referenced with math.entityname but if we import like this
# from math import pi ==> then only pi entity is imported and it can cause the name conflict if we define the function or variable 
# with the same name, it will override the value of the module entity with the user defined value.

print (sin(pi/2))
print (math.sin(pi/2))    

'''The dir function gives the alphabetically sorted list of the entitiues present in the module, If
you want to know how to use each of these you have chcek the pythobn documentation
'''       
print (dir(math))

# Using Random module
# Add imports here
import random

# Complete the function
def cards_sample(suits, ranks):
   deck =[str(x)+'-'+y for x in ranks for y in suits]
   return random.sample(deck,4)

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))

#using platform module
# from platform import machine, ...
import platform

def platform_info():
    user_os = platform.system()
    user_arch = platform.machine()
    user_python = platform.python_implementation()
    return user_os, user_arch, user_python


print(platform_info())