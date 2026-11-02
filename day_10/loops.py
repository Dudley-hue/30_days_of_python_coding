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

for number in range(1,11):
    print(f"{number} * {number} = {number**2}")
    
#6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


# languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for language in languages:
#     print(language)

# #7. Use for loop to iterate from 0 to 100 and print only even numbers
# for number in range(0,101):
#     if number % 2 == 0:
#         print(number)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers        
for number in range(0,101):
    if number % 2 != 0:
        print(number)