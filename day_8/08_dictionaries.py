#   Day 8 - 30DaysOfPython Challenge

#   Dictionaries

# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# Example:
person = {
    'first_name':'Araceli',
    'last_name':'Vera',
    'age':250,
    'country':'Argentina',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    } # The values could be any data types: string, boolean, list, tuple, set or a dictionary.

# Dictionary Length
print (len(person)) # 7

# Accessing Dictionary Items
print(person['first_name']) # Araceli
print(person['country'])    # Argentina
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # KeyError

# get()
# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML') # because it's a list
print(person) # {'first_name': 'Araceli','last_name': 'Vera', 'age': 250, 'country': 'Argentina', 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 'address': {'street': 'Space street', 'zipcode': '02210'}, 'job_title': 'Instructor'}

# Modifying Items in a Dictionary
person['first_name'] = 'Ayelen'
person['age'] = 26
print(person)

# Checking Keys in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name.
# del: "" "" "" "" "" "" "" "".
# popitem(): removes the last item.
person = {
    'first_name':'Araceli',
    'last_name':'Vera',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
print(dct) # Error

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting Dictionary Keys as a List
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])