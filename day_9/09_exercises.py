#     Day 9: Conditionals

#  Exercises: Level 1

'''
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
    Enter your age: 230
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
'''
# Solution
age= int(input('Enter your age: '))
if age >= 18:
  print("You are old enough to drive.")
else:
  print(f"You need {18 - age} more years to learn to drive.")

'''
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    Enter your age: 30
    You are 5 years older than me.
'''
# Solution 1 - Nested Condition
my_age = 25
your_age = int(input('Enter your age: '))
if your_age > my_age: 
  if your_age - my_age == 1:
    print(f'You are a year older than me.')
  else:
    print(f'You are {your_age - my_age} years older than me.')
elif  your_age < my_age:  
  if my_age - your_age == 1:
    print(f'You are a year younger than me.')
  else:
    print(f'You are {my_age - your_age} years younger than me')
else: 
  print("We are the same age")

# Solution 2 - elif
my_age = 25
your_age = int(input('Enter your age: '))
if abs(my_age-your_age) == 1: 
  print('Year')
elif your_age > my_age: 
  print(f'You are {your_age - my_age} years older than me.')
elif your_age < my_age: 
  print(f'You are {my_age - your_age} years younger than me')
else: 
  print("We are the same age")
  
'''
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
  Enter number one: 4
  Enter number two: 3
  4 is greater than 3
'''
# Solution
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
  print(f'{a} is greater than {b}')
elif a < b:
  print(f'{a} is smaller than {b}')
else:
  print(f'{a} is equal to {b}')
  

#  Exercises: Level 2

'''
1. Write a code which gives grade to students according to theirs scores:

  80-100, A
  70-79, B
  60-69, C
  50-59, D
  0-49, F
'''
# Solution
score= int(input('Enter score: '))
if score>=80 and score<=100:
  print('A')
elif score>=70 and score<= 79: 
  print('B')
elif score>=60 and score<=69:
  print('C')
elif score>=50 and score<=59:
  print('D')
elif score>=0 and score<=49:
  print('F')
else:
  print('Invalid score')

'''
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
'''
# Solution
season = input('Enter a month: ')
if season == 'September' or season == 'October' or season == 'November':
  print('The season is Autumn')
elif season == 'December' or season == 'January' or season == 'February':
  print('The season is Winter')
elif season == 'March' or season == 'April' or season =='May':
  print('The season is Spring')
elif season == 'June' or season == 'July' or season == 'August':
  print('The season is Summer')

'''
The following list contains some fruits:

    fruits = ['banana', 'orange', 'mango', 'lemon']
    
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
# Solution:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_add = input('Enter a fruit: ')
    
if fruit_to_add in fruits:
    print('That fruit already exists in the list')
else: 
    fruits.append(fruit_to_add)
print(fruits)


#  Exercises: Level 3

# 4. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Araceli',
    'last_name': 'Vera',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# a. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    print(person['skills'][(len(person['skills'])-1)//2]) # Node

# b. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
  if 'Python' in person['skills']:
    print("the person has 'Python' as a skill")

# c. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'Javascript' in person['skills'] and 'React' in person['skills'] and len(person['skills']==2):
  print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
  print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
  print('He is a fullstack developer')
else:
  print('unknown title') 
  
# d. If the person is married and if he lives in Finland, print the information in the following format:
#  Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred']== True and person['country']== 'Finland':
  print(f'{person["first_name"]} {person["last_name"]} is married and she lives in {person["country"]}')
 
