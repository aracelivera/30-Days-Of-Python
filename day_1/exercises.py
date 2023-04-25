''' 
  Exercises: Level 3

 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
 
'''

print(type(26))  # Int
print(type(3.33))  # Float
print(type(2 + 1j))  # Complex number
print(type('Araceli'))  # String
print(type(['avocado', 3, True, 9.6]))  # List
print(type({'name': 'Araceli',
            'last_name': 'Vera',
            'skills':['cloud', 'linux', 'networking']
            }))  # Dictionary
print(type({9.8, 3.14, 2.7}))  # Set
print(type((9.8, 3.14, 2.7)))  # Tuple

'''
  2. Find an Euclidian distance between (2, 3) and (10, 8).
  
  eucladian-distance(p,q)= ((q1-p1)**2 + (q2-p2)**2)**1/2

'''
print(((10-2)**2 + (8-3)**2)**1/2)