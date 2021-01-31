""" Tuple Data Structure"""
""" 1. Tuple is exactly same as list except that it is immutable. i.e.
       Once we creates tuple object, we cannot perform any changes in that object"""
""" 2. If our data is fixed and never change then we should go for Tuple"""
""" 3. Insertion order is preserved"""
""" 4. Duplicates are allowed"""
""" 5. Heterogeneous objects are allowed"""
""" 6. We can preserve insertion order and we can differentiate duplicate objects by using index"""
""" 7. Tuples support both positive and negative index"""
""" 8. We can represents tuple elements within parenthesis with comma seperator, parenthesis are optional"""

# t =  10, 20, 30, 40
# print(t)
# print(type(t))


"""" WE hae to take special care about single valued tuple.
     compulsary the value should ends with comma, otherwise it is not treated as tuple"""

# t = (10)
# print(t)  # here t treated as integer
# print(type(t))

# t = (10,)
# print(t)   # here t treated as tuple
# print(type(t))

""" Tuple Creation"""

# t = ()  # Creation of empty tuple
# t = (10,)  # creation of single valued tuple, parenthesis are optional, should ends with comma

# creation of multi values tuples & parenthesis are optional
# t = (10, 20, 30)
# t = 10, 20, 30


""" By using tuple() function"""

list = [10, 20, 30]
t = tuple(list)
print(t)

""" Accessing elements of tuple"""
""" We can access either by index or by slice operator"""
""" By using index"""
t = (10, 20, 30, 40, 50, 60)
print(t[0])
print(t[-1])
print(t[4])


""" By using slice operator"""
t = (10, 20, 30, 40, 50, 60)
print(t[2:5])
print(t[2:100])
print(t[::2])

""" tuple are immutable"""

t = (10, 20, 30, 40, 50)
t[1] = 70  # Type Error : 'tuple' object does not support item assignment

""" Mathematical operators for tuple"""
""" 1. Concatenation Operator(+)"""

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# t3 = t1+t2
# print(t3)

""" 2. Multiplication operator or repetition operator(*)"""
t1 = (10, 20, 30)
t2 = t1 * t3
print(t2)

""" Important functions of tuples"""

""" 1. len()"""
""" To return number of elements present in the tuple"""
t = (10, 20, 30, 40)
print(len(t))

""" 2. count()"""
"""" To return number of occurences of given element in the tuple"""

t = (10, 20, 10, 10, 20)
print(t.count(10))

""" 3. index() """
"""" return index of first occurrence of the given element"""
""" if the specified element is not available then we will get ValueError"""

t = (10, 20, 10, 10, 20)
print(t.index(10))

"""" 4. Sorted()"""
""" To sort elements based on default natural sorting order"""

# t = (40, 10, 30, 20)
# t1 = sorted((t))
# print(t1)
# print(t)

# t1 = sorted(t, reverse=True)
# print(t1)

""" 5. min () and max() function"""

""" These functions return min and max values according to default natural sorting order"""

t = (40, 10, 30, 20)
print(min(t))
print(max(t))


"""" Tuple Packing and Unpacking:"""

""" We can create a tuple by packing a group of variables """
# a = 10
# b = 20
# c = 30
# d = 40
# t = a, b, c, d
# print(t)

"""Here a,b, cd are packed into a tuple t. This is nothing but tuple packing"""
""" Tuple unpacking is the reverse process of tuple packing"""
""" We can unpack a tuple and assign its values to different variables"""
t = (10, 20, 30, 40)
a, b, c, d = t
print("a=",a ,"b=",b, "c=",c ,"d=",d)


""" Tuple Comprehension:"""
""" Tuple comprehension is not supported by Python."""

t = (x**2 for x in range(1, 6))

# Here we are not getting tuple object and we are getting generator object.