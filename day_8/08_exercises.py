#     Day 8: Dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Jupiter'
dog['color'] = 'black'
dog['breed'] = 'boxer'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Ara',
    'last_name': 'Vera',
    'gender': 'Female',
    'age': 26,
    'marital_status': 'merried',
    'country': 'Argentina',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 4. Get the length of the student dictionary
print(len(student)) #8

# 5. Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['Docker', 'AWS'])
print(student)

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
student.pop('age')
print(student)

# 11. Delete one of the dictionaries
del student