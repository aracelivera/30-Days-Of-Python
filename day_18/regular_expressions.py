##  Day 18 - 30DaysOfPython Challenge

##  Regular Expressions

# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

import re

# Methods in re Module

# Match
# The match function returns an object only if the text starts with the pattern, else returns None.
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I) # re.I is case ignore
print(match) # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# Search
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# Search returns a match object with a first match that was found,
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
span = match.span()
print(span)     # (100, 105)
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)   # first

# Searching for All Matches Using findall
# re.findall: Returns a list containing all matches

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

# If we do not have the re.I flag, then we will have to write our pattern differently. Let us check it out:
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# Replacing a Substring
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) 
# ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']


#   Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or 
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# meta characteres:
# https://docs.python.org/3/library/re.html

# Square Bracket
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple|[Bb]anana' # r'apple|banana' means either apple or a banana
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

# Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

# One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

# Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means [a]followed by any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are delicious fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are delicious fruits']

# Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier in RegEx
# We can specify the length of the substring we are looking for in a text, using a curly bracket.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# Cart ^

# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negation
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']