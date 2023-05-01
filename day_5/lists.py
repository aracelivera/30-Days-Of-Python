#   Day 5 - 30DaysOfPython Challenge

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.

# In Python we can create lists in two ways:
empty_list = list() 
print(len(empty_list)) # 0
# or
empty_list = [] 
print(len(empty_list)) # 0

# Lists with initial values
fruits = ['banana', 'orange', 'mango', 'lemon'] 
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]

# Accessing List Items Using Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] 
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit) # lemon

# Accessing List Items Using Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

# Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:] # or fruits[:]
print(all_fruits)
print(fruits[1:3]) # ['orange', 'mango'] , it does not include the last index
print(fruits[1:]) # ['orange', 'mango', 'lemon']
print(fruits[::2]) # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits)
print(fruits[-3:-1]) # it does not include the last index,['orange', 'mango']
print(fruits[-3:]) # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
print(fruits[::-1]) # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

# Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits) #  ['avocado', 'orange', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits) #  ['avocado', 'apple', 'mango', 'lime']

# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
print('lime' in fruits)  # False

# Adding Items to the END of a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']

# Inserting Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']

# Removing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list

# Removing Items Using Pop (and return the item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop() # last item
print(fruits)       # ['banana', 'orange','mango']
print(fruits.pop(0)) # 'banana'   
print(fruits) # ['orange', 'mango']

# Removing Items Using Del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1:3]  # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)  # ['orange','kiwi', 'lime']
del fruits  #delete the list completely
print(fruits)       # NameError: name 'fruits' is not defined

# Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) # []

# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# Joining Lists : There are several ways to join two or more lists 
# Plus Operator (+):
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# Joining using extend() method:
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Counting Items in a List:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) # 3

# Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

# Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']

# Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() # sorted in alphabetical order
print(fruits) # ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

# sorted(): returns the ordered list 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits,reverse=True)) # ['orange', 'mango', 'lemon', 'banana']
