""""" List Data Structure: """

""" If we want to represent a group of individual objects as a single entity where insertion order preserved
     and duplicates are allowed, then we should go for list"""

"""Key points related to list"""
"""1. Insertion order preserved"""
"""2. Duplicate objects are allowed """
"""3. Heterogeneous objects are allowed"""
"""4. List is dynamic because based on our requirement we can increase the size and decrease the size"""
"""5. In List the elements will be placed within square brackets and with comma seperator."""

"""We can differentiate duplicate elements by using index and we can preserve insertion order by using index"""
"""Python supports both positive and negative indexex. +ve index means from left to right where as negative index means right to left"""


# Example: [10,"A", "B", 20, 30, 10]
# List objects are mutable. i.e we can change the content.

"""Creation of list objects"""
# We can create empty list object as follows:

# list = []
# print(list)
# print(type(list))


"""" If we know the elements already then we can create list as follows:"""
#
# list = [10, 20, 30, 40]
# print(type(list))
# print(list)

""" Example With Dynamic Input"""

# list = eval(input("Enter list:"))
# print(list)
# print(type(list))

"""With list() function"""
# Example 1
# l = list(range(0, 12, 2))
# print(l)
# print(type(l))

# Example 2
# s = "prabhat"
# l = list(s)
# print(l)

"""with split() function"""

# s = "we are all working at ltts"
# l = s.split()
# print(l)
# print(type(l))

""" Nested List"""

""" Sometimes we can take list inside another list, such type of lists are called nested lists."""
"""[10, 20, [30,40]]"""


"""Accessing elements of list:"""

""" We can access elements of the list either by using index or by using slice operator(:) """

""" 1. By using Index """

"""" List follows zero based index. ie index of first element is zero."""
""" List support both +ve and -ve indexes"""
""" + Index means left to right"""
""" -ve Index means for Right to left """


# list = [10, 20, 30, 40, 50]
# print(list[0])
# print(list[-1])
# print(list[2])

""" 2. By Using Slice Operator """

"""list2 = list1[start:stop:step]"""
"""start ==> it indicates the index where slice has to start"""
"""stop ==> it indicates the index where slice has to end"""
"""step ==> Increment value default value is 1"""
#
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(n[2:7:2])
# print(n[4::2])
# print(n[3:7])
# print(n[8:2:-2])
# print(n[4:100])


"""List is mutable"""
"""Once we create a list object, we can modify its content.Hence list object are mutable"""
#
# n = [10, 20, 30, 40]
# print(n)
# n[1] = 777
# print(n)


""" Traversing the elements of the list:"""
"""The sequential access of each element in the list is called traversal."""

""" 1. By using while loop:"""
# n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < len(n):
#     print(n[i])
#     i = i+1

""" 2. By Using For loop."""

# n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n1 in n:
#     print(n1)

""" To display only even numbers"""
#
# n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n1 in n:
#     if n1 % 2 == 0:
#         print(n1)

""" To display elements by index wise: """

# l = ["A", "B", "C", "D"]
# x = len(l)
# for i in range(x):
#     print(l[i], "is available at positive index:", i, "and at negative index:", i-x)


"""Function of list: """

""" 1. len() : returns the number of element present in the list"""

# n = [10, 20, 30, 40]
# print(len(n))


""" 2. count() : It returns the number of occurrences of specified item in the list"""

# n = [1, 2, 2, 2, 2, 3, 4, 3, 4]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))

""" 3. index() : Returns the index of first occurrence of the specified item."""

# n = [1, 2, 2, 2, 2, 2, 3, 3]
# print(n.index(1))
# print(n.index(2))
# print(n.index(3))
# To check item present in the list or not by using operator
# print(4 in n)

""" Manipulating elements of list: """

""" 1. append() function: """
""" We can use append() function to add item at the end of the list"""

# list = []
# list.append("A")
# list.append("B")
# list.append(1)
# list.append(12.0)
# print(list)

"""2. insert() function: """
"""To insert item at specified index position"""
#
# n = [1, 2, 3, 4, 5]
# n.insert(1,88)
# print(n)

# case study 1 : if the specified index is greater than max index
""" then element will be inserted at last position.
    If the specified index is smaller than min index then
    element will be inserted at first position"""
# n = [1, 2, 3, 4, 5]
# n.insert(10, 777)
# n.insert(-10, 999)
# print(n)


""" extend() function"""
""" To add all items of one list to another list """

"""l1.extend(l2) :: All items present in l2 will be added to l1"""
#
# l1 = ["Prabhat", "Kunal", "Gaurav"]
# l2 = ["K", "M"]
# l1.extend(l2)
# print(l1)


""" remove() function"""
""" We can use this function to remove specified item from the list.
if the item present multiple times then only first occurrence will be removed"""
#
# n = [10, 20, 30, 40]
# n.remove(30)
# print(n)

