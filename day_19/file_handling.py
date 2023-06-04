##  Day 19 - 30DaysOfPython Challenge  ##

##  File Handling

# File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.

# Syntax
#   open('filename', mode) 

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# Opening Files for Reading
f = open('./day_19/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./day_19/reading_file_example.txt' mode='r' encoding='cp1252'>

# read(): read the whole text as string
f = open('./day_19/reading_file_example.txt')
txt = f.read()
print(type(txt)) # <class 'str'>
print(txt) # This is an example to show how to open a file and read...
f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.
f = open('./day_19/reading_file_example.txt')
txt = f.read(10)
print(type(txt)) # <class 'str'>
print(txt) # This is an
f.close()

# readline(): read only the first line
f = open('./day_19/reading_file_example.txt')
line = f.readline()
print(type(line)) # <class 'str'>
print(line) # This is an example to show how to open a file and read.
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('./day_19/reading_file_example.txt')
lines = f.readlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./day_19/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.', 'This is the second line of the text.'] 
f.close()

# After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using with - closes the files by itself. Let us rewrite the previous example with the with method:

with open('./day_19/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines)) # <class 'list'>
    print(lines) # ['This is an example to show how to open a file and read.', 'This is the second line of the text.'] 


# Opening Files for Writing and Updating

# To write to an existing file, we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

with open('./day_19/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./day_19/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')   
  
    
# Deleting Files

# import os
# os.remove('./day_19/example.txt')

# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
import os
if os.path.exists('./day_19/example.txt'):
    os.remove('./day_19/example.txt')
else:
    print('The file does not exist')
    
    
# File Types

# File with txt Extension (we have covered it above)

# File with json Extension

# JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)
print(type(person_dct)) # <class 'dict'>
print(person_dct) # {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
print(person_dct['name']) # Asabeneh

# Changing Dictionary to JSON
import json
# dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json)) # <class 'str'>
print(person_json)

# Saving as JSON File
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./day_19/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)  # For writing a json file, we use the json.dump() method. ndentation makes the json file easy to read.


# File with csv Extension

# CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database.
import csv
with open('./day_19/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
#output:
# Column names are :name, country, city, skills
#        Asabeneh is a teachers. He lives in Finland, Helsinki.
# Number of lines:  2


# File with xlsx Extension

# To read excel files we need to install xlrd package using pip.
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


# File with xml Extension

# XML is another structured data format which looks like HTML. In XML the tags are not predefined.
# How to read XML files: https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
tree = ET.parse('./day_19/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
# output:
# Root tag: person
# Attribute: {'gender': 'female'}
# field:  name
# field:  country
# field:  city
# field:  skills