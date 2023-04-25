# Day 2: 30 Days of python programming

# Let's declare variables with various data types

first_name = 'Araceli'   # str
year= 2023               # int
is_true=False            # bool

last_name, country, age, is_married = 'Vera', 'Argentina', 250, True

print(type(first_name))  # str
print(type(year))        # int
print(type(is_true))     # bool

# Built in functions
#Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().

print(len(first_name))    #7
print(min(20,30,40,50))   #20
print(max([20,30,40,50])) #50
print(sum([20,30,40,50])) #140

# Exercises level 2

# 5. The radius of a circle is 30 meters.
#    i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#    2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#    3. Take radius as user input and calculate the area.

radius=30
area_of_circle = 3.14*(radius)**2
circum_of_circle = 2*3.14*radius
print(area_of_circle)
print(circum_of_circle)

radius=int(input("Enter the radius of a circle: "))
area_of_circle = 3.14*radius**2
print(area_of_circle)

