#     Day 11: Functions


#  Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(5, 7))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area
print(area_of_circle(2))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for num in nums:
        if type(num) == int or type(num) == float:
            list_of_numers = True
        else:
            list_of_numers= False
    if list_of_numers:
        sum = 0
        for num in nums:
            sum += num
        return sum
    else:
        print('List items have to be numbers')

print(add_all_nums(1, 2, 5))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f= (c*9/5) + 32
    return f
celsius= 20
print(f'{celsius}°C are equivalent to {convert_celsius_to_fahrenheit(20)}°F')

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(season):
    if season == 'September' or season == 'October' or season == 'November':
        return 'Autumn'
    elif season == 'December' or season == 'January' or season == 'February':
        return 'Winter'
    elif season == 'March' or season == 'April' or season =='May':
        return 'Spring'
    elif season == 'June' or season == 'July' or season == 'August':
        return 'Summer'  
print('The season is ', check_season('January'))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 -4* a *c
    if discriminant>0:
        x1= (-b + (discriminant)*1/2) / 2*a
        x2 = (-b - (discriminant)*1/2) / 2*a
        return x1, x2
    elif discriminant==0:
         x1= (-b + (discriminant)*1/2) / 2*a
         return x1
    else:
        print('Complex roots')
print(solve_quadratic_eqn(1,-4,4))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(xlist):
    for element in xlist:
        print(element)
print_list([2.4,'perro','Ara'])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
'''
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
'''
def reverse_list(array):
    reverse_array = []
    for i in range(len(array)-1,-1, -1 ):
        reverse_array.append(array[i])
    return reverse_array

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))      
        

#   Exercises: Level 2

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
def evens_and_odds(number):
    if type(number) == int and number>=0:
        count_evens=0
        count_odds=0
        for i in range(number+1):
            if i%2==0:
                count_evens+=1
            else:
                count_odds+=1
        print(f"The number of odds in are ", count_odds,"\nThe number of evens in are ", count_evens )
evens_and_odds(4)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if type(number)== int:
        factorial=1
        for i in range(1, number+1):
            factorial*=i
        return factorial
num=6
print(f'The factorial of {num} is {factorial(num)}')

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param:
        return False
    else:
        return True
    
# Example usage
empty_list = []
non_empty_list = [1, 2, 3]

print(is_empty(empty_list))  # Output: True
print(is_empty(non_empty_list))  # Output: False


# Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num>1:
        for i in range(1, num+1):
            if i!=1 and i!=num and num%i==0:
                return False
    return True

print(is_prime(563))

# 2. Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
   return len(lst) == len(set(lst)) # In Python set is used to store unique items, it's an unordered collection

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 3, 4]
print(are_all_items_unique(list1))  # True
print(are_all_items_unique(list2))  # False

# 3. Write a function which checks if all the items of the list are of the same data type.
def are_all_items_same_type(lst):
    if not lst:  # Check if the list is empty, and if it is we return True
        return True 
    data_type= type(lst[0]) 
    for item in lst:
        if type(item) != data_type:
            return False
    return True
    
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, "four", 5]
list3 = []
print(are_all_items_same_type(list1))  # True
print(are_all_items_same_type(list2))  # False
print(are_all_items_same_type(list3))  # True
print(are_all_items_same_type(["apple", "banana", "cherry"]))  # True

# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    return variable.isidentifier()

var1 = "valid_variable"
var2 = "123_invalid_variable"
var3 = "invalid variable"
var4 = "validVariable123"

print(is_valid_variable(var1))  # Output: True
print(is_valid_variable(var2))  # Output: False
print(is_valid_variable(var3))  # Output: False
print(is_valid_variable(var4))  # Output: True

