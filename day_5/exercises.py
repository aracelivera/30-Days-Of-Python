# Exercises: Level 1


# 1. Declare an empty list
list=[]

# 2. Declare a list with more than 5 items
list=['oma', 'ivan', 'ara', 'cat', 1, 2]

# 3. Find the length of your list
print(len(list))

# 4. Get the first item, the middle item and the last item of the list
print(list[0]) #first item
print(list[(len(list)-1)//2]) #middle item
print(list[len(list)-1]) #last item

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['ara', '105', '1.60', 'Divorced', 'calle falsa 123']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print('Number of companies in the list: ', len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0]) #first item
print(it_companies[(len(it_companies)-1)//2]) #middle item
print(it_companies[len(it_companies)-1]) #last item

# 10. Print the list after modifying one of the companies
it_companies[2]= 'OpenIA'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('SAP')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert((len(it_companies)-1)//2,'Salesforce')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]= it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
it_companies.extend('#; ')
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
print('IBM exists in the it_companies list: ', 'IBM' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
index_middle = (len(it_companies)-1)//2
print(it_companies[index_middle - 1: index_middle + 2 ])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[(len(it_companies)-1)//2]
print(it_companies)
# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
del it_companies[0:]
print(it_companies)
# 25. Destroy the IT companies list
del it_companies
print(it_companies)

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Redux')+2, 'SQL')
print(full_stack) # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']


#   Exercises: Level 2


# 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#   a. Sort the list and find the min and max age
ages.sort()
min_age= ages[0]
max_ege= ages[len(ages) - 1]
print('Min age: ', min_age)
print('Max age: ', max_ege)

#   b. Add the min age and the max age again to the list
ages.extend([min_age, max_ege])
print(ages)

#   c. Find the median age (one middle item or two middle items divided by two)
ages.sort()
median_age_index= (len(ages)-1)//2
print(ages[median_age_index])

#   d. Find the average age (sum of all items divided by their number )
sum=0
for age in ages:
  sum+=age
avg= sum/(len(ages)-1)
print(f'Average of ages: {avg:.2f}')

# 2. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries[(len(countries)-1)//2])

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.

if (len(countries))%2 == 0:
  first_half_countries = countries[0 : (len(countries)-1)//2+1]
  second_half_countries = countries[(len(countries)-1)//2+1: ]
else:
  first_half_countries = countries[0 : (len(countries)-1)//2+2]
  second_half_countries = countries[(len(countries)-1)//2+2: ]

print(first_half_countries) #era impar
print(second_half_countries)

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

china, russia, usa, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print (f'{china}\n{russia}\n{usa}\n{scandic_countries}') 
