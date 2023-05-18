#   Day 13 - List comprehension, lambda functions

#  Exercises

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [i for i in numbers if i>0]
print(lst)

# 2. Flatten the following list of lists of lists to a one dimensional list:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using list comprehension create the following list of tuples:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuples= [(i, 1, i*1, i*i, i**3, i**4, i**5) for i in range (11)]
print(list_of_tuples)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flattened_list = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for (country, city) in sublist]
print(flattened_list)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]

countries_dict = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]
print(countries_dict)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

list_of_concatenated_strings = [name+' '+lastname for person in names for (name, lastname) in person]
print(list_of_concatenated_strings)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_function = lambda x1, y1, x2, y2, parameter: (y2 - y1) / (x2 - x1) if parameter == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1

slope = linear_function(2, -4, 6, 10, 'slope')
y_intercept = linear_function(2, -4, 6, 10, 'y-intercept')

print(f"Slope: {slope}")
print(f"Y-Intercept: {y_intercept}")