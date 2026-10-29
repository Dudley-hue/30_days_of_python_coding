##Exercises : Day 9
# #1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# age = int(input("Enter your age: "))

# if age >= 18:
#     print('You are old enough to learn to drive')
# else:
#      print(f"You need {18 - age} years to learn to drive")
     

#2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# my_age = int(input("Enter your age: "))
# your_age = int(input("Enter your age: "))

# if my_age > your_age:
#     diff = my_age - your_age
#     if diff == 1:
#         print(f"You are 1 year older than me.")
#     else:
#         print(f"You are {diff} years older than me.")
# elif my_age < your_age:
#     diff = your_age - my_age
#     if diff == 1:
#         print(f"I am 1 year older than you.")
#     else:
#         print(f"I am {diff} years older than you.")
# else:
#     print("We are the same age!")
    
    
#3.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# num_1 = int(input("Enter num one: "))
# num_2 = int(input("Enter num two: "))

# if num_1 > num_2 :
#     print(f'{num_1} is greater than {num_2}')
# elif num_1 < num_2:
#     print(f'{num_1} is less than {num_2}')
# else:
#     print("The numbers are equal")
    
    
###Exercises:Level 2

#1.Write a code which gives grade to students according to theirs scores:
# marks = int(input('Enter your marks : '))
# if marks > 90 :
#     print('A')
# elif marks > 80 :
#     print('B')
# elif marks > 70:
#     print('C')
# elif marks > 60 :
#     print('D')
# else:
#     print('F')
    
#2.Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# season = input('Enter the month: ')

# if season in ('September','October','November'):
#     print('Autumn')
# elif season in ('December','January','February'):
#     print('Winter')
# elif season in ('March', 'April','May'):
#     print('Spring')
# elif season in ('June','July','August'):
#     print('Summer')
# else:
#     print('The month you enter is not valid')
    

#3.Mysteries of the week

# mysteries = input('Enter the day of the week: ')

# if mysteries in ('Monday','Saturdays'):
#     print('Joyful Mysteries')
# elif mysteries in ('Tuesday','Friday'):
#     print('Sorrowful Mysteries')
# elif mysteries in ('Wednesday','Sunday'):
#     print('Glorius Mysteries')
# elif mysteries in ('Thursday'):
#     print('Luminous Mysteries')
# else:
#     print('Not a valid day')
    
    
#3.If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input("Enter the fruit: ")

# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)

###Exercises:Level 3
#1.Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1.Middle skill
if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])
    
    
#2.Has Python?
if 'skills' in person:
    print('Python' in person['skills'])
    

#3.Title
if 'skills' in person:
    if set(['JavaScript', 'React']) == set(skills):
        print('He is a front end developer')
    elif all(s in skills for s in ['Node', 'Python', 'MongoDB']):
        print('He is a backend developer')
    elif all(s in skills for s in ['React', 'Node', 'MongoDB']):
        print('He is a fullstack developer')
    else:
        print('unknown title')
        
        
# 4. Married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")