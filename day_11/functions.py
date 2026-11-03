###Declaring and Calling a Function

#syntax
#Declaring a function
# def function_name():
#     codes
#     codes
# #Calling a function
# function_name()

##Function without Parameters
# def generate_full_name():
#     first_name = 'Dudley'
#     last_name = 'Chege'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# generate_full_name()


# def add_two_numbers():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()


#Function Returning a Value - Part 1
#Function return values using the return statement.if a function has no return statement,it returns None.
# def generate_full_name():
#     first_name = 'Antony'
#     last_name = 'Kimani'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(generate_full_name())
    

# def add_two_numbers():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# print(add_two_numbers())

#Function with Paremeters
#In a function we can pass different data types(number,string,boolean,list,tuple,dictionary or set)as parameters

#Single Parameter:If our function takes a paremeter we should call our function with an argument
#syntax
#Declaring a function
# def function_name(paremeter):
#     codes
#     codes
# #Calling  function
# print(function_name(argument))

# def greetings(name):
#     message = name + ', Welcome to Python for Everyone!'
#     return message
# print(greetings('Dudley'))

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))

# def square_number(x):
#     return x * x
# print (square_number(2))

# def area_of_circle(r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))

# def sum_of_numbers(n):
#     total = 0
#     for i in range (n + 1):
#         total += i
#     return total
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))

##Two Parameters
# def generate_full_name (first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print('Full Name: ', generate_full_name('Dudley','Chege'))


# def sum_two_numbers(num_one,num_two):
#     sum = num_one + num_two
#     return sum
# print('Sum of two numbers: ', sum_two_numbers(1, 9))


# def calculate_age (current_year, birth_year):
#     age = current_year - birth_year
#     return age

# print('Age: ', calculate_age(2026, 2004))

# def weight_of_object (mass,gravity):
#     weight = str(mass * gravity)+ ' N'
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

##Passing Arguments with Key and Value
#syntax
#Declaring a function
# def function_name(para1,para2):
#     codes
#     codes
# #Calling function
# print(function_name(para1= ' John', para2= 'Doe'))

#Example
# def print_fullname(firstname,lastname):
#     space = ' '
#     full_name = firstname + space + lastname
#     print(full_name)
# print_fullname(firstname= ' Dudley' , lastname= 'Chege')

# def add_two_numbers(num1,num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(num2= 3,num1= 2))


##Function Returning a Value- Part 2
#If we do not return a value with a function, then our function is returning None by default.

# def print_name(firstname):
#     return firstname
# print(print_name('Dudley'))

# def print_full_name(firstname,lastname):
#     space = ' '
#     full_name = firstname + space + lastname
#     return full_name
# print(print_full_name(firstname= 'Dudley',lastname='Chege'))


# def calculate_age (current_year,birth_year):
#     age = current_year - birth_year
#     return age
# print('Age:', calculate_age(2026, 2004))

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False
# print(is_even(10))
# print(is_even(7))


# def find_even_numbers(n):
#     evens = []
#     for i in range (n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(find_even_numbers(10))


##Exercises : Day 11
#1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# def add_two_numbers(num_one,num_two):
#     total = num_one + num_two
#     return total
# print(add_two_numbers(num_one= 1 , num_two=3))


# #2.Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

# def area_of_circle(r):
#     area = 3.14 * r ** 2
#     return area
# print(area_of_circle(5))    


#3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*args):
#    total = 0
   
#    for num in args:
#        if not isinstance(num,(int,float)):
#            return "All arguments must be numbers."
       
#        total += num
       
#    return total

# print(add_all_nums(10,20,30,40))


# #4.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# print(convert_celsius_to_fahrenheit(35))


#5.Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(season):
    
 if season in ('September','October','November'):
    return('Autumn')
 elif season in ('December','January','February'):
    return('Winter')
 elif season in ('March', 'April','May'):
    return('Spring')
 elif season in ('June','July','August'):
    return('Summer')
 else:
    return('The month you enter is not valid')

season = input("Enter the month : ")

print(check_season(season))    