#   Day 12 - Modules

#  Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
import random
import string

def random_user_id():
    characteres = string.ascii_letters + string.digits
    # 'choices' function returns a LIST of characters, so ''.join() is then used to join these characters together into a single string without any separator.
    id = ''.join(random.choices(characteres, k=6))
    return str(id)
print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def _id_gen_by_user():
    number_of_characters = int(input('Enter the number of characters of each ID to generate: '))
    number_of_ids = int(input('Enter the number of IDs to generate: '))
    characteres = string.ascii_letters + string.digits
    for i in range(number_of_ids):
      print(''.join(random.choices(characteres, k=number_of_characters)))      
_id_gen_by_user()

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
from random import randint

def rgb_color_gen():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    print(f'rgb({red},{green},{blue})')
rgb_color_gen()

#   Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors():
    hexa_symbols = "0123456789abcdef"
    # 'choices' function returns a LIST of characters, so ''.join() is then used to join these characters together into a single string without any separator.
    hexa_number = '#'+ ''.join(random.choices(hexa_symbols, k=6))
    hexa_list = [hexa_number]
    return hexa_list
print(list_of_hexa_colors())

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
from random import randint

def list_of_rgb_colors():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb_color = f'rgb({red},{green},{blue})'
    return [rgb_color]
print(list_of_rgb_colors())

#. 3 Write a function generate_colors which can generate any number of hexa or rgb colors.
from random import choices, randint

def generate_colors(format, number):
    if format == 'rgb':
        rgb_list=[]
        for i in range(number):
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            rgb_color = f'rgb({red},{green},{blue})'
            rgb_list.append(rgb_color)
        print(rgb_list)
    elif format == 'hexa':
        hexa_list = []
        for i in range(number):
            hexa_symbols = "0123456789abcdef"
            hexa_number = '#'+ ''.join(choices(hexa_symbols, k=6))
            hexa_list.append(hexa_number)
        print(hexa_list)
     
generate_colors('hexa', 1)
generate_colors('rgb', 3)

#   Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
from random import shuffle
def shuffle_list(lst):
    shuffled_lst = lst.copy()
    shuffle(shuffled_lst)
    return shuffled_lst
lst=['Ivan', 32, 'Ara', 1]
print(shuffle_list(lst))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
from random import randint
def seven_random_numbers():
    numbers_list = [randint(0, 9)]
    count = 1
    while count < 7:
        random_number = randint(0,9)
        if not (random_number in numbers_list):
            numbers_list.append(random_number)
            count += 1
    return numbers_list
print(seven_random_numbers())