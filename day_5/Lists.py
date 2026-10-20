# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# # vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# # animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# # web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# # countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# # # Print the lists and its length
# # print('Fruits:', fruits)
# # print('Number of fruits:', len(fruits))
# # print('Vegetables:', vegetables)
# # print('Number of vegetables:', len(vegetables))
# # print('Animal products:',animal_products)
# # print('Number of animal products:', len(animal_products))
# # print('Web technologies:', web_techs)
# # print('Number of web technologies:', len(web_techs))
# # print('Countries:', countries)
# # print('Number of countries:', len(countries))

# #Accessing List items Using Positive Indexing
# first_fruit = fruits[0]
# print(first_fruit)
# second_fruit = fruits[1]
# print(second_fruit)
# last_fruit = fruits[3]
# print(last_fruit)

# #Last index
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

# #Accessing List Items Using Negative Indexing
# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[-4]
# last_fruit = fruits[-1]
# second_last = fruits[-2]
# print(first_fruit)
# print(last_fruit)
# print(second_last)

# #Unpacking List Items
# lst = ['item1','item2','item3','item4','item5']
# first_item, second_item,third_item, *rest = lst
# print(first_item)
# print(second_item)
# print(third_item)
# print(rest)

# # First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits 
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']
# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10
# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr) 
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)


#Exercises : Day 5
#Exercises: Level 1
#1.Declare an empty list
list = []

#2.Declare a list with more than 5 items
lists = ['Dudley','Eliud','Elvis','Jovanni','Elaine']

#3.Find the length of your list
print(len(lists))

#4.Get the first item, the middle item and the last item of the list

first_item,middle_item,*last_item = lists
print(first_item)
print(middle_item)
print(last_item)

#5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Dudley',21,5.8,'Single',1230-435]

#6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7.Print the list using print()

print(it_companies)

#8.Print the number of companies in the list

print(it_companies)

#9.Print the first, middle and last company

first_company,middle_company,*last_company = it_companies

print(first_company)
print(middle_company)
print(last_company)

# #10.Print the list after modifying one of the companies

# it_companies[2] = 'Nvidia'
# print(it_companies)

#11.Add an IT company to it_companies

it_companies.append('Nvidia')
print(it_companies)

#12.Insert an IT company in the middle of the companies list
# middle_company = len(it_companies) - 4
# it_companies[middle_company] = 'Tesla'
# print(it_companies)

it_companies.insert(4,'Tesla')
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[2] = 'MICROSOFT'
print(it_companies)

#14.Join the it_companies with a string '#;  '

it_companies2 = ['#; ']
it_companies3 = it_companies + it_companies2
print(it_companies3)

#15.Check if a certain company exists in the it_companies list.

does_exist = 'MICROSOFT' in it_companies
print(does_exist)

#16.Sort the list using sort() method

it_companies.sort()
print(it_companies)

#17.Reverse the list in descending order using reverse() method

print(it_companies[::-1])

#18.Slice out the first 3 companies from the list

new_company = it_companies[3:]
print(new_company)

#19.Slice out the last 3 companies from the list
old_company = it_companies[0:6]
print(old_company)

#20.Slice out the middle IT company or companies from the list

middle_company = it_companies.pop(5)
print(middle_company)
print(it_companies)

#21.Remove the first IT company from the list

it_companies.pop(0)
print(it_companies)

#22.Remove the middle IT company or companies from the list

it_companies.pop(4)
print(it_companies)

#23.Remove the last IT company from the list

it_companies.pop(5)
print(it_companies)

#24.Remove all IT companies from the list

del it_companies[0:5]
print(it_companies)

#25.Destroy the IT companies list

del it_companies
# print(it_companies)

#26.Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

print(front_end)

#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

