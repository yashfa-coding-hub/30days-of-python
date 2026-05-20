# Day 2 Exercise 1
# inside 30 days of python folder, a subfolder named day 2 with a file variable.py was created
# Comment generated saying its day 2 of python programming but its not executable
# Declaring a first name variable and assign a value to it
first_name = 'Yashfa'
print (first_name)
# Declaring a last name variable and assign a value to it
last_name = "Naveed"
print (last_name)
# Declaring a full name variable and assign a value to it
full_name = "Yashfa Naveed"
print (full_name)
# Declaring a country variable and assign a value to it
my_country = "PAKISTAN"
print (my_country)
# Declaring a city variable and assign a value to it
_city = "Lahore"
print (_city)
# Declaring an age variable and assign a value to it
_age = 21.4
print (_age)
# Declaring a year variable and assign a value to it
_Year_ = 2004
print (_Year_)
# Declaring a variable is_married and assign a value to it
is_married = False
print (is_married)
# Declaring a variable is_true and assign a value to it
is_true = True
print (is_true)
# Declaring a variable is_light_on and assign a value to it
is_light_on = True
print (is_light_on)
# Declaring multiple variable on one line
_Name , _Age , am_i_girl = "Yashfa", 21.4 , True
print (_Name , _Age , am_i_girl)
_complex , float_ , integer_ , bool_ean , st_ring , = 2 + 3j , 2.9999 , 38 , False , "I Love Pakistan"
print(_complex , float_ , integer_ , bool_ean , st_ring)

# Day 2 Exercise 2
# Checking the data type of all your variables using type() built-in function
print(type(_complex))
print(type(float_))
print(type(integer_))
print(type(bool_ean))
print(type(st_ring))
# Using the len() built-in function, finding the length of your first name
len("Yashfa")
print(len("Yashfa"))
len("Naveed")
print(len("Naveed"))
# Comparing the length of my first name and last name
first_name = "Yashfa"
last_name = "Naveed"
print(len(first_name)>len(last_name))
print(len(first_name)<len(last_name))
print(len(first_name)==len(last_name))
# Declaring 5 as num_one and 4 as num_two
num_one = 5 
num_two = 4
print (num_one)
print (num_two)
# Adding num_one and num_two and assigning the value to a variable total
total_num = num_one + num_two
print(total_num)
# Subtracting num_two from num_one and assigning the value to a variable diff
diff_of_both_num = num_one - num_two
print (diff_of_both_num)
# Multiplying num_two and num_one and assigning the value to a variable product
product_num = num_one * num_two
print(product_num)
# Dividing num_one by num_two and assiging the value to a variable division
division = num_one / num_two
print(division)
# Using modulus division to find num_two divided by num_one and assigning the value to a variable remainder
remainder = num_one % num_two
print (remainder)
# Calculating num_one to the power of num_two and assigning the value to a variable exp
exp = num_one ** num_two
print (exp)
# Finding floor division of num_one by num_two and assigning the value to a variable floor_division
floor_division = num_one // num_two
print (floor_division)
"""
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area 
"""
radius = 30
pi = 3.14
area_of_circle = pi * radius ** 2
print (area_of_circle)
diameter_of_circle = 2 * radius
circum_of_circle = diameter_of_circle * pi
print (circum_of_circle)
pi = 3.14
radius = float(input("Enter radius: "))
circumference = 2 * pi * radius
print("Circumference of circle is:", circumference)
"""
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
"""
name = input("Enter Name:")
print (name)
last_name = input ("Enter Last Name:")
print (last_name)
country = input ("Enter Country:")
print (country)
age = input ("Enter Age:")
print (age)
# Running help('keywords') in Python shell or in my file to check for the Python reserved words or keywords
help ('keywords')

# 🎉 CONGRATULATIONS ! 🎉 Day 2 Ended Successfully 
print ("🎉 CONGRATULATIONS ! 🎉")