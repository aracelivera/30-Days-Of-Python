#   Day 12 - 30DaysOfPython Challenge


#   Modules
# A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

#   Creating a Module
# To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let us write some code in this file.

#   Importing a Module
import mymodule
print(mymodule.generate_full_name('Araceli', 'Vera')) 

#   Import Functions from a Module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Araceli','Vera'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['first_name'])

#   Import Functions from a Module and Renaming
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Araceli','V'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['first_name'])

#   Import Built-in Modules
# Some of the common built-in modules: math, datetime, os, sys, random, statistics, collections, json,re

#   OS Module
# Using python os module it is possible to automatically perform many operating system task
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

#   Sys Module
import sys
# Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
# wrote in command line:  python script.py Araceli 30DaysOfPython
print(sys.argv[0], sys.argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# Some useful sys commands:
# To know the largest integer variable it takes
sys.maxsize # 9223372036854775807
# To know environment path
sys.path
# To know the version of python you are using
sys.version # 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]'
# to exit sys
# sys.exit()

#   Statistics Module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~21.1
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~6.1

#   Math Module
# To check what functions the module has got, we can use help(math), or dir(math).
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
print(pi)

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2.0

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(log10(100))          # 2.0

from math import pi as  PI
print(PI) # 3.141592653589793

#   String Module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#   Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive