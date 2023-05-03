#   Day 9 - 30DaysOfPython Challenge

#   Conditionals: if, else, elif 

# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:
# - Conditional execution: a block of one or more statements will be executed if a certain expression is true
# - Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true.

#   If Condition
condition = True
if condition:
  print(" this part of code runs for truthy conditions")

# Example:
a = 3
if a > 0: # True
    print('A is a positive number') # A is a positive number

# The condition was true and the block code was executed. However, if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be else:

#   If Else
condition = False
if condition:
  print("this part of code runs for truthy conditions")
else: 
  print("this part of code runs for false conditions") # this part of code runs for false conditions

# Example:
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number') # A is a positive number


#   If Elif Else
#  We use elif when we have multiple conditions.
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero') # A is zero


#   Short Hand
# code if condition else code
a = 3
print('A is positive') if a > 0 else print('A is negative') # 'A is positive'


#   Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero') # 'A os zero'
else:
    print('A is a negative number')
# We can avoid writing nested condition by using logical operator and:


#   If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero') # 'A is zero'
else:
    print('A is negative')
 
  
#   If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')