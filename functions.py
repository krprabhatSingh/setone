""" Function"""
"""" If a group of statements is repeatedly required then it is not recommended to write these statements 
    everytime seprately."""
""" we have to define these statements as a single unit and we can call that unit any number of times based on our requirement without rewriting"""
"""This unit nothing called function"""

""" The main advantage of functions is code reusability"""
"""Note: In other languages functions are know as methods, procedures, subroutines etc"""

""" 1. built in functions"""
""" 2. User Defined functions"""

"""" 1. Built in Functions:"""

"""" The functions which are coming along with python software automatically, are called 
     built in function or pre defined functions"""

""" Eg: id(), type(), input(), eval()"""

"""" 2. User Defined Functions:"""

""" The functions which are developed by programmer explicitly according to business requirements, are called user defined functions"""

""" Syntax to create user defined functions:"""
#
# def function_name(parameters):
#     """docstring"""
#     ---------
#     ---------
#     return value
#

""" While creating function we can use 2 keywords"""

"""" 1. def (mandatory)"""
"""" 2. return (optional) """


""" Write a function to print Hello"""

# def status():
#     print("Hello Good Morning")
# status()
# status()
# status()


"""Parameters"""

"""" Parameters are inputs to the function. If a function contain parameters, then at the time of calling
     compulsory we should provide values otherwise, otherwise we will get error"""

""" WAF to take name of the student as input and print wish message by name"""

def status(name):
    print("Hello", name, "Good Morning")
wish("Prabhat")
wish("Ravi")