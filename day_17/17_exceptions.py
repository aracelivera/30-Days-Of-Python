##  Day 17 - 30DaysOfPython Challenge

##  Exception Handling & Packing and Unpacking Arguments in Python

# Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust.

# try:
#    code in this block if things go well
# except:
#    code in this block run if things go wrong

# Example 1
try:
    print(10 + '5')
except:
    print('Something went wrong') #the except block will be executed
    
# Example 2

try:
    name = input('\nEnter your name:')
    year_born = input('Year you were born:')
    age = 2023 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong') # the exception block will run and we do not know exactly the problem.

# Example 3
# In the following example, it will handle the error and will also tell us the kind of error raised.

try:
    name = input('\nEnter your name:')
    year_born = input('Year you were born:')
    age = 2023 - year_born  # no se ejecuta
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured') # Type error occured
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# Example 4, finally block

try:
    name = input('\nEnter your name:')
    year_born = input('Year you born:')
    age = 2023 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block') # I usually run with the try block
finally:
    print('I alway run.') #I alway run. 

# It is also shorten the above code as follows:

try:
    name = input('\nEnter your name:')
    year_born = input('Year you born:')
    age = 2023 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


# Packing and Unpacking Arguments in Python

# * for tuples, lists
# ** for dictionaries

# Unpacking Lists
#Example 1
def sum_of_five_nums(a, b, c, d, e): #this function takes numbers (not a list) as arguments
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# Example 2
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(list(numbers))    # [2, 3, 4, 5,6]

# Example 3
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)   #  1 [2, 3, 4, 5, 6] 7

# Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. She is {age} year old.'
dct = {'name':'Ara', 'country':'Argentina', 'city':'Buenos Aires', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


# Packing

# Packing Lists
def sum_all(*args): # We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# Packing Dictionaries
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Araceli", country="Argentina", city="Buenos Aires", age=250))

# Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Enumerate : to get the index of each item in the list
for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries= ['Denmark','Finland', 'Sweden', 'Norway']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}') # The country Finland has been found at index 1

# Zip : to combine lists when looping through them. 
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)




