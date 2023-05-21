#   Day 14 - Higher Order Functions

#  Exercises Level 1

# 1. Explain the difference between map, filter, and reduce.

'''
  map(function, iterable):
map applies the given function to each item in the iterable and returns a new iterable containing the results.

  filter(function, iterable):
filter applies the given function to each item in the iterable and returns a new iterable containing only the elements for which the function returns True.

  reduce(function, iterable):
reduce applies the given function to the first two elements of the iterable, then applies it to the result and the next element, and continues until all elements are processed.
'''

# 2. Explain the difference between higher order function, closure and decorator
'''
 a higher-order function takes one or more functions as arguments or returns a function as its result, closures allows a nested function to access the outer scope of the enclosing function, and decorators enhance functions by wrapping them with additional functionality.
'''
# 3. 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
for country in countries :
  print(country)
# Use for to print each name in the names list.
for name in names:
  print(name)
# Use for to print each number in the numbers list.
for number in numbers:
  print(number)

#   Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def change_to_upper(string):
    return string.upper()
countries_upper_cased =map(change_to_upper, countries) 
print(list(countries_upper_cased))

# 2. Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(number):
  return number ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# 3. Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
names_upper_cased = list(map(change_to_upper, names))
print(names_upper_cased)

# 4. Use filter to filter out countries containing 'land'.
def is_land_in_country(country):
  if 'land' in country:
    return True
  return False
countries_with_land = list(filter(is_land_in_country, countries))
print(countries_with_land)

# 5. Use filter to filter out countries having exactly six characters.
def only_six_characters(country):
  if len(country)== 6:
    return True
  return False
countries_with_six_characters = list(filter(only_six_characters,countries))
print(countries_with_six_characters)

# 6. Use filter to filter out countries containing six letters and more in the country list.
def is_country_long(country):
  if len(country)>= 6:
    return True
  return False
long_countries = list(filter(is_country_long, countries))
print(long_countries)
                
# 7. Use filter to filter out countries starting with an 'E'
def is_starting_with(country):
  if country[0] == 'E':
    return True
  return False
countries_starting_with_E= list(filter(is_starting_with, countries))
print(countries_starting_with_E)

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
def map_filter_reduce(arr, map_callback, filter_callback, reduce_callback):
    mapped = map(map_callback, arr)
    filtered = filter(filter_callback, mapped)
    result = reduce(reduce_callback, filtered)
    return result

arr = [1, 2, 3, 4, 5]

result = map_filter_reduce(
    arr,
    lambda x: x**2,
    lambda x: x % 2 == 0,
    lambda x, y: x + y
)
print(result) 

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def is_item_a_string(item):
  if type(item) == str: 
    return True
  return False
def get_string_lists(lst):
  return list(filter(is_item_a_string, lst))

my_list = [1, "apple", "banana", 3.14, "orange"]
print(get_string_lists(my_list))


# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
numbers_list = [1, 2, 3, 4, 5]

def add_two_nums(x, y):
    return x + y
total = reduce(add_two_nums, numbers_list)
print(total)  

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

sentence = reduce(lambda x, y: x + ', ' + y, countries)
sentence = sentence + ' are north European countries.'

print(sentence)

# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def count_countries_by_letter(countries):
    country_counts = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in country_counts:
            country_counts[first_letter] += 1
        else:
            country_counts[first_letter] = 1
    return country_counts
  
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Spain', 'Senegal']
country_counts = count_countries_by_letter(countries)
print(country_counts)