
# numbers =(1, 2, 3)
# #numbers.count(self, 3)
# numbers[0] = 10


# # unpacking.py
# coordinates =(1,2,3)
# x = coordinates[1]
# y = coordinates[2]
# z = coordinates[0]

# # x,y,z = coordinates
# # this is same as the above three lines
# print(x)

#Dictionaries
# Customer = {
#     "Name": "haha",
# "Email": "asdf@gmail.com",
# "Age" : 30,  
# "is_verified": True
# }
# Customer["Name"]="jojo"
# print(Customer.get("birthdate", "Jan 1 2001"))

#

# Phone = input("Phone: ")
# digit_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }

# Output = " "

# for ch in Phone:
#     Output  += digit_mapping.get(ch, "!") + " "
# print(Output)

#_____________

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)" : "😊",
#     ";)" : "😉",
#     ":(" : "☹️",
#     "XD" : "😆",
#     ":P" : "😛",
#     ";P" : "😜"
#     }

# output = " "
# for w in words:
#    output += emojis.get(w, w)  + " "

# print(output)
# parameters and arguments
#____

# 
# #_______  return statement

# def square(number):
#     return number * number

# result = square(3)
# print(result)


# # by default all the functions erturn null
# make a function using def


# # by default all the functions erturn null
#exception ahndling
# try:
#     age = int(input('Age: '))
#     income = 2000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age can't be Zero")
# except ValueError:
#     print('Invalid vaalluuee')

# print("Ocean is blue")

# classes ; conditions

# #Numbers Strings, 
# numbers = [1,2,3]
# # naming convention for class camelcase generally and smallcase for other things;

# class Point:

#     def __init__(sef,x,y):
#         sef.x = x
#         sef.y = y

#     def move(sef):
#         print("move")

#     def draw(sef):
#         print("draw")


# p1 = Point(3,2)
# # p1.x=10
# # p1.y=20
# print(p1.x)
# print(p1)
# p1.draw()

#constructors
# inheritance
# class Mammal:
#     def walk(self):
#         print("walk")

# class Dog(Mammal):
#     def Bark(self):
#         print("Bark !! Bark!!")

# class Cat(Mammal): 
#     pass


# d1 = Dog()

# # using module converter

# import converters
# from converters import lbs_to_kg as k

# print(k(100))

# print(converters.kg_to_lbs(55))

# import ecommerce
# from utils import find_max as f


# ns = [11,2,4,2,3]
# # mm = utils.find_max(ns)
# m = f(ns)
# print(m)
# # max is a predenined function / method
# # it was giving the output as None as nothing was returnoing from find_max function from utils to object m  

# using refractor

# # packages
# import ecommerce
# from ecommerce import shopping
# from ecommerce.shopping import calc_shipping as s

# # calc_shipping()
# s()
# #ecommerce.shopping.calc_shipping()

# python module index --> python.org
# 
# files and directories
#
# from importlib.resources import path
# from pathlib import Path
 # absolute path 
 # 
 # # relative path

 #p.mkdir, rmdir, glob, empty, .....
