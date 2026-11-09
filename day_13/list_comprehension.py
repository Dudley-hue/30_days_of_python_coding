##List Comprehension
#List comprehension in Python is a compact way of creating a list from a sequence.
# It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

#syntax
#[expression for i in iterable if condition]

#Example:1
#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

# language = 'Python'
# lst = list(language)
# print(type(lst))
# print(lst)

# #Second way:list comprehension
# lst = [i for i in language]
# print(type(lst))
# print(lst)


# #Example : 2
# #For instance if you want to generate a list of numbers

# #Generating numbers
# numbers = [i for i in range(11)]
# print(numbers)

# #It is possible to do mathematical operations during iteration
# squares = [i * i for i in range(11)]
# print(squares)

# #It is also possible to make a list of tuples
# numbers = [(i, i * i) for i in range(11)]
# print(numbers)


# #Example:2
# #List comprehension can be combined with if expression

# even_numbers = [i for i in range(21) if i % 2 == 0]
# print(even_numbers)


# #Generating odd numbers
# odd_numbers = [i for i in range(21) if i % 2 != 0]
# print(odd_numbers)

# #Filter numbers:let's filter out positive even numbers from the list below
# numbers = [-8,-7,-3,-3,-1,0,1,3,4,5,7,6,8,10]
# positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
# print(positive_even_numbers)


# #Flattening a two dimensional array
# list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
# flattened_list = [number for row in list_of_lists for number in row]
# print(flattened_list)

# #Lambda Function
# #Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

# #Creating a Lambda Function
# #To create a lambda function we use lambda keyword followed by a parameter(s),followed by an expression.
# #syntax
# # x = lambda param1,param2,param3:param1 + param2 + param3
# # print(x(arg1,arg2,arg3))

# #Example
# #Named function
# def add_two_nums(a,b):
#     return a + b

# print(add_two_nums(2, 3))
# #Lets change the above function to a lambda function
# add_two_nums = lambda a,b: a + b
# print(add_two_nums(2,3))

# square = lambda x : x ** 2
# print(square(3))
# cube = lambda x : x ** 3
# print(cube(3))

#Lambda Function Inside Another Function
#Usinf a lambda function inside another function
# def power(x):
#     return lambda n : x ** n

# cube = power(2)(3)
# print(cube)

# two_power_of_five = power(2)(5)
# print(two_power_of_five)

##Exercises:Day 13
#1.Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i > 0]
print(positive_numbers)

#2.Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row ]
print(flattened_list)

#3.Using list comprehension create the following list of tuples:

numbers = [(i,i * i ) for i in range(5)]
print(numbers)


#4.Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [letter for row in countries for letter in row]
print (flattened_countries)

#5.Change the following list to a list of dictionaries:

print((flattened_countries))


#6.Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc = [name for row in names for name in row]
print(conc)