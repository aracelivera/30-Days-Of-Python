##   Day 18 - Regular Expressions

## Exercises: Level 1

# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
import re
from collections import Counter

# r'[^\w\s]' matches any character that is not a word character or a whitespace character  to remove punctuation marks from the paragraph by replacing them with an empty string , and then converting to lowercase
paragraph = re.sub(r'[^\w\s]', '', paragraph).lower()
# Creating Counter object from the preprocessed paragraph
counter_dict = Counter(paragraph.split()) 
# Creating the desired list format
count_word_list = [(count, word) for word, count in counter_dict.items()]
# Sorting the list by count in descending order
desired_list = sorted(count_word_list, key=lambda x: x[0], reverse=True)

print(desired_list)


# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
import re
txt= 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

regex_pattern = r'-?\d' # # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)
points = list(map(int, matches))
sorted_points = sorted(points)
print(sorted_points)
print('distance: ', sorted_points[-1]-sorted_points[0]) #12


## Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable
import re
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable) is not None
  
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))  # True
print(is_valid_variable('first name')) # False


## Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.
import re
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
  return re.sub(r'[^a-zA-Z\s]', '', txt)
'''
def most_frequent_words(text):                  # otra forma
    word_count=  Counter(text.split()).items()
    count_word= [(count, word) for word, count in word_count]
    sorted_words = sorted(count_word, key=lambda x: x[0], reverse=True)
    return sorted_words[:3]
'''
def most_frequent_words(text):
    word_count=  Counter(text.split())
    return [(count, word) for word, count in word_count.most_common(3)]

print(clean_text(sentence))
print(most_frequent_words(clean_text(sentence)))