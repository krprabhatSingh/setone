"""flow control describes the order in which statements will be executed at runtime"""
"""Conditional Statement"""
""" 1. If"""
"""Program 1"""
# name = input("Enter name:")
# if name == "prabhat":
#     print("Hello prabhat good morning")
# print("Hello", name, "how are you ?")


"""Program 2"""
"""if-else"""
"""if condition is true then Action-1 will be executed otherwise Action-2 will be executed"""

# name = input("Enter name")
# if name == 'prabhat':
#     print("Hello",name,"how are you")
# else:
#     print("Hello guest", name, "where you come from ??")
# print("How may i help you??")


"""3. If-elif-else"""
"""Program 3"""
# brand = input("Enter your favourite Brand:")
# if brand == 'RC':
#     print("It is childrens brand")
# elif brand == 'KF':
#     print("it is not that much kick")
# elif brand == 'FO':
#     print("Buy one get one free")
# else:
#     print("Other brands are not recommended")

"""There is no switch statement in python"""


"""Program 4"""
"""Write a program to find biggest of given 2 number from the command prompt: """

# n1 = int(input("Enter first number"))
# n2 = int(input("Enter Second number"))
# if n1 == n2:
#     print("Both number", n1, "and", n2, "are equal" )
# elif n1 > n2:
#     print("Number", n1, "is greater")
# else:
#     print("Number", n2, "is greater")

"""Program 5"""
"""WAP  to find biggest of given 3 numbers from the command prompt"""

# n1 = int(input("Enter first number"))
# n2 = int(input("Enter Second number"))
# n3 = int(input("Enter Third number"))
# if n1 > n2 > n3:
#     print("Biggest number is ", n1)
# elif n2 > n1 > n3:
#     print("Biggest number is", n2)
# else:
#     print("biggest number is", n3)

"""Program 6"""
"""" WAP to check whether the given number is in between 1 and 100"""
# n = int(input("Enter number:"))
# if n >= 1 and n <= 10:
#     print("The number", n, "is in between 1 to 10")
# else:
#     print("The number", n, "is not in between 1 to 10")

"""Program 7"""
"""WAP to take a single digit number from the key board and print is value in english word"""

alphabet = int(input("Enter an alphabet"))
if alphabet == 0:
    print("Zero")
elif alphabet == 1:
    print("One")
elif alphabet == 2:
    print("Two")
elif alphabet == 3:
    print("Three")
elif alphabet == 4:
    print("Four")
elif alphabet == 5:
    print("Five")
elif alphabet == 6:
    print("Six")
elif alphabet == 7:
    print("Seven")
elif alphabet == 8:
    print("Eight")
elif alphabet == 9:
    print("Nine")
else:
    print("enter alphabet is not valid")