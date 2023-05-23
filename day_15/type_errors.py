##  Day 15 - 30DaysOfPython Challenge

##  Type Errors

# SyntaxError
# print 'hello world'     # SyntaxError: Missing parentheses in call to 'print'. 
print('hello world')

# NameError
# print(age)      # NameError: name 'age' is not defined
age = 25
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
# print(numbers[5])      # IndexError: list index out of range 
print(numbers[4])

# ModuleNotFoundError
# import maths      # ModuleNotFoundError: No module named 'maths'
import math

# AttributeError
# print(math.PI)     # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
user = {'name':'Ara', 'age':250, 'country':'Finland'}
print(user['name'])
# print(user['county'])    # KeyError: 'county'
print(user['country'])

# TypeError
# print(4+'3')    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(4 + int('3'))
print(4 + float('3'))

# ImportError
# from math import power      # ImportError: cannot import name 'power' from 'math' (unknown location)
from math import pow
print(pow(2,3))

# ValueError
# int('12a')      ValueError: invalid literal for int() with base 10: '12a'
int('12')

# ZeroDivisionError
# print(1/0) #division by zero