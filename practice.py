#  Data type :
# Int Data type  :
a = 10
print(type(a))


# Being a developer we can pass specify literal values  in decimal, binary , octal and hexa decimal form.
# PVM will always provide values in decimal form only.

# We can represent int values in the foll0wing ways :
# Decimal form(base-10), Binary form(base-2), octal form(base-8, Hexa decimal form(base-16)
b = 10
print(b)
c = 0X10
print(c)
d = 0B10
print(d)

# Base Conversion :
# Python provides the following in-built function for base conversions.
# bin()  We can use any bin() to convert from any base to binary.


e = bin(15)
print(e)

# oct() : We can use oct() to convert any base to oct
f = oct(34)
print(f)
g = oct(10)
print(g)

# hex() : We can use hex() to convert any base to hexadecimal :
h = hex(100)
print(h)

# Float Data type :

# We can use float data type for representing floating point values : (decimal values)
fl = 1.234
print(type(fl))
# we can also represent floating point values by using exponetial form (scientific notations)
fe = 1.2e3
print(type(fe))
# The main advantage of exponential is we can represent big values in les memory.
#** we can represent int values in decimal,binary and ehx decimal forms. but we can represent float values by using decimal form only.

#fb = 0B11.01
#print(fb)  # We will get syntax error.


# Complex Data Type:
# A complex number is of the form :
# a + bj
# In the real part if we use int value then we can specify that either by decimal, octal, binary or hexa decimal form.
ca = 0B11+5j
print(ca)
type(ca)

# Complex data type has some inbuilt attributes to retrieve the real part and imaginary part.
c = 10.5+3.6j
print(c.real)
print(c.imag)

# Bool Data type :
# We can use this data type to represent boolean values :
# The only allowed values for this data type are : True and False :
# Internally  Python represents True as 1 and False as 0
bb = True
print(bb)
print(type(bb))


# Str Type :
# Str represents String data type
# A string is a sequence of characters enclosed with in single quotes or double quotes.
s1 = 'Prabhat'
s2 = "prabat"

# If it is required to represent multi line string literal  than we can use triple quotes : (""")

# Slicing of String :
# Slice means a piece
# [] operator is called slice operator, which can be used to retrieve parts of String.
# In python String follows zero based index
# The index can be either +ve or -ve.
# +ve index means forward direction from Left to Right.
# -ve index means backward direction from right to left.

ss = "prabhat"
print(ss[0])
print(ss[3])
print(ss[-1])
# print(ss[40]) # give index Error like string index out of range
print(ss[1:40])
print(ss[1:])
print(ss[:4])
print(ss[:])
print(ss*3)
print(len(ss))

# Note : In python the following data types are considered as Fundamental Data types.
# int, float, complex, bool , str