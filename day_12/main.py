# import module
# print(module.generate_full_name('Dudley','Chege'))


# from module import generate_full_name,sum_two_nums,person,gravity
# print(generate_full_name('Dudley','Chege'))
# print(sum_two_nums(1,9))
# mass = 100 
# weight = mass * gravity
# print(weight)
# print(person['firstname'])

##Import Built-in Modules
#OS Module

# import os
# #Creating a directory
# os.mkdir('directory_name')
# #Changing the current directory
# os.chdir('path')
# #Getting current working directory
# os.getcwd()
# #Removing directory
# os.rmdir()


##Sys Module
#The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
# import sys

# # print('Welcome  {}. Enjoy {} challenge!'.format (sys.argv[1], sys.argv[2]))

# # to exit sys
# sys.exit()
# # To know the largest integer variable it takes
# sys.maxsize
# # To know environment path
# sys.path
# # To know the version of python you are using
# print(sys.version)

##Statistics Module
#The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
# from statistics import * # importing all the statistics modules
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))       # ~22.9
# print(median(ages))     # 23
# print(mode(ages))       # 20
# print(stdev(ages))      # ~2.3

# ##Math Module
# import math
# print(math.pi)           # 3.141592653589793, pi constant
# print(math.sqrt(2))      # 1.4142135623730951, square root
# print(math.pow(2, 3))    # 8.0, exponential function
# print(math.floor(9.81))  # 9, rounding to the lowest
# print(math.ceil(9.81))   # 10, rounding to the highest
# print(math.log10(100))   # 2, logarithm with 10 as base

# #But if we want to import all the function in math module we can use * .

# from math import *
# print(pi)                  # 3.141592653589793, pi constant
# print(sqrt(2))             # 1.4142135623730951, square root
# print(pow(2, 3))           # 8.0, exponential
# print(floor(9.81))         # 9, rounding to the lowest
# print(ceil(9.81))          # 10, rounding to the highest
# print(math.log10(100))     # 2

#String Module
#A string module is a useful module for many purposes. The example below shows some use of the string module.
#import string
#print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#print(string.digits)        # 0123456789
#print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

##Random Module
import random
import string
# print(random())
# print(randint(5,20))

##Exercises : Level 1
##1.Write a function which generates a six digit/character random_user_id.
# def random_user_id():
#     randomSource = string.ascii_letters + string.digits 
#     password = random.sample(randomSource, 6)
#     password += random.sample(string.ascii_lowercase,3)
#     password += random.choice(string.digits)
    
#     passwordList = list(password)
#     random.SystemRandom().shuffle(passwordList)
#     password = ''.join(passwordList)
#     return password

# print(random_user_id())

import random
import string

def random_user_id():
    randomSource = string.ascii_letters + string.digits
    user_id = random.sample(randomSource, 6)

    random.shuffle(user_id)

    return ''.join(user_id)

print(random_user_id())


#2.Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    randomSource = string.ascii_letters + string.digits
    
    number_of_ids = input("Enter the number of characters")
    number_of_characters = input("Enter the number of ids")
    
     
    
    
    