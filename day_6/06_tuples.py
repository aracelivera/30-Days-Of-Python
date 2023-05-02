#   Day 6 - 30DaysOfPython Challenge

#   Tuples

# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator + : to join two or more tuples and to create a new tuple

# Creating an empty tuple
empty_tuple = ()
#or
empty_tuple = tuple() #()

# Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple lenght
len(fruits) # 4

# Accessing Tuple Items
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
# Negative indexing
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing tuples
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3 (-1)
orange_to_the_rest = fruits[-3:]

# Changing Tuples to Lists
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
print('orange' in fruits) # True
print('apple' in fruits) # True
fruits[0] = 'banana' # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1