""" Set Data Structure"""
""" If we want to represent a group of unique values as a single entity then we should go for set."""
""" Duplicate are not allowed"""
""" Insertion order is not preserved. But we can sort the elements"""
""" Indexing and slicing are not allowed for the set"""
""" Heterogeneous elements are allowed"""
""" Set are mutable
    i.e once we creates set object we can perform any changes in that object based on our requirement."""

""" We can apply mathematical operations like union, intersection, difference etc on set object"""

""" Creation of set object"""
# s = {10, 20, 30, 40}
# print(s)
# print(type(s))

""" We can create set objects by using set() function"""
# l = [10, 20, 30, 40 ,50]
# s = set(l)
# print(s)

""" While creating empty set we have to take special care. compulsory we should use set() function"""

# s = {}  # It is treated as dictionary but not empty set
# print(s)
# print(type(s))


""" Important functions of set"""

""" 1. add(x)"""
""" Add item x to the set"""
# s = {10, 20, 30}
# s.add(40)
# print(s)

""" 2. update(x,y,z)"""
""" To add multiple items to the set"""
""" Arguments are not individual elements and these are iterable objects like List, range etc."""
""" All elements present in the given Iterable objects will be added to the set"""
# s = {10, 20, 30}
# l = [40, 50, 60, 10]
# s.update(l,range(2))
# print(s)

# add we can use for individual item to the set
# Update() function to add multiple items to  the set.

""" 3. Return copy of the set"""
""" It is cloned object"""
#
# s = {10, 20, 30}
# s1 = s.copy()
# print(s1)

"""" 4. pop() : it removes and returns some random element from the set"""
#
# s = {40, 10, 30, 20}
# print(s)
# print(s.pop())
# print(s)

""" 5. remove(x):"""
""" It removes specified element from the set"""
""" if the specified element not present in the set then we will get KeyError"""

# s = {40, 10, 30, 20}
# s. remove(30)
# print(s)


""" 6. discard(x)"""

"""It removes the specified element from the set"""
"""if the specified element not present in the set then we won't get any error"""

# s = {10, 20, 30}
# s.discard(10)
# print(s)
# s.discard(50)
# print(s)
#

""" 7. Clear() : To remove all elements from the set"""
# s = {10, 20, 30}
# print(s)
# s.clear()
# print(s)


""" Mathematical Operation on Set"""

""" 1. union() : to return all elements present in both the set"""
#
# x = {10, 20, 30, 40}
# y = {10, 20, 30, 40}
# print(x.union(y))
# print(x|y)
""" 2. intersection() : Return common elemtns"""
# print(x.intersection(y))
# print(x&y)

""" 3. difference():"""
# returns element present in x but not in y
# print(x.difference(y))
# print(x-y)
# print(y-x)

"""" 4. symmetric difference() : return elemtns present in either x or y but not in both"""
# print(x.symmetric_difference(y))
# print(x^y)

""" Membership operator in or not in"""
#
# s = set("L&T")
# print(s)
# print('L' in s)
# print('P' in s)

""" Set comprehension"""
#
# s = {x*x for x in range(5)}

""" set objects won't support indexing and slicing"""

# s = {10,20.30}
# print(s[0])
# print(s[1:3])