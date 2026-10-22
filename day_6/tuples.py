#1.Create an empty tuple
school = ()
# print(type(school))

#2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Elvis','Jovanni')
sisters = ('Elaine','Wangui')

#3.Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#4.How many siblings do you have?
print(len(siblings))

#5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ('Johnson', 'Denise')
family_members = siblings + parents
print(siblings)

###Exercises:Level 2
#1.Unpack siblings and parents from family_members
*siblings , father , mother = family_members
print(siblings)
print(father)
print(mother)

#2.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango','orange','watermelon')
vegetables = ('broccoli','cabbage')
animal_products = ('hay','thaara')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
tpl=food_stuff_lt[0:3]
print(tpl)

#5.Slice out the first three items and the last three items from food_stuff_lt list
tl = food_stuff_lt[4:7]
print(tl)

# #6.Delete the food_stuff_tp tuple completely
# del food_stuff_tp
# print(food_stuff_tp)

#7.Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
country = 'Estonia' in  nordic_countries
print(country)

#b

countries = 'Iceland' in nordic_countries
print(countries)