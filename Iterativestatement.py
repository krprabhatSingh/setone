""" If we want to execute a group of statements multiple times then we should go for Iterative statement"""

""" Python support two types of iterative sentence 1. For loop and 2. While loop"""

""" For loop"""
""""If we want to execute some action for every element present in some sequence (it may be string or collection) then we should go for for loop"""

"""Program 1"""
# To print character present in a given string :

# s = "Prabhat kumar"
# for x in s:
#     print(x)


"""" Program 2"""

#  To print characters present in string index wise :

# s = input("Enter characters")
# i = 0
# for x in s:
#     print("Characters a", i, "is", x)
#     i = i+1


"""Program 3 """

# To print Hello 10 times :
# for i in range(10):
#     print("hello")

"""Program 4"""
# To display odd numbers from 0 to 20
# for i in range(21):
#     if i % 2 != 0:
#         print("Odd numbers", i)

"""Program 5"""

# To display numbers from 10 to 1 in descending order

# for i in range(10, 0 , -1):
#     print("Number in descending order",i)


# To print sum of numbers present inside list:

# list = eval(input("Enter list:"))
# sum = 0
# for x in list:
#     sum = sum +x
# print("The sum=",sum)

""" While Loop"""

""" If we want to execute a group of statements iteratively until some conditions false, than we should go for while loop"""

# To print numbers from 1 to 10 by using while loop :
# x = 1
# while x<= 10:
#     print(x)
#     x = x+1


# To display the sum of first n numbers:
#
# n = int(input("Enter number:"))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i+1
# print("The sum of first",n, "number is", sum)


# WAP to prompt user to enter some name until entering Prabhat
#
# name = ""
# while name!= "prabhat":
#     name = input("Enter name")
# print("Thanks for the confirmation")


# Infinite Loop:

# i = 0
# while True:
#     i = i+1
#     print("Hello",i)


# Nested Loop :

"""Sometimes we can take a loop inside another loop, which are also known as nested loops."""
#
# for i in range(4):
#     for j in range(4):
#         print("i=",i, "j=", j)

""" WAP to display * in Right angled triangled form"""
#
# n = int(input("Enter number of rows:"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print()


"""Transefer Statement"""
"""Break"""
# We can use break statement inside loops to break loop execution based on some conditions.
#
# for i in range(10):
#     if i == 7:
#         print("Processing is enough please break the statement")
#         break
#     print("Print the values",i)

"""Continue Statement"""

""" We can use continue statement to skip current iteration and continue next iteration."""

# Program 1 :
# To print odd numbers in the range 0 to 9 :

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)