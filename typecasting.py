""" We can convert one type value to another type.
This conversion is called Typecasting."""

""" Following are various in-built function for type casting"""

# int(), float(), complex(), bool(), str()

# int() method :
# we can use this function to convert values from other types to int()
print(int(123.45))
#print(int(10+5j))  # Complex value can't convert it.
print(int(True))
print(int(False))
print(int("10"))

"""Note 
  1. We can convert from any type to int except complex type.
  2. If we want to convert str type to int type, compulsary str should contain only integral value and should be specified  in base 10. 
"""

# print(int("Prabhat"))  #Invalid literals with base 10
# print(int("10.3"))    #Invalid literals with base 10
# print(int("0B1111"))   #Invalid literals with base 10

""" Float type casting"""

""" We can use float() function to convert other type values to float type"""

fi = print(float(10))
# fi = print(float(3 + 5j))  # Can't convert complex to float

fi = print(float(True))
fi = print(float(False))
f1 = print(float("12"))
f1 = print(float("12.0"))
# f1 = print(float("ten"))    # Could not convert string to float : 'ten'
# f1 = print(float("0B1111"))  # Could not convert string to float: '0B1111'


""" Complex() function  type casting """

""" We can use this function complex(x) to convert x into complex number with real part x and imaginary part 0"""
f2 = complex(10)
print(f2)

""" String (str)"""

""" We can use this method to convert other type values to str type """

print(type(str(100)))
# All data type will be  convert into string type.

""" All fundamental Data types are immutable. i.e. once we creates an object, we cannot perform any changes in that object.If
we are trying to change then with those change a new object will be created.
This non-changeable behaviour is called immutability."""

#ai = 10
bi = 10
ai = 11
print(id(ai))
print(id(bi))
#print(id(ai))

""" Byte Data type : """
""" The only allowed values for bytes data type are 0 to 256. By mistake if we are trying to provide any other values then we will get value error"""
""" Once we creates bytes data type value, we cannot change it's value, otherwise we will get TypeError"""
""" Bytes data type represents a group of byte numbers just like an array"""

x = [10, 20, 30, 40]
b = bytes(x)
# b[0] = 100  # Type error byte array
for i in b:
    print(i)

"""" Bytearray Data type: """

""" Bytearrary is exactly same as bytes data types except that its elements can be modified"""
x = [10, 20, 30, 40]
b = bytearray(x)
for i in b:
    print(i)
b[0] = 100
for i in b:print(i)


"""List Data Type"""
"""If we want to represent a group of values as a single entity where insertion order required
to preserve and duplicates are allowed then we should go for list data type"""

"""1. Insertion order is preserved"""
"""2. Hetrogenious objects are allowed"""
"""3. Duplicates are allowed"""
"""4. Growable in nature"""
"""5. values should be in closed within square brackets."""

list = [10,10.5, "Prabhat", 10,]
print(list)

list = [10, 20, 30, 40]
print(list)
print(list[0],list[-1])
print(list[1:3])

list[0] = 100
print(list)
list[1] = 200
print(list)
# list is growable in nature, i.e. based on our requirement we can increase or decrease the list
list = [23, 34, 56, 45]
list.append(("prabhat"))
print(list)
list.append("Kumar")
print(list)
print(type(list))
list2 = list*2
print(list2)

""" Note : An ordered,mutable, heterogenous collection of elements is nothing but list, where duplicates also allowed"""


""" Tuple Data type : """
""" Tuple data type is exactly same as list data type except that it is immutable. i.e. we can not change value"""
""" Tuple elements represented within parenthesis"""

t = (10, 20, 30, 40)
print(type(t))

p = (45, 67, 45, 67)
print(type(t))
print(p[0])
# p[0] = 100  # Tuple object does not support assignment
# print(p)
# p.remove(67)  # Attribute Error : tuple object as no attribute remove.
# print(p)
#p.append(100)  # Attribute Error : tuple object as no attribute append.
# print(p)

"""  Or else we say that tuple is the read only version of list"""



""" Range Data Type"""
""" Range data type represents a sequence of numbers. """

""" The elements present in the range is not modifiable . i.e. range Data type is immutable."""

ar = range(10)
print(ar)
for i in range(10):
    print(i)

ar2 = range(10, 20)
print(ar2)
for i in ar2:
    print(i)

ar3 = range(10, 20, 2)
print(type(ar3))
for i in ar3:
    print(i)

""" In range we can access the element through index also."""

r = range(10, 20)
print("Access the range value through index")
print(r[0])

"""We cannot modify the value of range datatype: """
#r[0]= 100  # Range object does not support item assignment.
#print(r)


""" Set Data type"""

""" If we want to represent a group of values without duplicate where order is not important then we should go for set Data type. """
""" 1. Insertion order is not preserved"""
""" 2. duplicate is not allowed"""
"""3. hetrogenious objects are allowed"""
""" 4. Index concept is not applicable"""
"""" 5. it is mutable collection"""
""" 6. Growable in nature"""

s = {100, 0, 20, 10, 'Prabhat'}
print("Insertion order is not preserved")
print(s)
# print(s[0]) # TypeError: 'set' object does not support indexing.

s.add(60)
print(s)
s.remove('Prabhat')
print(s)

""" Frozenset Data Type """
""" It is exactly same as set but except immutable"""
""" Hence we cannot use add or remove function"""

s = {10, 20, 30, 40}
fs = frozenset(s)
print(type(fs))

""" Dictionary Data type"""
""" If we want to represent a group of value with key-value pair than we should go for Dictionary"""

d = {101:'prabhat', 102:'suraj', 103:'kunal'}

"""Duplicate keys is not allowed,but duplicate values is allowed, if we are trying to update with duplicate keys than values should be updated."""
print(d)
print(d[101])

"""WE can create empty dictionary """

de = {}
print(de)
de[1]= 'Prabhat'
de[2]= 'Kumnal'
de['Name'] = 23
print(de)

"""Dict is mutable and the order wont be preserved"""
""" 1. In general we can use bytes and bytearray data types to represent binary information  like images, video files etc"""
""" 2. In python 2 login data type is available. But in python 3 it is not available and we can represent long values also by using int type only"""
""" 3. In Python there is no char data type. Hence we can represent char values also by using str type"""

""" None Data Type : """
""" None means nothing no values associated"""
""" If value is not available, then to handle such type of case None introduced."""

def m1():
    a = 10
print(m1())

# Constant :
# Constant concept is not included in python :
""" But it is convention to use only uppercase characters if we don't want to change value"""
""" MAX_VALUE = 10 It is just convention but we can change the value"""