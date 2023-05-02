#     Day 6: Tuples

# Exercises: Level 1
# 1. Create an empty tuple
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# 3. Join brothers and sisters tuples and assign it to siblings
# 4. How many siblings do you have?
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings = ()
sisters = ('Sele', 'Rocio', 'Marcelyn', 'Miley', 'Yin')
brothers = ('Leo', 'flanders')
siblings = sisters + brothers
print('How many siblings do you have?: ', len(siblings))
family_members = list(siblings)
family_members.extend(['Juan', 'Paulina'])
family_members = tuple(family_members)
print(family_members)


# Exercises: Level 2
# 1. Unpack siblings and parents from family_members
siblings=family_members[0:-2]
parents= family_members[-2:]
print(siblings) # ('Sele', 'Rocio', 'Marcelyn', 'Miley', 'Yin', 'Leo', 'flanders')
print(parents)  # ('Juan', 'Paulina')

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits= ('banana', 'orange', 'apple')
vegetables=('onion', 'garlic', 'carrot')
animal=('milk', 'asado')
food_stuff_tp= fruits + vegetables + animal

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt= list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index  = (len(food_stuff_tp)-1)//2
print(food_stuff_tp[middle_index])
print(food_stuff_lt[middle_index])

# 5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3]) # ['banana', 'orange', 'apple']
print(food_stuff_lt[-3:]) # ['carrot', 'milk', 'asado']

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#   a. Check if 'Estonia' is a nordic country
#   b. Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('"Estonia" is a nordic country: ', 'Estonia' in nordic_countries)
print("'Iceland' is a nordic country: ", 'Iceland' in nordic_countries)