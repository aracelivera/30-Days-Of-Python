#  Exercises - Day 3

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base= int(input('Enter base of the triangle: '))
height= int(input('Enter height of the triangle: '))
area= 0.5 * base * height
print('The area of the triangle is: ', area)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'))
print(len('dragon'))
print(len('python') != len('dragon')) # False

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('"on" is found in both "python" and "dragon": ', 'on' in 'python' and 'on' in 'dragon') # True

# 14. 'I hope this course is not full of jargon'. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon') # True

# 15. There is no 'on' in both dragon and python.
print(not('on' in 'python' and 'on' in 'dragon')) # False

# 16. Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number=int(input("Enter a number: "))
print("The number entered is divisible by 2: ", number % 2 == 0)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print( 7//3 == int(2.7)) # True

# 19. Check if type of '10' is equal to type of 10
print(type('10')==type(10)) # False

# 20. Check if int('9.8') is equal to 10
print(int(9.8)==10) # False
