#   Day 10 - 30DaysOfPython Challenge

#   Loops: while, for 


#   While Loop
# It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.
count = 0
while count < 5:
    print(count)
    count = count + 1
    
# prints from 0 to 4 as the condition becomes false when count is 5. That is when the loop stops.
# If we are interested to run block of code once the condition is no longer true, we can use else:
count = 0
while count < 5: 
    print(count)  # 0, 1, 2, 3, 4 (line by line)
    count = count + 1  
else:
    print(count) # 5


#   Break and Continue - Part 1
# We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)     #  0, 1, 2 (line by line)
    count = count + 1
    if count == 3:
        break    
      
# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count) #  0, 1, 2 and 4 
    count = count + 1


#   For Loop

# For loop with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    print(number)       # the numbers will be printed line by line, from 0 to 5

# For loop with string
language = 'Python'
for letter in language:
    print(letter)  #  from 'P' to 'n'

for i in range(len(language)): # range starts from 0 to len(language)-1
    print(language[i])
    
# For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) 

# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

#   Break and Continue - Part 2

# Break: To stop our loop
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
# Continue: Tto skip some of the steps 
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") 
print('outside the loop')

# The Range Function
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10

# Nested For Loop
person = {
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

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number) # 10

# Pass

for number in range(6):
    pass # we can use it as a placeholder for future statements and avoid errors