# 5. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order.
countries = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
    {
        "name": "Bahrain",
        "capital": "Manama",
        "languages": [
            "Arabic"
        ],
        "population": 1404900,
        "flag": "https://restcountries.eu/data/bhr.svg",
        "currency": "Bahraini dinar"
    },
    {
        "name": "Bangladesh",
        "capital": "Dhaka",
        "languages": [
            "Bengali"
        ],
        "population": 161006790,
        "flag": "https://restcountries.eu/data/bgd.svg",
        "currency": "Bangladeshi taka"
    },
    {
        "name": "Barbados",
        "capital": "Bridgetown",
        "languages": [
            "English"
        ],
        "population": 285000,
        "flag": "https://restcountries.eu/data/brb.svg",
        "currency": "Barbadian dollar"
    },
    {
        "name": "Belarus",
        "capital": "Minsk",
        "languages": [
            "Belarusian",
            "Russian"
        ],
        "population": 9498700,
        "flag": "https://restcountries.eu/data/blr.svg",
        "currency": "New Belarusian ruble"
    },
    {
        "name": "Belgium",
        "capital": "Brussels",
        "languages": [
            "Dutch",
            "French",
            "German"
        ],
        "population": 11319511,
        "flag": "https://restcountries.eu/data/bel.svg",
        "currency": "Euro"
    },
    {
        "name": "Belize",
        "capital": "Belmopan",
        "languages": [
            "English",
            "Spanish"
        ],
        "population": 370300,
        "flag": "https://restcountries.eu/data/blz.svg",
        "currency": "Belize dollar"
    },
    {
        "name": "Benin",
        "capital": "Porto-Novo",
        "languages": [
            "French"
        ],
        "population": 10653654,
        "flag": "https://restcountries.eu/data/ben.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
    {
        "name": "Bolivia (Plurinational State of)",
        "capital": "Sucre",
        "languages": [
            "Spanish",
            "Aymara",
            "Quechua"
        ],
        "population": 10985059,
        "flag": "https://restcountries.eu/data/bol.svg",
        "currency": "Bolivian boliviano"
    },
    {
        "name": "Bonaire, Sint Eustatius and Saba",
        "capital": "Kralendijk",
        "languages": [
            "Dutch"
        ],
        "population": 17408,
        "flag": "https://restcountries.eu/data/bes.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "languages": [
            "Bosnian",
            "Croatian",
            "Serbian"
        ],
        "population": 3531159,
        "flag": "https://restcountries.eu/data/bih.svg",
        "currency": "Bosnia and Herzegovina convertible mark"
    },
    {
        "name": "Botswana",
        "capital": "Gaborone",
        "languages": [
            "English",
            "Tswana"
        ],
        "population": 2141206,
        "flag": "https://restcountries.eu/data/bwa.svg",
        "currency": "Botswana pula"
    },
    {
        "name": "Bouvet Island",
        "capital": "",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/bvt.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Brazil",
        "capital": "Brasília",
        "languages": [
            "Portuguese"
        ],
        "population": 206135893,
        "flag": "https://restcountries.eu/data/bra.svg",
        "currency": "Brazilian real"
    },
    {
        "name": "British Indian Ocean Territory",
        "capital": "Diego Garcia",
        "languages": [
            "English"
        ],
        "population": 3000,
        "flag": "https://restcountries.eu/data/iot.svg",
        "currency": "United States dollar"
    },
    {
        "name": "United States Minor Outlying Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 300,
        "flag": "https://restcountries.eu/data/umi.svg",
        "currency": "United States Dollar"
    },
    {
        "name": "Virgin Islands (British)",
        "capital": "Road Town",
        "languages": [
            "English"
        ],
        "population": 28514,
        "flag": "https://restcountries.eu/data/vgb.svg",
        "currency": "[D]"
    },
    {
        "name": "Virgin Islands (U.S.)",
        "capital": "Charlotte Amalie",
        "languages": [
            "English"
        ],
        "population": 114743,
        "flag": "https://restcountries.eu/data/vir.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Brunei Darussalam",
        "capital": "Bandar Seri Begawan",
        "languages": [
            "Malay"
        ],
        "population": 411900,
        "flag": "https://restcountries.eu/data/brn.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Bulgaria",
        "capital": "Sofia",
        "languages": [
            "Bulgarian"
        ],
        "population": 7153784,
        "flag": "https://restcountries.eu/data/bgr.svg",
        "currency": "Bulgarian lev"
    },
    {
        "name": "Burkina Faso",
        "capital": "Ouagadougou",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 19034397,
        "flag": "https://restcountries.eu/data/bfa.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Burundi",
        "capital": "Bujumbura",
        "languages": [
            "French",
            "Kirundi"
        ],
        "population": 10114505,
        "flag": "https://restcountries.eu/data/bdi.svg",
        "currency": "Burundian franc"
    },
    {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "languages": [
            "Khmer"
        ],
        "population": 15626444,
        "flag": "https://restcountries.eu/data/khm.svg",
        "currency": "Cambodian riel"
    },
    {
        "name": "Cameroon",
        "capital": "Yaoundé",
        "languages": [
            "English",
            "French"
        ],
        "population": 22709892,
        "flag": "https://restcountries.eu/data/cmr.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Canada",
        "capital": "Ottawa",
        "languages": [
            "English",
            "French"
        ],
        "population": 36155487,
        "flag": "https://restcountries.eu/data/can.svg",
        "currency": "Canadian dollar"
    },
    {
        "name": "Cabo Verde",
        "capital": "Praia",
        "languages": [
            "Portuguese"
        ],
        "population": 531239,
        "flag": "https://restcountries.eu/data/cpv.svg",
        "currency": "Cape Verdean escudo"
    },
    {
        "name": "Cayman Islands",
        "capital": "George Town",
        "languages": [
            "English"
        ],
        "population": 58238,
        "flag": "https://restcountries.eu/data/cym.svg",
        "currency": "Cayman Islands dollar"
    },
    {
        "name": "Central African Republic",
        "capital": "Bangui",
        "languages": [
            "French",
            "Sango"
        ],
        "population": 4998000,
        "flag": "https://restcountries.eu/data/caf.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chad",
        "capital": "N'Djamena",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 14497000,
        "flag": "https://restcountries.eu/data/tcd.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chile",
        "capital": "Santiago",
        "languages": [
            "Spanish"
        ],
        "population": 18191900,
        "flag": "https://restcountries.eu/data/chl.svg",
        "currency": "Chilean peso"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": [
            "Chinese"
        ],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "Christmas Island",
        "capital": "Flying Fish Cove",
        "languages": [
            "English"
        ],
        "population": 2072,
        "flag": "https://restcountries.eu/data/cxr.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Cocos (Keeling) Islands",
        "capital": "West Island",
        "languages": [
            "English"
        ],
        "population": 550,
        "flag": "https://restcountries.eu/data/cck.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Colombia",
        "capital": "Bogotá",
        "languages": [
            "Spanish"
        ],
        "population": 48759958,
        "flag": "https://restcountries.eu/data/col.svg",
        "currency": "Colombian peso"
    },
    {
        "name": "Comoros",
        "capital": "Moroni",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 806153,
        "flag": "https://restcountries.eu/data/com.svg",
        "currency": "Comorian franc"
    },
    {
        "name": "Congo",
        "capital": "Brazzaville",
        "languages": [
            "French",
            "Lingala"
        ],
        "population": 4741000,
        "flag": "https://restcountries.eu/data/cog.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Congo (Democratic Republic of the)",
        "capital": "Kinshasa",
        "languages": [
            "French",
            "Lingala",
            "Kongo",
            "Swahili",
            "Luba-Katanga"
        ],
        "population": 85026000,
        "flag": "https://restcountries.eu/data/cod.svg",
        "currency": "Congolese franc"
    },
    {
        "name": "Cook Islands",
        "capital": "Avarua",
        "languages": [
            "English"
        ],
        "population": 18100,
        "flag": "https://restcountries.eu/data/cok.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Costa Rica",
        "capital": "San José",
        "languages": [
            "Spanish"
        ],
        "population": 4890379,
        "flag": "https://restcountries.eu/data/cri.svg",
        "currency": "Costa Rican colón"
    },
    {
        "name": "Croatia",
        "capital": "Zagreb",
        "languages": [
            "Croatian"
        ],
        "population": 4190669,
        "flag": "https://restcountries.eu/data/hrv.svg",
        "currency": "Croatian kuna"
    },
    {
        "name": "Cuba",
        "capital": "Havana",
        "languages": [
            "Spanish"
        ],
        "population": 11239004,
        "flag": "https://restcountries.eu/data/cub.svg",
        "currency": "Cuban convertible peso"
    },
    {
        "name": "Curaçao",
        "capital": "Willemstad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi",
            "English"
        ],
        "population": 154843,
        "flag": "https://restcountries.eu/data/cuw.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Cyprus",
        "capital": "Nicosia",
        "languages": [
            "Greek (modern)",
            "Turkish",
            "Armenian"
        ],
        "population": 847000,
        "flag": "https://restcountries.eu/data/cyp.svg",
        "currency": "Euro"
    },
    {
        "name": "Czech Republic",
        "capital": "Prague",
        "languages": [
            "Czech",
            "Slovak"
        ],
        "population": 10558524,
        "flag": "https://restcountries.eu/data/cze.svg",
        "currency": "Czech koruna"
    },
    {
        "name": "Denmark",
        "capital": "Copenhagen",
        "languages": [
            "Danish"
        ],
        "population": 5717014,
        "flag": "https://restcountries.eu/data/dnk.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Djibouti",
        "capital": "Djibouti",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 900000,
        "flag": "https://restcountries.eu/data/dji.svg",
        "currency": "Djiboutian franc"
    },
    {
        "name": "Dominica",
        "capital": "Roseau",
        "languages": [
            "English"
        ],
        "population": 71293,
        "flag": "https://restcountries.eu/data/dma.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Dominican Republic",
        "capital": "Santo Domingo",
        "languages": [
            "Spanish"
        ],
        "population": 10075045,
        "flag": "https://restcountries.eu/data/dom.svg",
        "currency": "Dominican peso"
    },
    {
        "name": "Ecuador",
        "capital": "Quito",
        "languages": [
            "Spanish"
        ],
        "population": 16545799,
        "flag": "https://restcountries.eu/data/ecu.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "languages": [
            "Arabic"
        ],
        "population": 91290000,
        "flag": "https://restcountries.eu/data/egy.svg",
        "currency": "Egyptian pound"
    },
    {
        "name": "El Salvador",
        "capital": "San Salvador",
        "languages": [
            "Spanish"
        ],
        "population": 6520675,
        "flag": "https://restcountries.eu/data/slv.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Equatorial Guinea",
        "capital": "Malabo",
        "languages": [
            "Spanish",
            "French"
        ],
        "population": 1222442,
        "flag": "https://restcountries.eu/data/gnq.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Eritrea",
        "capital": "Asmara",
        "languages": [
            "Tigrinya",
            "Arabic",
            "English"
        ],
        "population": 5352000,
        "flag": "https://restcountries.eu/data/eri.svg",
        "currency": "Eritrean nakfa"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": [
            "Estonian"
        ],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "languages": [
            "Amharic"
        ],
        "population": 92206005,
        "flag": "https://restcountries.eu/data/eth.svg",
        "currency": "Ethiopian birr"
    },
     {
        "name": "Falkland Islands (Malvinas)",
        "capital": "Stanley",
        "languages": [
            "English"
        ],
        "population": 2563,
        "flag": "https://restcountries.eu/data/flk.svg",
        "currency": "Falkland Islands pound"
    },
    {
        "name": "Faroe Islands",
        "capital": "Tórshavn",
        "languages": [
            "Faroese"
        ],
        "population": 49376,
        "flag": "https://restcountries.eu/data/fro.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Fiji",
        "capital": "Suva",
        "languages": [
            "English",
            "Fijian",
            "Hindi",
            "Urdu"
        ],
        "population": 867000,
        "flag": "https://restcountries.eu/data/fji.svg",
        "currency": "Fijian dollar"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": [
            "Finnish",
            "Swedish"
        ],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "France",
        "capital": "Paris",
        "languages": [
            "French"
        ],
        "population": 66710000,
        "flag": "https://restcountries.eu/data/fra.svg",
        "currency": "Euro"
    },
    {
        "name": "French Guiana",
        "capital": "Cayenne",
        "languages": [
            "French"
        ],
        "population": 254541,
        "flag": "https://restcountries.eu/data/guf.svg",
        "currency": "Euro"
    },
    {
        "name": "French Polynesia",
        "capital": "Papeetē",
        "languages": [
            "French"
        ],
        "population": 271800,
        "flag": "https://restcountries.eu/data/pyf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "French Southern Territories",
        "capital": "Port-aux-Français",
        "languages": [
            "French"
        ],
        "population": 140,
        "flag": "https://restcountries.eu/data/atf.svg",
        "currency": "Euro"
    },
    {
        "name": "Gabon",
        "capital": "Libreville",
        "languages": [
            "French"
        ],
        "population": 1802278,
        "flag": "https://restcountries.eu/data/gab.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Gambia",
        "capital": "Banjul",
        "languages": [
            "English"
        ],
        "population": 1882450,
        "flag": "https://restcountries.eu/data/gmb.svg",
        "currency": "Gambian dalasi"
    },
    {
        "name": "Georgia",
        "capital": "Tbilisi",
        "languages": [
            "Georgian"
        ],
        "population": 3720400,
        "flag": "https://restcountries.eu/data/geo.svg",
        "currency": "Georgian Lari"
    },
    {
        "name": "Germany",
        "capital": "Berlin",
        "languages": [
            "German"
        ],
        "population": 81770900,
        "flag": "https://restcountries.eu/data/deu.svg",
        "currency": "Euro"
    },
    {
        "name": "Ghana",
        "capital": "Accra",
        "languages": [
            "English"
        ],
        "population": 27670174,
        "flag": "https://restcountries.eu/data/gha.svg",
        "currency": "Ghanaian cedi"
    },
    {
        "name": "Gibraltar",
        "capital": "Gibraltar",
        "languages": [
            "English"
        ],
        "population": 33140,
        "flag": "https://restcountries.eu/data/gib.svg",
        "currency": "Gibraltar pound"
    },
    {
        "name": "Greece",
        "capital": "Athens",
        "languages": [
            "Greek (modern)"
        ],
        "population": 10858018,
        "flag": "https://restcountries.eu/data/grc.svg",
        "currency": "Euro"
    },
    {
        "name": "Greenland",
        "capital": "Nuuk",
        "languages": [
            "Kalaallisut"
        ],
        "population": 55847,
        "flag": "https://restcountries.eu/data/grl.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Grenada",
        "capital": "St. George's",
        "languages": [
            "English"
        ],
        "population": 103328,
        "flag": "https://restcountries.eu/data/grd.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Guadeloupe",
        "capital": "Basse-Terre",
        "languages": [
            "French"
        ],
        "population": 400132,
        "flag": "https://restcountries.eu/data/glp.svg",
        "currency": "Euro"
    },
    {
        "name": "Guam",
        "capital": "Hagåtña",
        "languages": [
            "English",
            "Chamorro",
            "Spanish"
        ],
        "population": 184200,
        "flag": "https://restcountries.eu/data/gum.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "languages": [
            "Spanish"
        ],
        "population": 16176133,
        "flag": "https://restcountries.eu/data/gtm.svg",
        "currency": "Guatemalan quetzal"
    },
    {
        "name": "Guernsey",
        "capital": "St. Peter Port",
        "languages": [
            "English",
            "French"
        ],
        "population": 62999,
        "flag": "https://restcountries.eu/data/ggy.svg",
        "currency": "British pound"
    },
    {
        "name": "Guinea",
        "capital": "Conakry",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 12947000,
        "flag": "https://restcountries.eu/data/gin.svg",
        "currency": "Guinean franc"
    },
    {
        "name": "Guinea-Bissau",
        "capital": "Bissau",
        "languages": [
            "Portuguese"
        ],
        "population": 1547777,
        "flag": "https://restcountries.eu/data/gnb.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Guyana",
        "capital": "Georgetown",
        "languages": [
            "English"
        ],
        "population": 746900,
        "flag": "https://restcountries.eu/data/guy.svg",
        "currency": "Guyanese dollar"
    },
    {
        "name": "Haiti",
        "capital": "Port-au-Prince",
        "languages": [
            "French",
            "Haitian"
        ],
        "population": 11078033,
        "flag": "https://restcountries.eu/data/hti.svg",
        "currency": "Haitian gourde"
    },
    {
        "name": "Heard Island and McDonald Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/hmd.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Holy See",
        "capital": "Rome",
        "languages": [
            "Latin",
            "Italian",
            "French",
            "German"
        ],
        "population": 451,
        "flag": "https://restcountries.eu/data/vat.svg",
        "currency": "Euro"
    },
    {
        "name": "Honduras",
        "capital": "Tegucigalpa",
        "languages": [
            "Spanish"
        ],
        "population": 8576532,
        "flag": "https://restcountries.eu/data/hnd.svg",
        "currency": "Honduran lempira"
    },
    {
        "name": "Hong Kong",
        "capital": "City of Victoria",
        "languages": [
            "English",
            "Chinese"
        ],
        "population": 7324300,
        "flag": "https://restcountries.eu/data/hkg.svg",
        "currency": "Hong Kong dollar"
    },
    {
        "name": "Hungary",
        "capital": "Budapest",
        "languages": [
            "Hungarian"
        ],
        "population": 9823000,
        "flag": "https://restcountries.eu/data/hun.svg",
        "currency": "Hungarian forint"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": [
            "Icelandic"
        ],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": [
            "Hindi",
            "English"
        ],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "languages": [
            "Indonesian"
        ],
        "population": 258705000,
        "flag": "https://restcountries.eu/data/idn.svg",
        "currency": "Indonesian rupiah"
    },
    {
        "name": "Côte d'Ivoire",
        "capital": "Yamoussoukro",
        "languages": [
            "French"
        ],
        "population": 22671331,
        "flag": "https://restcountries.eu/data/civ.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Iran (Islamic Republic of)",
        "capital": "Tehran",
        "languages": [
            "Persian (Farsi)"
        ],
        "population": 79369900,
        "flag": "https://restcountries.eu/data/irn.svg",
        "currency": "Iranian rial"
    },
    {
        "name": "Iraq",
        "capital": "Baghdad",
        "languages": [
            "Arabic",
            "Kurdish"
        ],
        "population": 37883543,
        "flag": "https://restcountries.eu/data/irq.svg",
        "currency": "Iraqi dinar"
    },
    {
        "name": "Ireland",
        "capital": "Dublin",
        "languages": [
            "Irish",
            "English"
        ],
        "population": 6378000,
        "flag": "https://restcountries.eu/data/irl.svg",
        "currency": "Euro"
    },
    {
        "name": "Isle of Man",
        "capital": "Douglas",
        "languages": [
            "English",
            "Manx"
        ],
        "population": 84497,
        "flag": "https://restcountries.eu/data/imn.svg",
        "currency": "British pound"
    },
    {
        "name": "Israel",
        "capital": "Jerusalem",
        "languages": [
            "Hebrew (modern)",
            "Arabic"
        ],
        "population": 8527400,
        "flag": "https://restcountries.eu/data/isr.svg",
        "currency": "Israeli new shekel"
    },
    {
        "name": "Italy",
        "capital": "Rome",
        "languages": [
            "Italian"
        ],
        "population": 60665551,
        "flag": "https://restcountries.eu/data/ita.svg",
        "currency": "Euro"
    },
    {
        "name": "Jamaica",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2723246,
        "flag": "https://restcountries.eu/data/jam.svg",
        "currency": "Jamaican dollar"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "languages": [
            "Japanese"
        ],
        "population": 126960000,
        "flag": "https://restcountries.eu/data/jpn.svg",
        "currency": "Japanese yen"
    },
    {
        "name": "Jersey",
        "capital": "Saint Helier",
        "languages": [
            "English",
            "French"
        ],
        "population": 100800,
        "flag": "https://restcountries.eu/data/jey.svg",
        "currency": "British pound"
    },
    {
        "name": "Jordan",
        "capital": "Amman",
        "languages": [
            "Arabic"
        ],
        "population": 9531712,
        "flag": "https://restcountries.eu/data/jor.svg",
        "currency": "Jordanian dinar"
    },
    {
        "name": "Kazakhstan",
        "capital": "Astana",
        "languages": [
            "Kazakh",
            "Russian"
        ],
        "population": 17753200,
        "flag": "https://restcountries.eu/data/kaz.svg",
        "currency": "Kazakhstani tenge"
    },
    {
        "name": "Kenya",
        "capital": "Nairobi",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 47251000,
        "flag": "https://restcountries.eu/data/ken.svg",
        "currency": "Kenyan shilling"
    },
    {
        "name": "Kiribati",
        "capital": "South Tarawa",
        "languages": [
            "English"
        ],
        "population": 113400,
        "flag": "https://restcountries.eu/data/kir.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "languages": [
            "Arabic"
        ],
        "population": 4183658,
        "flag": "https://restcountries.eu/data/kwt.svg",
        "currency": "Kuwaiti dinar"
    },
    {
        "name": "Kyrgyzstan",
        "capital": "Bishkek",
        "languages": [
            "Kyrgyz",
            "Russian"
        ],
        "population": 6047800,
        "flag": "https://restcountries.eu/data/kgz.svg",
        "currency": "Kyrgyzstani som"
    },
    {
        "name": "Lao People's Democratic Republic",
        "capital": "Vientiane",
        "languages": [
            "Lao"
        ],
        "population": 6492400,
        "flag": "https://restcountries.eu/data/lao.svg",
        "currency": "Lao kip"
    },
    {
        "name": "Latvia",
        "capital": "Riga",
        "languages": [
            "Latvian"
        ],
        "population": 1961600,
        "flag": "https://restcountries.eu/data/lva.svg",
        "currency": "Euro"
    },
    {
        "name": "Lebanon",
        "capital": "Beirut",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 5988000,
        "flag": "https://restcountries.eu/data/lbn.svg",
        "currency": "Lebanese pound"
    },
    {
        "name": "Lesotho",
        "capital": "Maseru",
        "languages": [
            "English",
            "Southern Sotho"
        ],
        "population": 1894194,
        "flag": "https://restcountries.eu/data/lso.svg",
        "currency": "Lesotho loti"
    },
    {
        "name": "Liberia",
        "capital": "Monrovia",
        "languages": [
            "English"
        ],
        "population": 4615000,
        "flag": "https://restcountries.eu/data/lbr.svg",
        "currency": "Liberian dollar"
    },
    {
        "name": "Libya",
        "capital": "Tripoli",
        "languages": [
            "Arabic"
        ],
        "population": 6385000,
        "flag": "https://restcountries.eu/data/lby.svg",
        "currency": "Libyan dinar"
    },
    {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "languages": [
            "German"
        ],
        "population": 37623,
        "flag": "https://restcountries.eu/data/lie.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Lithuania",
        "capital": "Vilnius",
        "languages": [
            "Lithuanian"
        ],
        "population": 2872294,
        "flag": "https://restcountries.eu/data/ltu.svg",
        "currency": "Euro"
    },
    {
        "name": "Luxembourg",
        "capital": "Luxembourg",
        "languages": [
            "French",
            "German",
            "Luxembourgish"
        ],
        "population": 576200,
        "flag": "https://restcountries.eu/data/lux.svg",
        "currency": "Euro"
    }
    
]

def most_spoken_languages(countries):
    languages_in_countries =[]
    for country in countries:
        languages_in_countries.extend(country["languages"])
    
    language_count = dict((language, languages_in_countries.count(language)) for language in languages_in_countries)
    languages_count_list = list(language_count.items())
    languages_sorted_by_count = sorted(languages_count_list, key=lambda x: x[1], reverse=True)
    top_10_languages=[]
    for language in languages_sorted_by_count[0:10]:
        top_10_languages.append(language[0])  
    return top_10_languages    
           
print(most_spoken_languages(countries))

# 6. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries,top):
    country_population = dict((country["name"],country["population"] ) for country in countries)
    country_population_list= list(country_population.items())
    countries_sorted_by_population = sorted(country_population_list, key=lambda x: x[1], reverse=True)
    most_populated_countries=[]
    for item in countries_sorted_by_population[:top]:
        most_populated_countries.append(item[0])
    return most_populated_countries

print(most_populated_countries(countries,10))
    



   