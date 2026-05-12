print (3+4) # performing different operations using operand 3 and 4
print (3-4)
print (3*4)
print (3/4)
print (3**4)
print (3//4)
print (3%4)
print ("My name is Yashfa") #single line comment
print ("My family name is Naveed Ch") # single line comment
print ("I am Pakistani") #single line comment
print ("""
I am not enjoying my 30 days of python too well bcoz my chachoo is a little bit strict but he is indeed a good tutor as well:)
""") # multi-line comment
print(type("ABC"))
print(type("10")) #any text in quotes is considered as string whether its alphabet or number or any text
print(type(9.9))
print(type(10))
print(type(True))
print(type(False))
print(type(3+4j))
print(type("Yashfa; Pakistan; Python"))
print(type(('Yashfa','Pakistan','Python'))) #in tuple rounded brackets () are used, tuples are unchangeable and ordered
print(type(['Yashfa','Pakistan','Python'])) #in list square brackets [] are used, lists are changeable and ordered
print(type({'Yashfa','Pakistan','Python'})) #in set curly or curved brackets {} are used, sets have unique and unduplicated value
print(type({"name":"Yashfa", "age": 21 })) #in dictionary curved brackets {} are used along with colon : to represent key and its value
#eucledean distance
import math
x1 = 5
y1 = 4
x2 = 6
y2 = 7
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)