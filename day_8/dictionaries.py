#1.Create an empty dictionary called dog
dog = {}
#2.Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Ruby'
dog['color'] = 'Black'
dog['breed'] = 'Boerbel'
dog['legs'] = 4
dog['age'] = 3

print(dog)

#3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Dudley'
student['last_name'] = 'Chege'
student['gender'] = 'Male'
student['age'] = 21
student['marital status'] = 'Single'
student['skills'] = ['Software Engineer','Data analyst','Football analyst']
student['country'] = 'Kenya'
student['city'] = 'Nairobi'
student['address'] = {
    'street' : 'Baraka Road',
    'zipcode' : '15509'
}


print(student)

#4.Get the length of the student dictionary

print(len(student))

#5.Get the value of skills and check the data type, it should be a list
print(len(student['skills']))
print(type(student['skills']))

#6.Modify the skills values by adding one or two skills
student['skills'].append('Vocalist')
student['skills'].append('Chess-Boy')
print(student['skills'])

#7.Get the dictionary keys as a list
keys = student.keys()
print(keys)

#8.Get the dictionary values as a list
values = student.values()
print(values)

#9.Change the dictionary to a list of tuples using items() method
print(student.items())

#10.Delete one of the items in the dictionary
del student['marital status']
print(student)

#11.Delete one of the dictionaries
del dog
print(dog)