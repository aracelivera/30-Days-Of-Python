#   Day 7 - 30DaysOfPython Challenge

#   Sets

# Set is a collection of items. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# Creating an empty set
st = {}
# or
st = set()

# Creating a set with initial items
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's Length
len(fruits)

# Checking an Item
print('mango' in fruits ) # True

# Add one item using add()
fruits.add('lime')

# Add multiple items using update(), it takes a list argument.
fruits.update(['apple', 'cherry'])
#or
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# Removing items from a Set
# remove(), discard()
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st.discard('item2')) #none
print(st.remove('item2')) #  If the item is not found remove() method will raise errors.
# pop()
fruits.pop()  # removes a random item from the set and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

# Clearing Items in a Set (empty)
fruits.clear()
print(fruits) # set()

# Deleting a Set
del fruits
print(fruits) #NameError: name 'fruits' is not defined

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'} - the order is random, because sets in general are unordered

# Joining Sets: 
#union()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7'}
st3 = st1.union(st2) # lo tengo q guardarr
print(st1) # {'item3', 'item1', 'item2', 'item4'}
#update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Finding intersection Items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# examples:
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

# Checking Subset and Super Set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

# Checking the Difference Between Two Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}


# Finding Symmetric Difference Between Two Sets
# it means that it returns a set that contains all items from both sets, except items that are present in both sets (intersection), mathematically (A\B)∪(B\A)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.symmetric_difference(st1) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

#  Disjoint Sets
# If two sets do not have a common item or items we call them disjoint sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))# False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