# if the specified item not present in list then we will get  value error


""" pop() function: """
""" It removes and returns the last element of the list"""
""" This is only function which manipulates list and returns some element"""
#
# n = [10, 20, 30, 40]
# print(n.pop())
# print(n.pop())
# print(n.pop())
# print(n)


""" 1. pop() is hte only function which manipulates the list and returns some value
    2. In general we can use append() and pop() functions to implement stack data structure
       by using list, which follows LIFO(Last in First Out) order"""
""" In general we can use pop() function to remove lst element of the list.
    But we can use remove element based on index."""

""" n.pop(index) ==> To remove and return element present at specified index"""
""" n.pop() ===> To remove and return last element of the list"""

#
# n = [10, 20, 30, 40, 50, 60]
# print(n.pop())
# print(n.pop(1))


"""" List object are dynamic: i.e. based on our requirement we can increase and decrease the size"""
""" append(), insert(), extend() ==> for increasing the size/growable nature"""
""" remove(), pop() =====> for decreasing the size/ shrinking nature"""

""" ===================================================================================================="""

""" Ordering Element of list"""

""" 1. reverse()"""
""" we can use to reverse() order of elements of list"""

n = [10, 20, 30, 40]
n.reverse()
print(n)

""" 2. sort() functions: """

"""" In list by default insertion order is preserved. If want to sort the elements of list according to default natural 
     sorting order then we should go for sort() method"""

""" For numbers ==> default natural sorting order is Ascending  Order """
""" For Strings ==> default natural sorting order is Alphabetical Order"""

# n = [20, 5, 15, 10, 0]
# n.sort()
# print(n)
#
# s = ["Dog", "Banana", "Cat", "Apple"]
# s.sort()
# print(s)

""" To use sort() function, compulsory list should contain only homogeneous elements otherwise we will get TypeError"""

""" To sort in reverse of default natural sorting order: """
#
# n = [40, 10, 30, 20]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)
# n.sort(reverse=False)
# print(n)

""" Aliasing and Cloning of list objects:"""

"""" The process of giving another reference variable to the existing list is called aliasing"""
#
# x = [10, 20, 30, 40]
# y = x
# print(id(x))
#

"""" The problem in this approach is by using one reference variable if we are changing content,
    then those changes will be reflected to the other reference variable"""

x = [10, 20, 30, 40]
y = x
y[1] = 777
print(x)

""" To overcome this problem we should go for cloning"""
""" The process of creating exactly duplicate independent object is called cloning """

""" We can implement cloning by using slice operator or by sing copy() function"""

x = [10, 20, 30, 40]
y = x[:]
y[1] = 777
print(x)
print(y)

"""By using copy() function"""
x = [10, 20, 30, 40]
y = x.copy()
y[1] = 777
print(x)
print(y)


"""" Mathematical operator for list object"""

""" 1. concatenation operator(+)"""

# a = [10, 20, 30]
# b = [40, 50, 60]
# c = a + b
# print(c)

# to use + operator compulsory both arguments should be list objects, otherwise we will get TypeError

""" 2. Repetation Operator(*)"""

""" We can use repetation operator * to repeat elements of list specified numbers of times """
# x = [10, 20, 30]
# y = x*3
# print(y)


"""" 3. Comparing list objects"""

x = ["Dog", "Cat", "Rat"]
y = ["DOG", "CAT", "RAT"]
z = ["Dog", "Cat", "Rat"]
#
# print(x==y)
# print(x==z)
# print(x != z)

""" 4. Relational operator: """

# x = [50, 20, 30]
# y = [40, 50, 60, 100, 200]
# print(x > y)
# print(x >= y)
# print(x < y)
# print(x <= y)
#

""" 5. Membership Operator"""
""" We can check whether element is a member of the list or not by using membership operator"""
""" in operator"""
""" not in operator"""
#
# n = [10, 20, 30, 40]
# print(10 in n)
# print(10 not in n)
# print(50 in n)
# print(50 not in n)

""" Clear() : clear function is used to remove all elements of list"""
#
# n = [10, 20, 30, 40]
# print(n)
# n.clear()
# print(n)


""" Nested Lists: """
# Sometime we can take one list inside another list. Such type of lists are called nested lists.
#
# n = [10, 20,[30,40]]
# print(n)
# print(n[0])
# print(n[2])
# print(n[2][0])
# print(n[2][1])

# We can access nested list elements by using index just like accessing multi dimensional array elements

""" List comprehensions"""

""" it is very easy and compact way of creating list objects from any iterable objects 
    like(list, tuple, dictionary, range etc) based on some conditions"""

# s = [x*x for x in range(1,11)]
# print(s)