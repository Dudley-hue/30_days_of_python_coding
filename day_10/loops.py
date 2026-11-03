### It is used to execute a block of code repeatedly as long as a certain condition is true. The loop will continue to run until the condition becomes false.

##While loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1
    
### In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
#syntax:
# while condition:
#  code goes here
# else:
# code goes here

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print(count)
    
## The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

##Break and Continue - Part 1
# Break : we use break when we like to get out of or stop the loop
# syntax
# while condition:
#     code goes here
#     if condition:
#         break

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break
    
#The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

##Continue: With the continue statement we can skip the current iteration, and continue with the next:

# count = 0 
# while count < 5:
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count += 1

##For  loop
# syntax:
# for iterator in list:
#    code goes here

# numbers = [0, 1, 2, 3, 4,5]
# for number in numbers:
#     print(number)

#Using For loop on string

# language = 'Python'
# # for letter in language:
# #     print(letter)
    
# for i in range(len(language)):
#     print(language[i])
    

# ## using for loop in tpl
# numbers = (0, 1, 2, 3, 4,5)
# for number in numbers:
#     print(number)
    
    
# ## for loop in dictionary
# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for key in person:
#     print(key)
    
# for key, value in person.items():
#     print(key, value)
    
# #using for loop in set
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

##Break and Continue - Part 2
# Break : we use break when we like to get out of or stop the loop

# numbers = (0, 1, 2, 3, 4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         break
    
##Continue
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')


###Exercise : Day 10
##Exercises: Level 1
#1. Iterate 0 to 10 using for loop, do the same using while loop
# for i in range (0,11):
#     print(i)
    
# ##While loop
# count = 0
# while count < 11:
#     print(count)
#     count += 1
##2. Iterate 10 to 0 using for loop, do the same using while loop

# for i in range(10, -1, -1):
#     print(i)

###While loop
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# count = '#'
# for i in range(7):
#     print(count)
#     count += '#'
    
# #4. Use nested loops to create the following:
# for i in range(1,5):
#     for j in range(1,17):
#         print("#", end=" ")
#     print()

#5.Print the following pattern:

# for number in range(1,11):
#     print(f"{number} * {number} = {number**2}")
    
#6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


# languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for language in languages:
#     print(language)

# #7. Use for loop to iterate from 0 to 100 and print only even numbers
# for number in range(0,101):
#     if number % 2 == 0:
#         print(number)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers        
# for number in range(0,101):
#     if number % 2 != 0:
#         print(number)

##Practice
##While Loop

# 1.#write a while loop that prints numbers from 1 to 10
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
    
# 2.#Counting backwards from 10 to 1 using a while loop
# count = 10
# while count >= 1:
#     print(count)
#     count -= 1
    
# 3.#Write a while loop that prints the even numbers from 2 to 20
# count = 2
# while count <= 20:
#     print(count)
#     count += 2
# 4.#Use a while loop to calculate the sum of numbers from 1 to 100.
# sum = 0
# count = 1
# while count <= 100:
#     sum += count
#     count += 1
# print(f"The sum of numbers from 1 to 100 is: {sum}")

##Multiplication Table
#Ask the user to enter a number, then use a while loop to generate its multiplication table up to 12.
# number = int(input("Enter a number: "))
# count = 1
# while count <= 12:
#     product = number * count
#     print(f"{number} x {count} = {product}")
#     count += 1
    

##Create a program that keeps asking the user for a password until they enter the correct password.
# password = input("Enter the password: ")
# correct_password = "python123"
# while password != correct_password:
#     print("You have entered the wrong password")
#     password = input("Enter the password: ")
# else:
#     print("Access Granted")
    
#Exercise:Level 2
# #1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# sum = 0
# count = 1
# while count <= 100:
#     sum+= count
#     count+=1
# print(f"{sum}")

#2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# even = 0

# count = 0

# while count <= 100:
#  if even % 2 == 0:
#     even += count
#     count += 2
# print(f"The sum of all even is {even}")


number = 1
odd_sum = 0
while number <=100:
    if number % 2 != 0:
        odd_sum += number

    number += 1
print(f"The sum of all odds is {odd_sum}")