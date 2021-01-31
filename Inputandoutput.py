
# Every input value is treated as a String

# print(type(input("Enter values")))
# print(type(input("enter values")))
# print(type(input("Enter values")))

# WAP to read 2 numbers from the keyboard and print sum.

# Program 1
# Method 1 :
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# c = a + b
# print("The sum of", a , "and", b, "is", c)
# print("The sum is", a+b)

# Method 2 :

# print("The sum is", int(input("Enter first number:")) + int(input("Enter second number:")))


# Program 2 : wap to read employeed data from the keyboard and print the data.
#
# eno = int(input("Enter Employee No:"))
# ename = input("Enter Employee Name:")
# esal = float(input("Enter employee salary:"))
# married = bool(input("Employee Married? [True|False]"))
#
# print("Employee Number is", eno)
# print("Employee Name is ", ename)
# print("Employee salary is", esal)
# print("Employee married status is", married)

"""Program 3"""
""" Read mutliple values from the keyboard in a single line"""

# a,b,c = [int(x) for x in input("Enter 3 numbers").split()]
# print("product is: ", a*b*c)

# x, y, z = [int(i) for i in input("Enter 3 values").split(',')]
# print("product is : ", x * y * z)

""" Program 4"""
""" WAP to read 3 float numbers from the keyboard with , seperator and print their sum """

# p, q, r = [float(i) for i in input("Enter the 3 values").split(',')]
# print("The sum is", p+q+r)

""" eval() """

""" eval function take a string and evaluate the result"""

# x = eval("10+20+30")
# print(x)


# x = eval(input("Enter expression"))
# print(type(x))

""" Arg is not an array it is a list , it is available is sys module."""