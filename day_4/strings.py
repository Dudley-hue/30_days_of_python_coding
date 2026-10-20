# ### Strings
# letter = 'P'
# print(letter)
# print(len(letter))
# greeting = 'Hello, World!'
# print(greeting)
# print(len(greeting))


# ### Multiline Strings
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)


###String Concatenation
# first_name = 'Dudley'
# last_name = 'Chege'
# space = ' '
# full_name = first_name + space + last_name
# print(full_name)

# print(len(first_name))
# print(len(last_name))
# print(len(first_name) > len(last_name))
# print(len(full_name))


###Escape Sequences in Strings
#\n:new line
#\t:Tab means(8 spaces)
#\\:Back slash
#\':Single Quote (')
#\":Double quote (")


# print('I hope everyone is enjoying the Python challenge.\nAre you ?')#line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backlash symbol (\\)') #To write a backlash
# print('In every programming language it starts with \"Hello, World!"')



###String Formatting
# %s-String
# %d-Integers
# %f-Floating point numbers
#"%.number of digitsf" - Floating point numbers with fixed precision 


#Strings only
# first_name = 'Dudley'
# last_name = 'Chege'
# language = 'Python'
# formatted_string = 'I am %s %s.I teach %s'%(first_name,last_name,language)
# print(formatted_string)

#Strings and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
# print(formatted_string)


# python_libraries = ['Django', 'Flask', 'NumPy','Matplotlib','Pandas']
# formatted_string = 'The following are python libraries:%s'%(python_libraries)
# print(formatted_string)


### New Style String Formatting
# first_name = 'Dudley'
# last_name = 'Chege'
# language = 'Python'
# formatted_string = 'I am {} {}.I teach {}'.format(first_name,last_name,language)
# print(formatted_string)


# a = 4
# b = 3

# print('{} + {} = {}'.format(a,b, a + b))
# print('{} - {} = {}'.format(a,b, a - b))
# print('{} * {} = {}'.format(a,b, a * b))
# print('{} / {} = {:.2f}'.format(a,b, a / b))
# print('{} % {} = {}'.format(a,b, a % b))
# print('{} // {} = {}'.format(a,b, a // b))
# print('{} ** {} = {}'.format(a,b, a ** b))



# ##String Interpolation / f-Strings (Python 3.6+)
# a = 4
# b = 3

# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')


# #Unpacking Characters 
# language = 'Python'
# a,b,c,d,e,f = language
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n


# #Accessing Characters in Strings by Index
# language = 'Python'
# first_letter = language[0]
# print(first_letter) # P
# second_letter = language[1]
# print(second_letter) # y
# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter) # n


# #Slicing Python Strings
# language = 'Python'
# first_three = language[0:3]
# print(first_three)
# last_three = language[3:6]
# print(last_three)

# #Another way
# last_three = language[-3:]
# print(last_three)
# last_three = language[3:]
# print(last_three)

# #Reversing a String
# greeting = 'Hello, World!'
# print(greeting[::-1])

#Skipping Characters While Slicing
# language = 'Python'
# pto = language[0:6:2]
# print(pto)


# #String Methods
# #Capitalize(): Converts the first character of the string to capital letter
# challenge = 'thirty days of python'
# print(challenge.capitalize())

# #Count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
# challenge = 'thirty days of python'
# print(challenge.count('y'))
# print(challenge.count('y', 7 , 14))
# print(challenge.count('th'))

# #endswith(): Checks if a string ends with a specified ending
# challenge = 'thirty days of python'
# print(challenge.endswith('on'))
# print(challenge.endswith('tion'))

# #expandtabs():Replaces tab character with spaces,default tab size is 8 .It takes tab size argument
# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())
# print(challenge.expandtabs(10))

# #find():Returns the index of the first occurrence of a substring,if not found returns -1
# challenge = 'thirty days of python'
# print(challenge.find('y'))
# print(challenge.find('th'))

# #rfind():Returns the index of the last occurrence of a substring,if not found returns -1
# challenge = 'thirty days of python'
# print(challenge.rfind('y'))
# print(challenge.rfind('th'))

# #isalnum(): Checks alphanumeric character
# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True

# challenge = '30DaysPython'
# print(challenge.isalnum()) # True

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False, space is not an alphanumeric character

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum()) # Falsechallenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True

# challenge = '30DaysPython'
# print(challenge.isalnum()) # True

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False, space is not an alphanumeric character

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum()) # False




###Exercise - Day 4
#1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
combined = a + space + b + space + c + space + d
print(combined)

#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = 'Coding'
b = 'For'
c = 'All'
space = ' '
combined = a + space + b + space + c
print(combined)

#3.Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'


#4.Print the variable company using print().
print(company)

#5.Print the length of the company string using len() method and print().
print(len(company))

#6.Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7.Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize()) #capitalize
print(company.title()) #title
print(company.swapcase()) #Swapcase

# #9.Cut(slice) out the first word of Coding For All string.
# print(company.strip('Coding'))

#10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

#11.Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#12.Change "Python for Everyone" to "Python for All" using the replace method or other methods.
code = 'Python for Everyone'
print(code.replace('Python for Everyone', 'Python for All'))

#13.Split the string 'Coding For All' using space as the separator (split()) .
print(company.split( ))

#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = 'Facebook , Google, Microsoft , Apple ,IBM ,Oracle ,Amazon '
print(tech_companies.split(',  '))

#15.What is the character at index 0 in the string Coding For All.
print(company[0])

#16.What is the last index of the string Coding For All.
print(company[-1])

#17.What character is at index 10 in "Coding For All" string.
print(company[10])

#18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
coding = 'Python For Everyone'
print(coding[0:6:2])

#19.Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0:6:2])

#20.Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21.Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rindex('l'))

#23.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjuction'
print(sentence.index('because'))

#24.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.strip('because because because'))

#26.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#28.Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#29.Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
refactor = '  Coding For All   '
print(refactor.strip(' '))

#31.Which one of the following variables return True when we use the method isidentifier():
a = '30DaysOfPython'
b = 'thirty_days_of_python'

print(a.isidentifier(), b.isidentifier())
#32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '-'.join(libraries)
print(result)

#33.Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge .\nI just wonder what is next.')

#34.Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Dudley\t21\tKenya\tKitengela')

#35.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formatted_string = 'The area of a circle is radius %d is %.2f' %(radius,area)
print(formatted_string)

#36.Make the following using string formatting methods:
a = 8
b = 6

print('{} + {} = {}'.format(a,b , a + b))
print('{} - {} = {}'.format(a,b , a - b))
print('{} * {} = {}'.format(a,b , a * b))
print('{} / {} = {}'.format(a,b , a / b))
print('{} % {} = {}'.format(a,b , a % b))
print('{} // {} = {}'.format(a,b , a // b))
print('{} ** {} = {}'.format(a,b , a ** b))


