#Exercises:Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

###Exercises:Level 1
#1.Find the length of the set it_companies
print(len(it_companies))

#2.Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#3.Insert multiple IT companies at once to the set it_companies
it_companies.update(['Whatsapp','Instagram'])
print(it_companies)

#4.Remove one of the companies from the set it_companies
it_companies.remove('Google')

#5.What is the difference between remove and discard




##Exercises:Level 2
#1.Join A and B
C = A.union(B)
sorted(C)
print(C)

#2.Find A intersection B
print(A.intersection(B))

#3.Is A subset of B
print(B.issubset(A))

#4.Are A and B disjoint sets
##Yes

#5.Join A with B and B with A
D = B.union(A)
print(C)
print(D)

#6.What is the symmetric difference between A and B
print(A.difference(B))
print(B.difference(A))

#7.Delete the sets completely
# del A
# del B

# print(A)
# print(B)

#Exercises:Level 3
#1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages = set(age)

print(len(ages))
print(len(age))